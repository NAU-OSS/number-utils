"""
Number Utils - A lightweight Python library for parsing number strings.

Extracts the characteristic (integer part) and mantissa (fractional part)
from numeric strings, useful for logarithms, scientific notation, and
custom number formatting.
"""
import math


def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.

    Args:
        num_string: A string representation of a number (e.g., "3.14", "-2.5").

    Returns:
        tuple: (bool, int) - (True, characteristic) if valid,
        (False, 0) if invalid
    """
    if not isinstance(num_string, str):
        return (False, 0)
    s = num_string.strip()
    if not s:
        return (False, 0)
    try:
        value = float(s)
        if not math.isfinite(value):
            return (False, 0)
        return (True, int(value))
    except (ValueError, TypeError):
        return (False, 0)


def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.

    Returns the fractional part as a numerator/denominator pair.
    For example, "3.14" returns (True, 14, 100).

    Args:
        num_string: A string representation of a number.

    Returns:
        tuple: (bool, int, int) - (True, numerator, denominator) if valid,
        (False, 0, 0) if invalid
    """
    if not isinstance(num_string, str):
        return (False, 0, 0)
    s = num_string.strip()
    if not s:
        return (False, 0, 0)
    try:
        value = float(s)
        if not math.isfinite(value):
            return (False, 0, 0)
        if "." not in s:
            return (True, 0, 1)
        parts = s.split(".")
        if len(parts) != 2:
            return (False, 0, 0)
        frac = parts[1]
        if not frac:
            return (True, 0, 1)
        numerator = int(frac)
        denominator = 10 ** len(frac)
        return (True, numerator, denominator)
    except (ValueError, TypeError):
        return (False, 0, 0)
