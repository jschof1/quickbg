# Contributing to QuickBG

Thank you for your interest in contributing to QuickBG! This document will help you get started.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful and inclusive.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check the [issue tracker](https://github.com/jschof1/quickbg/issues) to see if the issue has already been reported.

When creating a bug report, include:

- A quick summary and background
- Steps to reproduce
- What you expected vs what happened
- Notes (possibly including why you think this might be happening)

### Suggesting Features

Feature requests are welcome! Please check the existing issues first, then create a new one with:

- A clear, descriptive title
- A detailed description of the proposed feature
- Why this would be beneficial
- Any potential alternatives you've considered

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Write a clear commit message
7. Push to your fork and submit a pull request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/jschof1/quickbg.git
cd quickbg

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest
```

## Style Guides

### Python Code

- We use [Black](https://github.com/psf/black) for formatting (line length: 100)
- We use [Ruff](https://github.com/astral-sh/ruff) for linting
- Type hints are required where applicable
- Docstrings for all public functions

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

## Recognition

Contributors will be credited in the README and release notes.
