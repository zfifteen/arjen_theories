#!/usr/bin/env python3

"""Deterministic special-case instrument for the constrained RVM collision."""

from __future__ import annotations

import argparse
import csv
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, TextIO


REL_TOL = 1e-12
ABS_TOL = 1e-12
DEFAULT_LENGTH = 2.0
DEFAULT_SEPARATION_SPEED = 1.0
DEFAULT_OMEGA_VALUES = (1.0, math.pi / 2.0, 2.0)
FIELDNAMES = [
    "omega",
    "length",
    "separation_speed",
    "omega_0",
    "omega_ratio",
    "v_tip",
    "t_rot",
    "t_clear",
    "delta_t",
    "s_re",
    "ell_rem",
    "first_reencounter_location",
    "interior_reencounter_occurs",
    "gliding_contact_occurs",
    "regime",
    "tau_contact_supported",
    "tau_contact",
    "tau_contact_status",
]


@dataclass(frozen=True)
class Observation:
    omega: str
    length: str
    separation_speed: str
    omega_0: str
    omega_ratio: str
    v_tip: str
    t_rot: str
    t_clear: str
    delta_t: str
    s_re: str
    ell_rem: str
    first_reencounter_location: str
    interior_reencounter_occurs: str
    gliding_contact_occurs: str
    regime: str
    tau_contact_supported: str
    tau_contact: str
    tau_contact_status: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=(
            "Compute the supported special-case collision observables from "
            "dijksman_rvm_revised.md and special_case_derivation.md."
        )
    )
    parser.add_argument(
        "omega",
        nargs="*",
        type=positive_float,
        default=list(DEFAULT_OMEGA_VALUES),
        help="One or more angular-speed values to evaluate.",
    )
    parser.add_argument(
        "--length",
        default=DEFAULT_LENGTH,
        type=positive_float,
        help="Segment length L.",
    )
    parser.add_argument(
        "--separation-speed",
        default=DEFAULT_SEPARATION_SPEED,
        type=positive_float,
        help="Separation speed c.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional CSV output path. If omitted, rows are written to stdout.",
    )
    return parser.parse_args()


def positive_float(raw_value: str) -> float:
    value = float(raw_value)
    if value <= 0.0:
        raise argparse.ArgumentTypeError("value must be positive")
    return value


def format_float(value: float) -> str:
    return format(value, ".15g")


def classify_regime(omega: float, omega_0: float) -> tuple[str, str, str, str]:
    if math.isclose(omega, omega_0, rel_tol=REL_TOL, abs_tol=ABS_TOL):
        return (
            "critical_recollision",
            "tip",
            "no",
            "no",
        )
    if omega < omega_0:
        return (
            "instantaneous_contact",
            "off_segment",
            "no",
            "no",
        )
    return (
        "non_instantaneous_gliding_contact",
        "interior",
        "yes",
        "yes",
    )


def compute_observation(omega: float, length: float, separation_speed: float) -> Observation:
    omega_0 = math.pi * separation_speed / length
    omega_ratio = omega / omega_0
    v_tip = omega * length / 2.0
    t_rot = math.pi / (2.0 * omega)
    t_clear = length / (2.0 * separation_speed)
    delta_t = t_clear - t_rot
    s_re = math.pi * separation_speed / (2.0 * omega)
    ell_rem = length / 2.0 - s_re
    regime, first_reencounter_location, interior_reencounter_occurs, gliding_contact_occurs = (
        classify_regime(omega, omega_0)
    )

    return Observation(
        omega=format_float(omega),
        length=format_float(length),
        separation_speed=format_float(separation_speed),
        omega_0=format_float(omega_0),
        omega_ratio=format_float(omega_ratio),
        v_tip=format_float(v_tip),
        t_rot=format_float(t_rot),
        t_clear=format_float(t_clear),
        delta_t=format_float(delta_t),
        s_re=format_float(s_re),
        ell_rem=format_float(ell_rem),
        first_reencounter_location=first_reencounter_location,
        interior_reencounter_occurs=interior_reencounter_occurs,
        gliding_contact_occurs=gliding_contact_occurs,
        regime=regime,
        tau_contact_supported="no",
        tau_contact="",
        tau_contact_status="undetermined_from_source_note",
    )


def write_rows(rows: Iterable[Observation], stream: TextIO) -> None:
    writer = csv.DictWriter(stream, fieldnames=FIELDNAMES, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow(asdict(row))


def main() -> int:
    args = parse_args()
    rows = [
        compute_observation(
            omega=omega,
            length=args.length,
            separation_speed=args.separation_speed,
        )
        for omega in args.omega
    ]

    if args.output is None:
        write_rows(rows, sys.stdout)
        return 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        write_rows(rows, handle)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
