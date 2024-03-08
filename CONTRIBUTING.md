# FLPQ_Solver project contributing guide

Thank you very much if you have decided to contribute to our project. We follow very simple and clear open-source
research community accepted guidelines for contributing. The guideline instructions divided into sections depending on
the part of the project you want to contribute.

## Rules for adding commits

Create a new branch, if you want to add something new.
Recommended naming branch is `<type>/<name of stuff>`.

Commits are added according to conventional commits. Those
`<type>(<scope>): <body>`.

The `<type>` field must take one of these values:

* `feat` to add new functionality
* `fix` to fix a bug in the project
* `refactor` for code refactoring, such as renaming a variable
* `test` to add tests, refactor them
* `struct` for changes related to a change in the structure of the project (BUT NOT CODE), for example, changing
  folder locations
* `ci` for various ci/cd tasks
* `docs` for changes in documentation

The `<body>` field contains the gist of the changes in the present imperative in English without the dot in
at the end, the first word is a verb with a small letter.
Examples:

* Good: "feat: add module for future BST implementations"
* Bad: "Added module for future BST implementations."

## Source code developers guide (1)

1. Fork this repository using your GitHub account.
2. Install `git` and clone your forked copy of the `repo`.
3. Build project following build instructions in [README.md](./README.md) file, make sure everything is ok.
4. Run unit-tests following instructions in [README.md](./README.md) file, make sure all tests passing.
5. Implement new feature or fix existing one in the source code.
6. Commit your changes.
7. Open a pull-request following repository template rules.
8. Wait for review from developers of the project.
9. Fix major and minor issues if presented.
10. Get your work merged into `main`!

## Documentation improvements guide (2)

1. Fork this repository using your GitHub account.
2. Install `git` and clone your forked copy of the `repo`.
3. Edit code documentation in source files and/or in [docs](./docs) folder files.
4. Commit your changes.
5. Open a pull-request following repository template rules.
6. Wait for review from developers of the project.
7. Fix major and minor issues if presented.
8. Get your work merged into `main`!

## Useful links

If you want to fix something, ask a question, add new functionality or feature, have a look at our templates.

- **Issue templates**:
  [https://github.com/SparseLinearAlgebra/spla/tree/main/.github/ISSUE_TEMPLATE](https://github.com/SparseLinearAlgebra/spla/tree/main/.github/ISSUE_TEMPLATE)
- **Pull-request templates**:
  [https://github.com/SparseLinearAlgebra/spla/tree/main/.github/PULL_REQUEST_TEMPLATE](https://github.com/SparseLinearAlgebra/spla/tree/main/.github/PULL_REQUEST_TEMPLATE)

## Rules for collaborators

### Basic Tips

1. Don't use merge, only rebase (to keep a linear commit history)
2. Do not change other people's branches unless absolutely necessary
3. Recheck your commit history before creating a pull request
4. **Check you're on the right branch**, never commit directly in main

### Rules for pull requests

**Forbidden** to merge your pull request into the branch yourself.

If you click on the green button, then **make sure** that it says `REBASE AND MERGE`

The review takes place in the form of comments to pull requests, discussions in the team chat and personal
communication.
