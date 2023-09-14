import pytest
from .before import IceCreamShop


@pytest.fixture
def shop():
    return IceCreamShop()


def test_place_order(shop):
    assert shop.place_order("Vanilla", ["Sprinkles"], "Medium", 2) == "Order placed. Your total is $17.6. Tax is $1.6."
    assert shop.total_sales == 17.6


@pytest.mark.parametrize("flavor", [("Coke", "Pepsi")])
def test_removing_and_adding_flavors(shop, flavor):
    shop.inventory.add_flavor(flavor)
    assert flavor in shop.inventory.flavors


@pytest.mark.parametrize("amount, total", [(0, 0), (10, 1), (20, 2)])
def test_calculate_tax(shop, amount, total):
    assert shop.financial.calculate_tax(amount) == total
