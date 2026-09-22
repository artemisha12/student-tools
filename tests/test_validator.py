from src.validator import is_valid_number


def test_valid_number():
    assert is_valid_number("10") is True
    assert is_valid_number("3.14") is True


def test_invalid_number():
    assert is_valid_number("abc") is False


def test_empty_input():
    assert is_valid_number("") is False


def test_incorrect_format():
    assert is_valid_number("1,5") is False
    assert is_valid_number("12abc") is False
    assert is_valid_number("   ") is False