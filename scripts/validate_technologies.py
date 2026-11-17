import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from costs.technologies import load_technology  # noqa: E402

for arg in sys.argv[1:]:
    load_technology(Path(arg))
