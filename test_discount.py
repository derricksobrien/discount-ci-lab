from discount import calculate_discounted_price
import pytest

def test_premium_discount():
    assert calculate_discounted_price(100, "premium") == 80.00

def test_negative_price_raises():
    with pytest.raises(ValueError):
        calculate_discounted_price(-10, "standard")
