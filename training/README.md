# Training: Collaborative open source workflows

In this session you contribute to [`costs`](../README.md), a project you don't own. You'll go through the same steps as a real contribution to PyPSA or PowSyBl.

```
issue → fork → branch → commit → pull request → CI → review → merge
```

## Before the session

- [ ] You are logged in to GitHub
- [ ] git works in a terminal (VS Code is fine): `git --version`
- [ ] Optional, saves time: fork this repository, clone your fork and run `conda env create -f environment.yaml`

No git on your laptop? Exercise 2 describes a Codespaces option and a browser-only option.

## Exercises

You work in pairs. Count off 1–10; your number is your task card.

| When | Exercise | Sheet |
|---|---|---|
| 12:07 | Turn your task card into an issue | [exercise-1-issue.md](exercise-1-issue.md) |
| 12:15 | Fork, branch, pull request, CI, review | [exercise-2-fork-pr.md](exercise-2-fork-pr.md) |
| | Your task | [task-cards.md](task-cards.md) |

## Rules of the game

- Read [CONTRIBUTING.md](../CONTRIBUTING.md). The maintainers expect you to follow it, just like in a real project.
- The trainers act as maintainers. They review, request changes and merge.
- Red CI is part of the exercise. Read the log, fix the problem and push again.
