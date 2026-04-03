#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import os
import textwrap
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/arjen_theories_matplotlib")

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt
from matplotlib.lines import Line2D


REGIME_STYLE = {
    "instantaneous_contact": {
        "label": "Instantaneous contact",
        "marker": "s",
        "color": "#c0392b",
    },
    "critical_recollision": {
        "label": "Critical recollision",
        "marker": "D",
        "color": "#444444",
    },
    "non_instantaneous_gliding_contact": {
        "label": "Non-instantaneous gliding contact",
        "marker": "o",
        "color": "#245b8f",
    },
}


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if not rows:
        raise ValueError(f"{csv_path} is empty")
    return rows


def render_figure(rows: list[dict[str, str]], output_path: Path) -> None:
    omega_ratios = [float(row["omega_ratio"]) for row in rows]
    ell_rem_values = [float(row["ell_rem"]) for row in rows]

    fig, ax = plt.subplots(figsize=(7.0, 5.8), constrained_layout=False)

    ax.plot(
        omega_ratios,
        ell_rem_values,
        color="#97a6a8",
        linewidth=2.0,
        zorder=1,
    )

    for row in rows:
        regime = row["regime"]
        if regime not in REGIME_STYLE:
            raise ValueError(f"unsupported regime: {regime}")
        style = REGIME_STYLE[regime]
        ax.scatter(
            float(row["omega_ratio"]),
            float(row["ell_rem"]),
            s=110,
            marker=style["marker"],
            color=style["color"],
            edgecolor="white",
            linewidth=0.9,
            zorder=3,
        )

    ax.axvline(1.0, color="#333333", linewidth=1.5, linestyle="--", zorder=2)
    ax.axhline(0.0, color="#555555", linewidth=1.2, zorder=2)

    ax.set_title("Fixed Special-Case Threshold Sweep", fontsize=19, pad=14)
    ax.set_xlabel(r"Angular-speed ratio $\omega / \omega_0$", fontsize=12)
    ax.set_ylabel(r"Interior margin $\ell_{\mathrm{rem}} = L/2 - s_{\mathrm{re}}$", fontsize=12)

    ax.set_xlim(0.45, 1.55)
    ax.set_ylim(-1.08, 0.42)
    ax.grid(axis="y", color="#d7d7d7", linewidth=1.0)
    ax.set_axisbelow(True)

    ax.text(
        1.01,
        0.98,
        r"threshold $\omega / \omega_0 = 1$",
        transform=ax.get_xaxis_transform(),
        ha="left",
        va="top",
        fontsize=10,
        color="#333333",
    )

    legend_handles = [
        Line2D(
            [0],
            [0],
            marker=style["marker"],
            color="none",
            markerfacecolor=style["color"],
            markeredgecolor="white",
            markeredgewidth=0.9,
            markersize=9,
            label=style["label"],
        )
        for style in REGIME_STYLE.values()
    ]
    ax.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.16),
        ncol=2,
        frameon=False,
        fontsize=11,
        columnspacing=1.6,
        handletextpad=0.7,
    )

    note = (
        "Negative values place the first re-encounter beyond the available half-length. "
        "Zero is the tip case. Positive values move the first re-encounter into the interior."
    )
    fig.text(
        0.5,
        0.04,
        textwrap.fill(note, width=94),
        ha="center",
        va="bottom",
        fontsize=10,
        color="#333333",
    )

    fig.subplots_adjust(left=0.14, right=0.98, top=0.9, bottom=0.28)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Render the canonical special-case threshold figure."
    )
    parser.add_argument(
        "--input",
        default=repo_root / "results" / "special_case_threshold.csv",
        type=Path,
        help="Path to the canonical special-case threshold CSV.",
    )
    parser.add_argument(
        "--output",
        default=repo_root / "figures" / "special_case_threshold.png",
        type=Path,
        help="Path for the rendered PNG figure.",
    )
    args = parser.parse_args()

    rows = load_rows(args.input)
    render_figure(rows, args.output)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
