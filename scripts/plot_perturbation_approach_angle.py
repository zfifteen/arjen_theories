#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/arjen_theories_matplotlib")

import matplotlib

matplotlib.use("Agg")

from matplotlib import colors
from matplotlib import pyplot as plt
from matplotlib.patches import Patch


STATUS_TO_CODE = {"no": 0, "yes": 1, "ambiguous": 2}
CODE_TO_MARK = {0: "N", 1: "Y", 2: "A"}


def load_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if not rows:
        raise ValueError(f"{csv_path} is empty")
    return rows


def build_status_matrix(rows: list[dict[str, str]]) -> tuple[list[float], list[float], list[list[int]]]:
    omega_reference_ratios = sorted({float(row["omega_reference_ratio"]) for row in rows})
    approach_angle_degrees = sorted({float(row["approach_angle_degrees"]) for row in rows})

    matrix = [[None for _ in omega_reference_ratios] for _ in approach_angle_degrees]

    x_index = {value: index for index, value in enumerate(omega_reference_ratios)}
    y_index = {value: index for index, value in enumerate(approach_angle_degrees)}

    for row in rows:
        status = row["gliding_contact_occurs"]
        if status not in STATUS_TO_CODE:
            raise ValueError(f"unsupported gliding status: {status}")

        x_value = float(row["omega_reference_ratio"])
        y_value = float(row["approach_angle_degrees"])
        if y_value > 0.0 and status != "ambiguous":
            raise ValueError(
                "nonzero approach_angle rows must remain ambiguous under the current "
                f"contract, got {status} for approach_angle_degrees={y_value}"
            )

        x_position = x_index[x_value]
        y_position = y_index[y_value]

        if matrix[y_position][x_position] is not None:
            raise ValueError(
                "duplicate grid cell for "
                f"omega/omega_0={x_value}, approach_angle_degrees={y_value}"
            )

        matrix[y_position][x_position] = STATUS_TO_CODE[status]

    for y_position, row in enumerate(matrix):
        for x_position, value in enumerate(row):
            if value is None:
                raise ValueError(
                    "missing grid cell for "
                    f"omega/omega_0={omega_reference_ratios[x_position]}, "
                    f"approach_angle_degrees={approach_angle_degrees[y_position]}"
                )

    return omega_reference_ratios, approach_angle_degrees, matrix


def render_figure(
    omega_reference_ratios: list[float],
    approach_angle_degrees: list[float],
    matrix: list[list[int]],
    output_path: Path,
) -> None:
    cmap = colors.ListedColormap(["#d9e7f5", "#74c476", "#d9d9d9"])
    norm = colors.BoundaryNorm([-0.5, 0.5, 1.5, 2.5], cmap.N)

    fig, ax = plt.subplots(figsize=(10.5, 6.8), constrained_layout=False)
    image = ax.imshow(matrix, cmap=cmap, norm=norm, aspect="auto", origin="lower")
    image.set_interpolation("nearest")

    ax.set_xticks(range(len(omega_reference_ratios)))
    ax.set_xticklabels([f"{value:g}" for value in omega_reference_ratios])
    ax.set_yticks(range(len(approach_angle_degrees)))
    ax.set_yticklabels([f"{value:g}" for value in approach_angle_degrees])
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel("approach angle (degrees)")
    ax.set_title("Approach-Angle Perturbation Status Matrix")

    threshold_index = omega_reference_ratios.index(1.0)
    ax.axvline(
        threshold_index,
        color="#333333",
        linewidth=1.5,
        linestyle="--",
        label=r"special-case threshold $\omega / \omega_0 = 1$",
    )

    ax.set_xticks([tick - 0.5 for tick in range(1, len(omega_reference_ratios))], minor=True)
    ax.set_yticks([tick - 0.5 for tick in range(1, len(approach_angle_degrees))], minor=True)
    ax.grid(which="minor", color="white", linewidth=1.4)
    ax.tick_params(which="minor", bottom=False, left=False)

    for y_position, row in enumerate(matrix):
        for x_position, value in enumerate(row):
            mark = CODE_TO_MARK[value]
            ax.text(
                x_position,
                y_position,
                mark,
                ha="center",
                va="center",
                color="#1a1a1a",
                fontsize=11,
                fontweight="bold",
            )

    legend_items = [
        Patch(facecolor="#d9e7f5", edgecolor="none", label="No supported gliding contact"),
        Patch(facecolor="#74c476", edgecolor="none", label="Supported gliding contact"),
        Patch(facecolor="#d9d9d9", edgecolor="none", label="Ambiguous under current source set"),
    ]
    ax.legend(
        handles=legend_items,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.16),
        ncol=3,
        frameon=False,
    )

    fig.text(
        0.5,
        0.035,
        "Perpendicular-approach control retains the special-case transition. "
        r"Every nonzero approach-angle row remains ambiguous because no family-specific "
        r"gliding or $\tau_{contact}$ law is available in the current source set.",
        ha="center",
        va="center",
        fontsize=10,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Render the canonical approach-angle perturbation figure."
    )
    parser.add_argument(
        "--input",
        default=repo_root / "results" / "perturbation_approach_angle.csv",
        type=Path,
        help="Path to the canonical approach-angle perturbation CSV.",
    )
    parser.add_argument(
        "--output",
        default=repo_root / "figures" / "perturbation_approach_angle.png",
        type=Path,
        help="Path for the rendered PNG figure.",
    )
    args = parser.parse_args()

    rows = load_rows(args.input)
    omega_reference_ratios, approach_angle_degrees, matrix = build_status_matrix(rows)
    render_figure(omega_reference_ratios, approach_angle_degrees, matrix, args.output)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
