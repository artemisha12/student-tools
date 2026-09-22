def test_valid_number():
    assert is_valid_number("10") is True
    assert is_valid_number("3.14") is True


def test_invalid_number():
    assert is_valid_number("abc") is False
def test_empty_input():
    assert validate_input("") is False