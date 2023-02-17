# Contribution Guide

## How to contribute

### Reporting Bugs

Before you create a bug report, please check that an issue reporting the same problem does not already exist.

If you're unable to find an open issue addressing the problem, [open a new one](). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

Before you create an enhancement suggestion, please check that an issue suggesting the same or a similar enhancement does not already exist.

If you're unable to find an open issue addressing the problem, [open a new one](

). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Pull Requests

Pull requests are the best way to propose changes to the codebase . We actively welcome your pull requests:

- Fork the repo and create your branch from `master`.
- If you've added code that should be tested, add tests.
- If you've changed APIs, update the documentation.
- Ensure the test suite passes.
- Make sure your code lints.
- Issue that pull request!

## Conventional Commits

This project uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) to automate the generation of the changelog. Please follow the guidelines when writing commit messages.

## Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

Any line of the commit message cannot be longer 100 characters! This allows the message to be easier to read on GitHub as well as in various git tools.

### Revert

If the commit reverts a previous commit, it should begin with `revert: `, followed by the header of the reverted commit. In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.

## Code of Conduct

This project and everyone participating in it is governed by the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/1/4/code-of-conduct). By participating, you are expected to uphold this code. Please report unacceptable behavior
