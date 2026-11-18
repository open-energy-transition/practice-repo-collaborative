from pathlib import Path

import pytest
import yaml

from costs import load_technologies

VALID = {
    "name": "demo",
    "carrier": "gas",
    "investment_eur_per_kw": 800,
    "fom_percent_per_year": 3.0,
    "lifetime_years": 25,
    "source": "test",
}


def write(directory: Path, data: dict) -> None:
    (directory / "demo.yaml").write_text(yaml.safe_dump(data))


def test_valid_file_loads(tmp_path: Path) -> None:
    write(tmp_path, VALID)
    [tech] = load_technologies(tmp_path)
    assert tech.lifetime_years == 25


@pytest.mark.parametrize(
    ("data", "error"),
    [
        ({k: v for k, v in VALID.items() if k != "source"}, "missing keys"),
        ({**VALID, "colour": "red"}, "unknown keys"),
        ({**VALID, "name": "other"}, "must match"),
    ],
)
def test_invalid_file_raises(tmp_path: Path, data: dict, error: str) -> None:
    write(tmp_path, data)
    with pytest.raises(ValueError, match=error):
        load_technologies(tmp_path)
