# Number Utils

A lightweight Python library for parsing number strings. Extract the characteristic (integer part) and mantissa (fractional part) from numeric strings—useful for logarithms, scientific notation, and custom number formatting.

## What Does This Project Do?

Number Utils provides two core functions: `characteristic` and `mantissa`. Given a string like `"3.14"`, `characteristic` returns the integer part (3), and `mantissa` returns the fractional part as a numerator/denominator pair (14, 100). This is particularly useful when working with logarithms, where the characteristic and mantissa have distinct mathematical meanings, or when you need precise control over how numbers are decomposed for display or computation.

The library handles edge cases: invalid input returns a success flag of `False`, empty strings and non-numeric input are rejected, and infinity/NaN are treated as invalid. All functions are pure and have no side effects.

## Why Is This Project Useful?

Parsing numbers from strings is common, but extracting the integer and fractional parts as separate, validated components is less straightforward. Many applications—scientific calculators, educational tools, data processing pipelines—need this decomposition. Rather than reimplementing the logic each time, Number Utils offers a small, well-tested, dependency-free module that does one thing well.

It is useful for students learning about number representation, developers building calculators or formatters, and anyone who needs to work with the structure of decimal numbers in string form.

## How Do I Get Started?

### Installation

Clone the repository and use the module directly (no package manager required):

```bash
git clone https://github.com/NAU-OSS/number-utils.git
cd number-utils
```

### Basic Usage

```python
from number_utils import characteristic, mantissa

# Extract the integer part
ok, char = characteristic("3.14")
print(char)  # 3

# Extract the fractional part as numerator/denominator
ok, num, denom = mantissa("3.14")
print(num, denom)  # 14, 100

# Handle invalid input
ok, char = characteristic("not a number")
print(ok)  # False
```

### Running Tests

```bash
python -m unittest discover -s tests -v
```

Or with pytest:

```bash
pip install pytest
pytest tests/ -v
```

## Where Can I Get More Help?

- **Contributing:** See [CONTRIBUTING.md](CONTRIBUTING.md) for how to report bugs, suggest features, and submit changes.
- **Code of Conduct:** We expect all participants to follow our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- **Contributors:** See [CONTRIBUTORS.md](CONTRIBUTORS.md) for those who have contributed to this project.
- **Issues:** Open a [GitHub Issue](https://github.com/NAU-OSS/number-utils/issues) for bugs or feature requests.

## Project Goals and Vision

This project aims to be a minimal, reliable utility for number string parsing. We welcome contributions that improve documentation, add tests, or extend functionality while keeping the API simple and the codebase small.

## License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.
