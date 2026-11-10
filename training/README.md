# Training: Collaborative open source workflows

In this session you contribute to [`costs`](../README.md), a project you don't own. You'll go through the same steps as a real contribution to PyPSA or PowSyBl.

```
issue → fork → branch → commit → pull request → CI → review → merge
```

## Before the session (5 min, saves a lot of time)

- [ ] You are logged in to GitHub
- [ ] git works in a terminal (VS Code is fine): `git --version`
- [ ] git knows who you are:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "12345+you@users.noreply.github.com"
  ```
  Use your private GitHub address from https://github.com/settings/emails, or the email address of your GitHub account.
- [ ] You can push to GitHub from this laptop. If you're not sure, test it in the morning sessions.
- [ ] Optional: fork this repository, clone your fork, and run `conda env create -f environment.yaml`.

No git on your laptop? Exercise 2 has a browser-only path. Everything works with just a GitHub account.

The repository is called `practive-repo-collaborative`, typo included. The Python package inside it is called `costs`.

## Exercises

You work in pairs. Count off 1–10; your number is your task card.

| When | Exercise | Sheet |
|---|---|---|
| 12:07 | Turn your task card into an issue | [exercise-1-issue.md](exercise-1-issue.md) |
| 12:15 | Fork, branch, pull request, CI, review | [exercise-2-fork-pr.md](exercise-2-fork-pr.md) |
| | Your task card | [task-cards.md](task-cards.md) |

## Rules of the game

- Read [CONTRIBUTING.md](../CONTRIBUTING.md). The maintainers expect you to follow it, just like in a real project.
- The trainers act as maintainers. They review, request changes and merge.
- Red CI is part of the exercise. Read the log, fix the problem and push again.
