# Exercise 2 · Fork, branch, pull request, CI (until 12:40, in pairs)

**One fork, one laptop per pair.** One person types, the other reads the instructions and checks. Swap at step 3.

You need:

- `<N>`: your issue number from exercise 1, for example `14`
- `<tech>`: the file name on your task card, for example `onwind`
- `<you>`: the GitHub user name of the person whose laptop you use

The repository is called `practive-repo-collaborative`, typo included. The Python package inside it is called `costs`.

## Choose your path

| | Path T · Terminal | Path B · Browser only |
|---|---|---|
| You need | git + VS Code (or Codespaces) | Only a web browser |
| You practise | The real workflow, including local checks | The same workflow, but CI does all the checks |
| Choose it if | git works on your laptop | git doesn't work, or you want it simple |

Both paths have the same five steps and end with the same pull request.

```
1 Fork → 2 Branch + add your file → 3 Pull request → 4 CI → 5 Review
```

## 1. Fork (both paths)

Open https://github.com/open-energy-transition/practive-repo-collaborative → **Fork** (top right) → *Create fork*.
You now have your own copy at `github.com/<you>/practive-repo-collaborative`.

## 2. Branch and add your file

### Path T · Terminal

**Using Codespaces?** In your fork: *Code* → *Codespaces* → *Create codespace on main*. It is already cloned and set up, so skip 2a and the `conda` lines in 2d.

**a. Clone your fork and add upstream.** Already cloned before the session? Just run the last two lines.

```bash
git clone https://github.com/<you>/practive-repo-collaborative.git
cd practive-repo-collaborative
git remote add upstream https://github.com/open-energy-transition/practive-repo-collaborative.git
git remote -v
```

You should see `origin` (your fork) and `upstream` (the original).

**b. Create a branch.**

```bash
git switch -c data/<N>-<tech>
```

**c. Create the file.** Read `CONTRIBUTING.md`, section 4. Copy `data/technologies/ccgt.yaml` to `data/technologies/<tech>.yaml` and change the values. Keep the keys exactly as they are.

**d. Check locally (optional).** pre-commit only sees files git knows about, so `git add` first:

```bash
git add data/technologies/<tech>.yaml
conda env create -f environment.yaml   # only once, takes a few minutes
conda activate costs
pre-commit run --all-files
```

Everything should say `Passed`. If not, read the message, fix the file, `git add` it again and rerun.

**e. Commit with sign-off and push.**

```bash
git add data/technologies/<tech>.yaml
git commit -s -m "data: add <tech>"
git log -1
git push -u origin data/<N>-<tech>
```

`git log -1` must show a line `Signed-off-by: Your Name <email>`.

### Path B · Browser only

**a. Create a branch in your fork.** In **your fork**: click the branch button (it shows `main`) → type `data/<N>-<tech>` → *Create branch data/<N>-<tech> from main*.

**b. Add the file.**
1. Check that your new branch is selected.
2. Open the folder `data/technologies/` → **Add file** → *Create new file*.
3. Name: `<tech>.yaml`.
4. Content: open `ccgt.yaml` in another tab, copy it, and change the values. Keep the keys exactly as they are. Read `CONTRIBUTING.md`, section 4.

**c. Commit with sign-off.** Click **Commit changes…**
- Commit message: `data: add <tech>`
- *Extended description*: `Signed-off-by: Your Name <your-email>`
  You can use your private GitHub address from https://github.com/settings/emails, which looks like `12345+you@users.noreply.github.com`.
- Choose *Commit directly to the `data/<N>-<tech>` branch* → **Commit changes**.

## 3. Open the pull request (both paths)

Swap who types now.

GitHub shows a yellow banner **Compare & pull request**. If it's gone: your fork → *Pull requests* → *New pull request*.

Check before you click *Create pull request*:

- [ ] base repository: `open-energy-transition/practive-repo-collaborative`, base: `main`
- [ ] head repository: `<you>/practive-repo-collaborative`, compare: `data/<N>-<tech>`
- [ ] title: `data: add <tech>`
- [ ] description starts with `Closes #<N>`
- [ ] checklist filled in. **Path B:** leave the two "passes locally" boxes unticked and write "Browser path, checked by CI only".

## 4. Watch CI (both paths)

