# Exercise 2 · Fork, branch, pull request, CI (20 min, in pairs)

One person types, the other reads the instructions and checks. Swap roles after the push.

Replace `<you>` with your GitHub user name, `<N>` with your issue number and `<tech>` with your technology (for example `onwind`).

## 1. Fork and clone

On GitHub: practice repository → **Fork** → *Create fork*.

```bash
git clone https://github.com/<you>/practive-repo-collaborative.git
cd practive-repo-collaborative
git remote add upstream https://github.com/open-energy-transition/practive-repo-collaborative.git
git remote -v
```

You should see `origin` (your fork) and `upstream` (the original).

## 2. Branch

```bash
git switch -c data/<N>-<tech>
```

## 3. Make the change

Read `CONTRIBUTING.md`. Then create `data/technologies/<tech>.yaml`, using `ccgt.yaml` as a model.

## 4. Commit with sign-off and push

```bash
git add data/technologies/<tech>.yaml
git commit -s -m "data: add <tech>"
git log -1
git push -u origin data/<N>-<tech>
```

`git log -1` must show a `Signed-off-by:` line.

## 5. Open the pull request

GitHub shows a banner *Compare & pull request*. Check:

- base repository: **upstream** `main`, head: **your fork**, your branch
- title: `data: add <tech>`
- description: `Closes #<N>`, then fill in the checklist

## 6. Watch CI

Open the **Checks** tab. If something is red:

1. Click the failing job and read the log. What does it complain about?
2. Fix it locally. To run the same checks on your machine:

   ```bash
   conda env create -f environment.yaml   # only once
   conda activate costs
   pre-commit run --all-files
   ```

3. Commit with `-s` and push again. The PR updates automatically. Don't open a new PR.

## 7. Respond to review

When a maintainer requests changes, add a **new commit** and push. Don't force-push after review has started: it hides what changed since the last review.

## Done when

- [ ] CI is green
- [ ] A maintainer approved
- [ ] After the merge, your issue closed automatically

## No git on your machine?

### Option A · Codespaces (full terminal in the browser)

1. In **your fork**: *Code* → *Codespaces* → *Create codespace on main*.
2. Wait until the terminal shows a prompt. The package, pytest and pre-commit are already installed, so you can skip `conda`.
3. Follow steps 2–7 above in the Codespaces terminal. `upstream` is not set; add it as in step 1 if you need it.

### Option B · Browser only (no terminal at all)

1. In **your fork**: switch the branch selector to *main* → type `data/<N>-<tech>` → *Create branch*.
2. Open `data/technologies/` → *Add file* → *Create new file* → name it `<tech>.yaml`, paste the content.
3. *Commit changes*: message `data: add <tech>`, tick **Sign off**, commit to your branch.
4. GitHub offers *Compare & pull request*. Continue with step 5 above.
5. To fix a red check, open the file on your branch → pencil icon → edit → commit with sign-off again.

With option B you can't run pre-commit locally. CI runs the checks for you instead.

## Stuck?

| Problem | Fix |
|---|---|
| `git push` asks for a password | Use a personal access token or SSH. See the setup from the morning session. |
| Forgot `-s` | `git commit --amend -s --no-edit`, then `git push --force-with-lease`. This is fine *before* review starts. |
| PR targets your own fork | Edit the PR: change the base repository to upstream. |
| `pre-commit: command not found` | Run `conda activate costs` first |
| Creating the conda environment fails or is slow | Push anyway and let CI run the checks for you |
