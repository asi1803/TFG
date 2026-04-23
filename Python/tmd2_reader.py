"""
Lector reutilizable para archivos ESATAN .TMD/.TMD2 basado en la estructura
detectada en SAT_TFG_CASO_01.TMD2.

Funciones principales:
- load_tmd2: abre el archivo y devuelve metadatos + arrays
- nodes_table: devuelve tabla de nodos
- time_series_dataframe: devuelve DataFrame ancho con índice temporal
- select_nodes: filtra nodos por etiqueta, tipo o lista de nodos
- extract_attribute: extrae un atributo por nodo y tiempo
- aggregate_by_label: agrega una magnitud para una etiqueta

Requisitos:
    pip install h5py pandas numpy
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Sequence

import h5py
import numpy as np
import pandas as pd


THERMAL_GROUP = "AnalysisSet1"
DATA_GROUP = f"{THERMAL_GROUP}/DataGroup1"


@dataclass
class TMD2Data:
    path: str
    times_s: np.ndarray
    node_numbers: np.ndarray
    node_internal_numbers: np.ndarray
    node_types: np.ndarray
    node_labels: np.ndarray
    real_attribute_names: list[str]
    string_attribute_names: list[str]
    thermal_real_data: np.ndarray

    @property
    def times_min(self) -> np.ndarray:
        return self.times_s / 60.0

    @property
    def times_h(self) -> np.ndarray:
        return self.times_s / 3600.0

    @property
    def times_days(self) -> np.ndarray:
        return self.times_s / 86400.0


def _decode_array(arr: np.ndarray) -> np.ndarray:
    if arr.dtype.kind == "S":
        return arr.astype(str)
    return arr


def _read_required_dataset(h5: h5py.File, key: str) -> np.ndarray:
    if key not in h5:
        raise KeyError(f"No existe el dataset requerido: {key}")
    return h5[key][:]


def load_tmd2(filename: str | Path) -> TMD2Data:
    filename = str(filename)
    with h5py.File(filename, "r") as h5:
        node_numbers = _read_required_dataset(h5, f"{THERMAL_GROUP}/thermalNodes")[:, 0]
        thermal_real_data = _read_required_dataset(h5, f"{DATA_GROUP}/thermalNodesRealData")
        thermal_string_data = _read_required_dataset(h5, f"{DATA_GROUP}/thermalNodesStringData")
        times_s = _read_required_dataset(h5, f"{DATA_GROUP}/times")

        real_attribute_names = [
            x.decode() if isinstance(x, (bytes, np.bytes_)) else str(x)
            for x in _read_required_dataset(h5, f"{THERMAL_GROUP}/thermalNodesRealAttributes")
        ]
        string_attribute_names = [
            x.decode() if isinstance(x, (bytes, np.bytes_)) else str(x)
            for x in _read_required_dataset(h5, f"{THERMAL_GROUP}/thermalNodesStringAttributes")
        ]

        node_types = _decode_array(thermal_string_data[0, :, 0])
        node_labels = _decode_array(thermal_string_data[0, :, 1])
        node_internal_numbers = np.arange(len(node_numbers), dtype=int)

    return TMD2Data(
        path=filename,
        times_s=np.asarray(times_s, dtype=float),
        node_numbers=np.asarray(node_numbers, dtype=int),
        node_internal_numbers=node_internal_numbers,
        node_types=np.asarray(node_types),
        node_labels=np.asarray(node_labels),
        real_attribute_names=real_attribute_names,
        string_attribute_names=string_attribute_names,
        thermal_real_data=np.asarray(thermal_real_data, dtype=float),
    )


def nodes_table(data: TMD2Data) -> pd.DataFrame:
    df = pd.DataFrame(
        {
            "node": data.node_numbers,
            "internal_node": data.node_internal_numbers,
            "type": data.node_types,
            "label": data.node_labels,
        }
    )
    return df


def time_series_dataframe(data: TMD2Data) -> pd.DataFrame:
    """Devuelve DataFrame ancho con columnas MultiIndex: (node, attribute)."""
    columns = pd.MultiIndex.from_product(
        [data.node_numbers, data.real_attribute_names],
        names=["node", "attribute"],
    )
    raw = np.concatenate(
        [data.thermal_real_data[:, :, i] for i in range(data.thermal_real_data.shape[2])],
        axis=1,
    )
    return pd.DataFrame(raw, index=data.times_s, columns=columns)


def _normalize_attribute_name(name: str) -> str:
    return name.strip().lower().replace(" ", "_").replace("-", "_")


def resolve_attribute_name(data: TMD2Data, requested: str) -> str:
    req = _normalize_attribute_name(requested)
    mapping = {_normalize_attribute_name(x): x for x in data.real_attribute_names}
    if req in mapping:
        return mapping[req]

    aliases = {
        "t": "Temperature",
        "temp": "Temperature",
        "temperature": "Temperature",
        "c": "Capacitance",
        "capacitance": "Capacitance",
        "qa": "Total_Albedo_Heat_Source",
        "qe": "Total_Earth_Heat_Source",
        "qi": "Total_Internal_Heat_Source",
        "qr": "Total_Rest_Heat_Source",
        "qs": "Total_Solar_Heat_Source",
        "area": "Area",
        "alpha": "Solar_Absorptivity",
        "epsilon": "Infra-Red_Emissivity",
        "incident_albedo": "Incident_Albedo_Heat_Source",
        "incident_earth": "Incident_Earth_Heat_Source",
        "incident_solar": "Incident_Solar_Heat_Source",
        "x": "X_Coordinate",
        "y": "Y_Coordinate",
        "z": "Z_Coordinate",
    }
    if req in aliases and aliases[req] in data.real_attribute_names:
        return aliases[req]

    raise KeyError(
        f"Atributo no encontrado: {requested}. "
        f"Disponibles: {', '.join(data.real_attribute_names)}"
    )


def select_nodes(
    data: TMD2Data,
    labels: Optional[Sequence[str]] = None,
    node_types: Optional[Sequence[str]] = None,
    node_numbers: Optional[Sequence[int]] = None,
    contains: Optional[str] = None,
) -> pd.DataFrame:
    nodes = nodes_table(data)
    mask = pd.Series(True, index=nodes.index)

    if labels:
        mask &= nodes["label"].isin(labels)

    if node_types:
        mask &= nodes["type"].isin(node_types)

    if node_numbers:
        mask &= nodes["node"].isin(node_numbers)

    if contains:
        mask &= nodes["label"].str.contains(contains, case=False, regex=False)

    return nodes.loc[mask].copy()


def extract_attribute(
    data: TMD2Data,
    attribute: str = "Temperature",
    labels: Optional[Sequence[str]] = None,
    node_types: Optional[Sequence[str]] = None,
    node_numbers: Optional[Sequence[int]] = None,
    contains: Optional[str] = None,
) -> pd.DataFrame:
    attribute = resolve_attribute_name(data, attribute)
    selected = select_nodes(
        data,
        labels=labels,
        node_types=node_types,
        node_numbers=node_numbers,
        contains=contains,
    )
    if selected.empty:
        raise ValueError("No hay nodos que cumplan el filtro indicado.")

    attr_idx = data.real_attribute_names.index(attribute)
    cols = list(selected["node"].astype(int))
    node_pos = [np.where(data.node_numbers == n)[0][0] for n in cols]
    values = data.thermal_real_data[:, node_pos, attr_idx]

    df = pd.DataFrame(values, index=data.times_s, columns=cols)
    df.index.name = "time_s"
    return df


def aggregate_by_label(
    data: TMD2Data,
    label: str,
    attribute: str = "Temperature",
    stat: str = "mean",
) -> pd.Series:
    df = extract_attribute(data, attribute=attribute, labels=[label])
    stat = stat.lower()
    if stat == "mean":
        return df.mean(axis=1)
    if stat == "min":
        return df.min(axis=1)
    if stat == "max":
        return df.max(axis=1)
    if stat == "sum":
        return df.sum(axis=1)
    raise ValueError("stat debe ser one of: mean, min, max, sum")


def summary(data: TMD2Data) -> dict:
    nodes = nodes_table(data)
    return {
        "file": data.path,
        "n_times": int(len(data.times_s)),
        "n_nodes": int(len(data.node_numbers)),
        "time_start_s": float(data.times_s[0]),
        "time_end_s": float(data.times_s[-1]),
        "types": sorted(nodes["type"].astype(str).unique().tolist()),
        "labels": sorted(nodes["label"].astype(str).unique().tolist()),
        "attributes": list(data.real_attribute_names),
    }


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) < 2:
        print("Uso: python tmd2_reader.py archivo.TMD2")
        raise SystemExit(1)

    data = load_tmd2(sys.argv[1])
    print(json.dumps(summary(data), indent=2, ensure_ascii=False))
