import pytest
from .before import IceCreamShop


@pytest.fixture
def shop():
    return IceCreamShop()


def test_place_order(shop):
    assert (
        shop.place_order("Vanilla", ["Sprinkles"], "Medium", 2)
        == "Order placed. Your total is $16."
    )

    assert shop.total_sales == 16
    assert (
        shop.place_order("Mint", ["Sprinkles"], "Medium", 2)
        == "Order could not be placed. Please check the availability."
    )
    assert shop.total_sales == 16


def test_is_flavor_available(shop):
    assert True == shop.is_flavor_available("Vanilla")
    assert False == shop.is_flavor_available("Mint")


def test_cup_availability(shop):
    assert False == shop.is_cup_available("Monster")
    assert True == shop.is_cup_available("Large")


def test_calculate_single_ice_cream_price(shop):
    assert shop.calculate_single_ice_cream_price("Small", []) == 5
    assert shop.calculate_single_ice_cream_price("Large", []) == 10
