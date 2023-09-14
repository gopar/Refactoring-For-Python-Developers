import pytest
from .before import IceCreamShop

@pytest.fixture
def shop():
    return IceCreamShop()

def test_flavor_availability(shop):
    assert shop.is_flavor_available("Vanilla") == True
    assert shop.is_flavor_available("Mint") == False

def test_cup_availability(shop):
    assert shop.is_cup_available("Small") == True
    assert shop.is_cup_available("Extra Large") == False

def test_single_ice_cream_price(shop):
    assert shop.calculate_single_ice_cream_price("Small", ["Sprinkles"]) == 6
    assert shop.calculate_single_ice_cream_price("Medium", ["Nuts", "Fudge"]) == 9
    assert shop.calculate_single_ice_cream_price("Large", []) == 10

def test_place_order(shop):
    assert shop.place_order("Vanilla", ["Sprinkles"], "Medium", 2) == "Order placed. Your total is $18."
    assert shop.place_order("Mint", ["Sprinkles"], "Medium", 2) == "Order could not be placed. Please check the availability."
    assert shop.total_sales == 18
