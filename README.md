# costs

A tiny library that computes annualised investment costs for energy technologies.
It is used to practise the open source contribution workflow: issue, fork, branch, pull request, CI, review, merge.

```bash
conda env create -f environment.yaml
conda activate costs
pytest
```

With uv instead: `uv sync && uv run pytest`.

Technology data lives in `data/technologies/`, one YAML file per technology.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before you open a pull request.
