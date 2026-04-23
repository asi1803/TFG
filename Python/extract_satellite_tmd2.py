"""
Script CLI para leer SAT_TFG_CASO_01.TMD2 y exportar su información.

Ejemplos:
    python extract_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --summary
    python extract_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --list-labels
    python extract_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --label battery_pack --attribute Temperature --csv battery_pack_temp.csv
    python extract_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --internal-only --all-labels-csv temperaturas_internas.csv

Si no pasas --csv, el script genera:
- nodes_catalog.csv
- labels_catalog.csv
en la carpeta de salida.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from tmd2_reader import (
    aggregate_by_label,
    extract_attribute,
    load_tmd2,
    nodes_table,
    summary,
)


DEFAULT_INTERNAL_LABELS = [
    "adcs_unit",
    "battery_pack",
    "body_plate_inf",
    "body_plate_med",
    "body_plate_sup",
    "camera_base",
    "camera_cyl",
    "camera_electronics",
    "camera_lens",
    "comms_box",
    "obc_box",
]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Extractor para archivos ESATAN TMD2 del satélite.")
    p.add_argument("tmd2_file", help="Ruta al archivo .TMD2")
    p.add_argument("--outdir", default="output_tmd2", help="Carpeta de salida")
    p.add_argument("--summary", action="store_true", help="Imprime resumen del archivo")
    p.add_argument("--list-labels", action="store_true", help="Lista etiquetas disponibles")
    p.add_argument("--label", action="append", help="Etiqueta exacta a extraer. Repetible.")
    p.add_argument("--contains", help="Subcadena a buscar en label")
    p.add_argument("--type", action="append", dest="node_types", help="Tipo de nodo (D, B, X)")
    p.add_argument("--node", action="append", type=int, dest="nodes", help="Nodo de usuario concreto. Repetible.")
    p.add_argument("--attribute", default="Temperature", help="Atributo a extraer")
    p.add_argument("--stat", default="mean", choices=["mean", "min", "max", "sum"], help="Agregación por etiqueta")
    p.add_argument("--csv", help="Nombre CSV para la extracción pedida")
    p.add_argument("--all-labels-csv", help="Exporta una tabla con una columna por label agregado")
    p.add_argument("--internal-only", action="store_true", help="Limita la exportación multi-label a elementos internos")
    return p


def main() -> None:
    args = build_parser().parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    data = load_tmd2(args.tmd2_file)
    nodes = nodes_table(data)
    nodes.to_csv(outdir / "nodes_catalog.csv", index=False)

    labels_catalog = (
        nodes.groupby(["label", "type"])
        .size()
        .rename("count")
        .reset_index()
        .sort_values(["label", "type"])
    )
    labels_catalog.to_csv(outdir / "labels_catalog.csv", index=False)

    if args.summary:
        info = summary(data)
        print("Resumen:")
        for k, v in info.items():
            print(f"- {k}: {v}")

    if args.list_labels:
        print("Etiquetas disponibles:")
        for label in sorted(nodes["label"].unique()):
            n = int((nodes["label"] == label).sum())
            print(f"  {label} ({n} nodos)")

    if args.all_labels_csv:
        labels = sorted(nodes["label"].unique())
        if args.internal_only:
            labels = [x for x in labels if x in DEFAULT_INTERNAL_LABELS]

        table = pd.DataFrame(index=data.times_s)
        table.index.name = "time_s"
        for label in labels:
            table[label] = aggregate_by_label(
                data,
                label=label,
                attribute=args.attribute,
                stat=args.stat,
            ).values

        outfile = outdir / args.all_labels_csv
        table.to_csv(outfile)
        print(f"Archivo generado: {outfile}")

    if args.label or args.contains or args.node_types or args.nodes:
        df = extract_attribute(
            data,
            attribute=args.attribute,
            labels=args.label,
            node_types=args.node_types,
            node_numbers=args.nodes,
            contains=args.contains,
        )
        if args.csv:
            outfile = outdir / args.csv
        else:
            outfile = outdir / "extraction.csv"
        df.to_csv(outfile)
        print(f"Archivo generado: {outfile}")


if __name__ == "__main__":
    main()
