import pytest
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100


def test_float_input():
    assert celsius_to_fahrenheit(36.6) == pytest.approx(97.88)
    
def test_celsius_to_fahrenheit_negative():
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(-10) == 14