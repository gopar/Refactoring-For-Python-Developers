from typing import List


class IceCreamShop:
    def __init__(self):
        self.flavors = ["Vanilla", "Chocolate", "Strawberry"]
        self.toppings = ["Sprinkles", "Nuts", "Fudge"]
        self.cups = ["Small", "Medium", "Large"]
        self.total_sales = 0

    def is_flavor_available(self, flavor: str) -> bool:
        return flavor in self.flavors

    def is_cup_available(self, cup_size: str) -> bool:
        return cup_size in self.cups

    def calculate_single_ice_cream_price(
            self,
            cup_size: str,
            toppings: List[str]
    ) -> float:
        cup_size_prices = {'Small': 5, 'Medium': 7, "Large": 10}
        price = cup_size_prices.get(cup_size, 0)
        price_with_toppings = price + sum(1 for topping in toppings if topping
                                          in self.toppings)
        return price_with_toppings

    def place_order(
            self,
            flavor: str,
            toppings: List[str],
            cup_size: str,
            quantity: int
    ) -> str:
        flavor_available = self.is_flavor_available(flavor)
        cup_available = self.is_cup_available(cup_size)
        price = self.calculate_single_ice_cream_price(cup_size, toppings)

        # Calculate the total price
        total_price = price * quantity

        # Check if the order can be placed
        if flavor_available and cup_available:
            self.total_sales += total_price
            return f"Order placed. Your total is ${total_price}."
        else:
            return "Order could not be placed. Please check the availability."


# Example usage
if __name__ == "__main__":
    shop = IceCreamShop()
    print(shop.place_order("Vanilla", ["Sprinkles", "Fudge"], "Medium", 2))
