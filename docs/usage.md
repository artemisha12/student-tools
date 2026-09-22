# Converter Module Usage Guide

The `converter` module provides tools for converting temperature units.

## Functions & Formulas

### 1. `celsius_to_fahrenheit(celsius)`
Converts temperature from Celsius to Fahrenheit.
- **Formula:** $F = C \times \frac{9}{5} + 32$
- **Example:**
  ```python
  from src.converter import celsius_to_fahrenheit

  # Example: Convert 0°C to Fahrenheit
  result = celsius_to_fahrenheit(0)
  print(result)  # Expected Output: 32.0
## Temperature converter

```python
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius

celsius_to_fahrenheit(100)   # 212.0
fahrenheit_to_celsius(32)    # 0.0
```
