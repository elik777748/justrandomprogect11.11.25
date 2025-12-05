import pytest
from functions import is_valid_email, avg, ua_to_usd


# is_valid_email


def test_valid_email():
    assert is_valid_email("test@example.com") is True

def test_email_starts_with_at():
    assert is_valid_email("@example.com") is False

def test_email_ends_with_at():
    assert is_valid_email("test@") is False

def test_email_starts_with_dot():
    assert is_valid_email(".test@example.com") is False

def test_email_ends_with_dot():
    assert is_valid_email("test@example.") is False

def test_email_without_at():
    assert is_valid_email("testexample.com") is False

def test_empty_email():
    assert is_valid_email("") is False

def test_invalid_domain():
    assert is_valid_email("test@otherdomain.com") is False



# avg

def test_avg_normal_list():
    assert avg([1.0, 2.0, 3.0]) == pytest.approx(2.0)

def test_avg_single_value_raises():
    with pytest.raises(ValueError):
        avg([5.0])

def test_avg_empty_list():
    with pytest.raises(ValueError):
        avg([])

def test_avg_with_negative():
    with pytest.raises(ValueError):
        avg([-1.0, 2.0, 3.0])

def test_avg_zero_in_list():
    with pytest.raises(ValueError):
        avg([0.0, 2.0, 3.0])



# ua_to_usd

def test_normal_case():
    assert ua_to_usd(5000, 40) == pytest.approx(125.0)

def test_invalid_rate():
    with pytest.raises(ValueError):
        ua_to_usd(1000, 0)

    with pytest.raises(ValueError):
        ua_to_usd(1000, -25)

def test_invalid_amount():
    with pytest.raises(ValueError):
        ua_to_usd(0, 40)

    with pytest.raises(ValueError):
        ua_to_usd(-500, 40)

def test_large_values():
    assert ua_to_usd(1_000_000, 40) == pytest.approx(25000.0)

def test_float_precision():
    result = ua_to_usd(1234.56, 36.78)
    assert result == pytest.approx(33.56, rel=1e-3)
