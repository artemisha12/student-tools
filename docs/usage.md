# Converter Module Usage Guide

The `converter` module provides tools for converting temperature units.

## Functions

### 1. `celsius_to_fahrenheit(celsius)`
Converts temperature from Celsius to Fahrenheit.

### 2. `fahrenheit_to_celsius(fahrenheit)`
Converts temperature from Fahrenheit to Celsius.

## Example Code

```python
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(0))     # Expected Output: 32.0
print(fahrenheit_to_celsius(212))   # Expected Output: 100.0