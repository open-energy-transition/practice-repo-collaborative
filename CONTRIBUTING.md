# Contributing

Thank you for contributing! Please follow these rules so that maintainers can review your change quickly.

## 1. Open an issue first

- Search existing issues to avoid duplicates.
- Use one of the issue templates. Every issue needs acceptance criteria.

## 2. Fork and branch

- Fork the repository and clone your fork.
- Never commit to `main`. Create a branch named `{type}/{issue-number}-{short-name}`, for example `fix/12-annuity-formula`.
- Types: `feat`, `fix`, `docs`, `data`, `test`, `chore`.

## 3. Commit

- Sign off every commit: `git commit -s`. This certifies the [Developer Certificate of Origin](https://developercertificate.org/).
- Run the checks locally before you push:

  ```bash
  conda env create -f environment.yaml
  conda activate costs
  pre-commit install
  pre-commit run --all-files
  pytest
  ```

  `pre-commit install` makes the checks run on every `git commit`. With uv instead of conda, prefix the commands with `uv run`.

## 4. Technology data

Each technology is one file `data/technologies/<name>.yaml`. The file name and the `name` key must match and be lowercase.

Required keys:

| key | unit |
|---|---|
| `name` | – |
| `carrier` | – |
| `investment_eur_per_kw` | EUR/kW |
| `fom_percent_per_year` | % of investment per year |
| `lifetime_years` | years (integer) |
| `source` | full reference for the numbers |

Data without a `source` will not be accepted.

## 5. Pull request

- Title: `{type}: short description`, for example `data: add onshore wind`.
- Write `Closes #<issue-number>` in the description.
- CI must be green and one maintainer must approve before merging.
- After review has started, do not force-push. Add new commits instead.
