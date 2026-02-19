# Contributing to Number Utils

First off, thank you for considering contributing to Number Utils. It is people like you that make this project useful for others. Every contribution—whether it is a bug report, a documentation fix, or new code—is meaningful.

## How to Report Bugs

If you find a bug, please open an [issue](https://github.com/NAU-OSS/number-utils/issues) with:

- A clear, descriptive title
- Steps to reproduce the problem
- The behavior you expected vs. what actually happened
- Your Python version and operating system (if relevant)

If you can, include a minimal code snippet that demonstrates the bug. This helps us reproduce and fix the issue quickly.

## How to Suggest a New Feature

We welcome feature ideas. Open an [issue](https://github.com/NAU-OSS/number-utils/issues) with the `enhancement` label and describe:

- What problem the feature would solve
- How you imagine it would work
- Any alternatives you have considered

We may not implement every suggestion, but we will read and respond to all of them.

## How to Set Up Your Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NAU-OSS/number-utils.git
   cd number-utils
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Run the tests:**
   ```bash
   python -m unittest discover -s tests -v
   ```

   Or with pytest:
   ```bash
   pip install pytest
   pytest tests/ -v
   ```

## Technical Requirements for Contributions

- **Tests must pass.** Before submitting a pull request, run the test suite and ensure all tests pass.
- **Code style.** Use clear, descriptive variable and function names. Follow PEP 8 where practical.
- **Documentation.** If you add or change behavior, update docstrings and the README as needed.

## Types of Contributions We Welcome

- **Bug fixes** – Fix incorrect behavior or edge cases
- **Documentation** – Improve README, docstrings, or add examples
- **Tests** – Add or improve test coverage
- **Code** – Implement new features or refactor existing code (please open an issue first to discuss)

## How to Get in Touch

- Open an [issue](https://github.com/NAU-OSS/number-utils/issues) for questions, bugs, or feature requests
- For sensitive matters (e.g., code of conduct violations), see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for reporting options

Thank you for participating.
