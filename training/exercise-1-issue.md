# Exercise 1 · Turn a task card into an issue (8 min, in pairs)

Your pair has a task card. A colleague asked for this change, but the maintainers of `costs` don't know you. Write an issue they can act on without asking you anything.

## Steps

1. **Search first (1 min).** Open the practice repository → *Issues*. Search for your technology, including closed issues. Also look at `data/technologies/`. Does it already exist?
2. **Pick the template (1 min).** *New issue* → choose the template that fits. Bug or feature?
3. **Write it (5 min).**
   - Title with a type prefix, for example `data: add onshore wind`.
   - *Why is this needed?* One or two sentences.
   - *What needs to be done?* Be concrete: which file, which values.
   - *Acceptance criteria:* a checklist that says when the issue is done.
4. **Submit and note the issue number.** You need it for the branch name and the pull request.

## Checklist: would a stranger understand it?

- [ ] The title alone says what the issue is about
- [ ] Someone who never saw your task card could do the work
- [ ] The acceptance criteria can be checked with yes or no
- [ ] You searched for duplicates first

## Example

> **data: add onshore wind**
>
> **Why is this needed?**
> Models built with `costs` can't use onshore wind, one of the main technologies in European scenarios.
>
> **What needs to be done?**
> Add `data/technologies/onwind.yaml` with investment 1100 EUR/kW, FOM 1.2 %/a, lifetime 30 a, carrier `wind`.
>
> **Acceptance criteria**
> - [ ] `data/technologies/onwind.yaml` exists and passes the checks
> - [ ] Values and source are documented in the file
