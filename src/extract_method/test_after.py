import pytest
from .before import calculate_total_price, calculate_tax

@pytest.mark.parametrize("cost, total_price", [
    (10, 10.80),
    (2, 2.16),
    (1, 1.08),
    (0, 0),
])
def test_calculate_total_price(cost, total_price):
    assert total_price == calculate_total_price(cost)


@pytest.mark.parametrize("cost, total_tax", [
    (10, .80),
    (2, .16),
    (1, .08),
    (0, 0),
])
def test_calculate_tax(cost, total_tax):
    assert total_tax == calculate_tax(cost)
