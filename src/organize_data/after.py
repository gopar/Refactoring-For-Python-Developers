from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Car:
    _type: str
    price: float
    is_available: bool = True


class CarInventory:
    def __init__(self, available_cars: List[Car]):
        self.available_cars = available_cars

    def rent_car(self, car_type: str) -> Car | None:
        cars = list(filter(lambda car: car._type == car_type, self.available_cars))
        if not cars:
            return None

        car = cars[0]
        self.available_cars.remove(car)
        return car

    def return_car(self, car: Car) -> None:
        self.available_cars.append(car)

    @classmethod
    def from_dict(cls, _dict: Dict[str, float]) -> "CarInventory":
        available_cars = [Car(_type=_type, price=price) for _type, price in _dict.items()]
        return cls(available_cars)


class CustomerData:
    def __init__(self) -> None:
        self.data: Dict[str, Car] = {}

    def add_customer(self, customer_id: str, car: Car) -> None:
        self.data[customer_id] = car

    def remove_customer(self, customer_id: str) -> None:
        del self.data[customer_id]


class CarRentalComplex:
    def __init__(self) -> None:
        self.inventory = CarInventory.from_dict({"Sedan": 50, "SUV": 80, "Truck": 100})
        self.customer_data = CustomerData()

    def rent_car(self, car_type: str, customer_id: str) -> None:
        car = self.inventory.rent_car(car_type)
        if not car:
            return

        self.customer_data.add_customer(customer_id, car)

    def return_car(self, customer_id: str) -> None:
        car = self.customer_data.data[customer_id]
        self.inventory.return_car(car)
        self.customer_data.remove_customer(customer_id)
