from pathlib import Path

from costs import load_technologies

DATA = Path(__file__).parents[1] / "data" / "technologies"


def test_all_technologies_load() -> None:
    assert load_technologies(DATA)
