import pytest
from .after import CarRentalComplex


@pytest.fixture
def rental():
    return CarRentalComplex()


def test_complex_rent_and_return_car(rental):
    rental.rent_car("Sedan", "customer_1")
    available_cars = [car._type for car in rental.inventory.available_cars]
    assert "Sedan" not in available_cars
    assert "customer_1" in rental.customer_data.data

    rental.return_car("customer_1")
    available_cars = [car._type for car in rental.inventory.available_cars]
    assert "Sedan" in available_cars
    assert "customer_1" not in rental.customer_data.data
