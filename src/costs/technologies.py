from dataclasses import dataclass
from pathlib import Path

import yaml

REQUIRED_KEYS = {
    "name",
    "carrier",
    "investment_eur_per_kw",
    "fom_percent_per_year",
    "lifetime_years",
    "source",
}


@dataclass(frozen=True)
class Technology:
    name: str
    carrier: str
    investment_eur_per_kw: float
    fom_percent_per_year: float
    lifetime_years: int
    source: str


def load_technology(path: Path) -> Technology:
    data = yaml.safe_load(path.read_text())
    missing = REQUIRED_KEYS - data.keys()
    unknown = data.keys() - REQUIRED_KEYS
    if missing:
        raise ValueError(f"{path}: missing keys {sorted(missing)}")
    if unknown:
        raise ValueError(f"{path}: unknown keys {sorted(unknown)}")
    if data["name"] != path.stem:
        raise ValueError(f"{path}: name '{data['name']}' must match file name")
    return Technology(**data)


def load_technologies(directory: Path) -> list[Technology]:
    return [load_technology(p) for p in sorted(directory.glob("*.yaml"))]
