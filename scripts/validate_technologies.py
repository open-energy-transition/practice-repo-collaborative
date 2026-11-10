import sys
from pathlib import Path

from costs.technologies import load_technology

for arg in sys.argv[1:]:
    load_technology(Path(arg))
