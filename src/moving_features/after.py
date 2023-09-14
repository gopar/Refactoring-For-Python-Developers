class Inventory:
    def __init__(self) -> None:
        self.flavors = ["Vanilla", "Chocolate", "Strawberry"]
        self.toppings = ["Sprinkles", "Nuts", "Fudge"]
        self.cups = ["Small", "Medium", "Large"]

    def add_flavor(self, flavor: str) -> None:
        self.flavors.append(flavor)

    def remove_flavor(self, flavor: str) -> None:
        self.flavors.remove(flavor)


class Financial:
    def __init__(self) -> None:
        self.tax_rate = 0.1

    def calculate_tax(self, amount: float) -> float:
        return amount * self.tax_rate


class IceCreamShop:
    def __init__(self):
        self.inventory = Inventory()
        self.financial = Financial()
        self.total_sales = 0

    def place_order(self, flavor, toppings, cup_size, quantity):
        flavor_available = flavor in self.inventory.flavors
        cup_available = cup_size in self.inventory.cups
        cup_size_prices = {"Small": 5, "Medium": 7, "Large": 10}
        single_ice_cream_price = cup_size_prices.get(cup_size, 0)
        single_ice_cream_price += sum(1 for topping in toppings if topping in self.inventory.toppings)
        price = single_ice_cream_price * quantity
        tax = self.financial.calculate_tax(price)
        total_price = price + tax

        if flavor_available and cup_available:
            self.total_sales += total_price
            return f"Order placed. Your total is ${total_price}. Tax is ${tax}."
        else:
            return "Order could not be placed. Please check the availability."
