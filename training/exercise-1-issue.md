# Exercise 1 · Turn a task card into an issue (6 min, in pairs)

Your pair has a task card from [task-cards.md](task-cards.md). A colleague asked for this change, but the maintainers of the project don't know you. Write an issue they can act on without asking you anything.

Work in the **main repository**: https://github.com/open-energy-transition/practice-repo-collaborative. You don't have a fork yet; that's exercise 2.

## Steps

1. **Search first.**
   - Open the *Issues* tab and type your technology in the search box. Delete `is:open` from the filter, so closed issues show up too.
   - Also look in the folder `data/technologies/`.
   - **Already exists?** Don't open an issue. Tell a trainer and take spare card 12.
2. **Pick the template.** *New issue* → **Feature or data request**.
3. **Write it (4 min).**
   - Title: replace the prefilled `feat: ` with `data: `, for example `data: add solar PV`.
   - *Why is this needed?* One or two sentences.
   - *What needs to be done?* Be concrete: which file, which values.
   - *Acceptance criteria:* a checklist that says when the issue is done.
4. **Submit and note the issue number** (`#…` after the title). You need it for the branch name and the pull request.

## Checklist: would a stranger understand it?

- [ ] The title alone says what the issue is about
- [ ] Someone who never saw your task card could do the work
- [ ] The acceptance criteria can be checked with yes or no
- [ ] You searched for duplicates first

## Example

This technology is not on any card.

> **data: add lignite power plant**
>
> **Why is this needed?**
> Models built with this library can't represent existing lignite capacity, which matters for coal phase-out scenarios.
>
> **What needs to be done?**
> Add `data/technologies/lignite.yaml`: carrier `lignite`, investment 1900 EUR/kW, fixed O&M 1.6 % per year, lifetime 40 years.
>
> **Acceptance criteria**
> - [ ] `data/technologies/lignite.yaml` exists with the values above
> - [ ] CI is green

## Hints

<details>
<summary>I don't see the templates, only an empty text box</summary>

You are probably in your fork. Go to `open-energy-transition/practice-repo-collaborative` and click *New issue* there.

</details>

<details>
<summary>What's a good acceptance criterion?</summary>

Something a reviewer can check with yes or no: "the file exists", "CI is green", "the values match the card". "It works well" is not checkable.

</details>

<details>
<summary>We finished early</summary>

Read another pair's issue. Could you do the work from their description alone? Leave a friendly comment if something is missing.

</details>