Scroll down in your PR to the checks. They take about a minute.
**Nothing happens after 1 minute, or it says "awaiting approval"?** Raise your hand. A trainer has to approve CI runs for first-time contributors.

If something is red:

1. Click **Details** next to the failing check. Scroll to the end of the log. What does it complain about? See the hints below.
2. Fix it:
   - **Path T:** edit the file, `git add` it, run `pre-commit run --all-files`, then `git commit -s -m "data: fix <tech>"` and `git push`.
   - **Path B:** in your fork, switch to your branch, open the file → pencil icon → edit → *Commit changes* with the `Signed-off-by:` line as in 2c.
3. The PR updates automatically. **Don't open a new PR.**

## 5. Respond to review (both paths)

The trainers act as maintainers and review the PRs in batches. If they request changes, fix them with a **new commit**, as in step 4.
Don't force-push once review has started: the reviewer can no longer see what changed since their last look.

## Done when

- [ ] Your PR is open against `open-energy-transition/...` and mentions `Closes #<N>`
- [ ] CI is green
- [ ] You answered any review comments

The trainers merge a few PRs live and the rest after the session. Your issue then closes automatically.

**Finished early?**
- Review another pair's PR: open it → *Files changed* → click a line → leave a comment, for example "Could you add the year to the source?"
- Or take spare card 11 or 12 and do the whole cycle again on your own.

## Afterwards: keep your fork in sync

Your fork doesn't update itself. Before your next contribution:

- **Browser:** your fork → **Sync fork** → *Update branch*.
- **Terminal:**

  ```bash
  git switch main
  git fetch upstream
  git merge --ff-only upstream/main
  git push origin main
  ```

Never commit to `main` in your fork; always start a new branch from an up-to-date `main`. `--ff-only` stops with an error if you did commit on `main`, so you can't make a mess by accident.

---

## Hints

<details>
<summary>What does a technology file look like?</summary>

Look at `data/technologies/ccgt.yaml`. Your file has the same six keys. Only the values change, and `name` must equal the file name without `.yaml`.

</details>

<details>
<summary>CI says <code>missing keys ['source']</code></summary>

`CONTRIBUTING.md` requires a `source` for every technology. Your task card says where the numbers come from. Put that in a `source:` line.

</details>

<details>
<summary>CI says <code>unknown keys [...]</code></summary>

You used a key that doesn't exist, for example `fom` or `cost`. Copy the keys exactly from `ccgt.yaml` and only change the values.

</details>

<details>
<summary>CI says <code>name ... must match file name</code></summary>

`onwind.yaml` needs `name: onwind`: lowercase and identical to the file name.

</details>

<details>
<summary>The <code>sign-off</code> check is red</summary>

One of your commits has no `Signed-off-by:` line.

- **Path T, before review:** `git rebase --signoff upstream/main`, then `git push --force-with-lease`. This adds the line to every commit on your branch. Run `git fetch upstream` first if git doesn't know `upstream/main`.
- **Path B:** close the PR. Create a new branch from `main`, add the file again with the `Signed-off-by:` line, and open a new PR. It takes 2 minutes.

</details>

<details>
<summary><code>trim trailing whitespace</code> or <code>fix end of files</code> failed</summary>

There are spaces at the end of a line, or the file doesn't end with a line break.
**Path T:** pre-commit already fixed the file for you: `git add` it and commit again.
**Path B:** remove the spaces and make sure there is an empty line after the last line.

</details>

<details>
<summary>My PR goes to my own fork, or shows many changes I didn't make</summary>

The base repository can't be changed after the PR is open. Close the PR. Then: your fork → *Pull requests* → *New pull request*, and check that the base repository is `open-energy-transition/practive-repo-collaborative`.

</details>

<details>
<summary>Terminal problems</summary>

| Problem | Fix |
|---|---|
| `git push` asks for a password, or is rejected | Use SSH or a personal access token (see the morning session), or switch to Path B |
| Push rejected with `GH007` (private email) | `git config user.email "12345+you@users.noreply.github.com"` (your address from https://github.com/settings/emails), then `git commit --amend --reset-author -s --no-edit` and push again |
| `error: remote upstream already exists` | Fine. It's already set; continue |
| `pre-commit: command not found` | `conda activate costs` |
| Creating the conda environment is slow or fails | Skip 2d and let CI run the checks |

</details>
