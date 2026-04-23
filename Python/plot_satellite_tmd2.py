"""
Representa temperaturas de nodos o etiquetas del .TMD2 del satélite.

Ejemplos:
    python plot_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --label battery_pack
    python plot_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --label obc_box --label comms_box
    python plot_satellite_tmd2.py SAT_TFG_CASO_01.TMD2 --nodes 10000 10001 10002
"""
from __future__ import annotations

import argparse

import matplotlib.pyplot as plt

from tmd2_reader import aggregate_by_label, extract_attribute, load_tmd2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Gráficas rápidas para un archivo TMD2.")
    p.add_argument("tmd2_file", help="Ruta al archivo .TMD2")
    p.add_argument("--label", action="append", help="Etiqueta exacta a representar. Repetible.")
    p.add_argument("--nodes", nargs="+", type=int, help="Nodos concretos a representar")
    p.add_argument("--attribute", default="Temperature", help="Atributo a representar")
    p.add_argument("--stat", default="mean", choices=["mean", "min", "max", "sum"], help="Agregación para etiquetas")
    p.add_argument("--time-unit", default="s", choices=["s", "min", "h", "days"], help="Unidad temporal")
    return p


def convert_time(times_s, unit):
    if unit == "s":
        return times_s, "Time (s)"
    if unit == "min":
        return times_s / 60.0, "Time (min)"
    if unit == "h":
        return times_s / 3600.0, "Time (h)"
    return times_s / 86400.0, "Time (days)"


def main():
    args = build_parser().parse_args()
    data = load_tmd2(args.tmd2_file)
    x, xlabel = convert_time(data.times_s, args.time_unit)

    plt.figure()

    used_any = False

    if args.label:
        for label in args.label:
            y = aggregate_by_label(data, label=label, attribute=args.attribute, stat=args.stat)
            plt.plot(x, y.values, label=f"{label} ({args.stat})")
            used_any = True

    if args.nodes:
        df = extract_attribute(data, attribute=args.attribute, node_numbers=args.nodes)
        for node in df.columns:
            plt.plot(x, df[node].values, label=f"Node {node}")
            used_any = True

    if not used_any:
        raise SystemExit("Indica --label o --nodes")

    plt.xlabel(xlabel)
    plt.ylabel(args.attribute)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
