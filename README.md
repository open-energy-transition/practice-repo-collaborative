# costs

> **Training participants: start here → [training/](training/README.md)**
> This repository is a practice project for the session *Collaborative open source workflows*. Treat it like a real open source project that you don't own.

`costs` is a tiny Python library that computes the annualised cost of energy technologies (investment plus fixed O&M, spread over the lifetime with a discount rate), similar to what PyPSA models use.

## What's inside

| Path | Content |
|---|---|
| `src/costs/annuity.py` | `annuity()` and `annualised_cost()` |
| `src/costs/technologies.py` | Loads and validates technology data |
| `data/technologies/` | One YAML file per technology, for example `ccgt.yaml` |
| `tests/` | Tests run by CI |

## Quick start

```bash
conda env create -f environment.yaml
conda activate costs
pytest
```

```python
from pathlib import Path
from costs import annualised_cost, load_technologies

for tech in load_technologies(Path("data/technologies")):
    cost = annualised_cost(tech.investment_eur_per_kw, tech.fom_percent_per_year, tech.lifetime_years, 0.07)
    print(f"{tech.name}: {cost:.1f} EUR/kW/a")
```

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before you open an issue or a pull request.

## Licence

[MIT](LICENSE)
