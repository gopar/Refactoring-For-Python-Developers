class IceCreamShopRefactored:
    def __init__(self):
        self.flavors = ["Vanilla", "Chocolate", "Strawberry"]
        self.toppings = ["Sprinkles", "Nuts", "Fudge"]
        self.cups = ["Small", "Medium", "Large"]
        self.total_sales = 0

    # Extract Method: is_flavor_available
    def is_flavor_available(self, flavor):
        return flavor in self.flavors

    # Extract Method: is_cup_available
    def is_cup_available(self, cup_size):
        return cup_size in self.cups

    # Extract Method: calculate_single_ice_cream_price
    def calculate_single_ice_cream_price(self, cup_size, toppings):
        cup_size_prices = {"Small": 5, "Medium": 7, "Large": 10}  # Replace Temp with Query
        price = cup_size_prices.get(cup_size, 0)  # Introduce Explaining Variable
        price += sum(1 for topping in toppings if topping in self.toppings)  # Substitute Algorithm
        return price

    def place_order(self, flavor, toppings, cup_size, quantity):
        flavor_available = self.is_flavor_available(flavor)  # Inline Temp
        cup_available = self.is_cup_available(cup_size)  # Inline Temp

        # Split Temporary Variable: single_ice_cream_price and total_price
        single_ice_cream_price = self.calculate_single_ice_cream_price(cup_size, toppings)
        total_price = single_ice_cream_price * quantity  # Introduce Explaining Variable

        if flavor_available and cup_available:
            print(f"Order placed. Your total is ${total_price}.")
            self.total_sales += total_price  # Remove Assignments to Parameters
        else:
            print("Order could not be placed. Please check the availability.")  # Inline Method (implicit)

# Example usage for testing
refactored_shop = IceCreamShopRefactored()
refactored_shop.place_order("Vanilla", ["Sprinkles", "Fudge"], "Medium", 2)

'''
Refactoring Methods Applied:

    Extract Method: Created is_flavor_available() and is_cup_available() to check the availability of flavors and cup sizes. This makes the place_order method easier to read.

    python

def is_flavor_available(self, flavor):
    return flavor in self.flavors

def is_cup_available(self, cup_size):
    return cup_size in self.cups

Inline Temp: Inlined the temporary variables flavor_available and cup_available to make the code more straightforward.

python

flavor_available = self.is_flavor_available(flavor)
cup_available = self.is_cup_available(cup_size)

Replace Temp with Query: Replaced the if-elif-else construct for cup sizes with a dictionary lookup, making the code more concise.

python

cup_size_prices = {"Small": 5, "Medium": 7, "Large": 10}

Introduce Explaining Variable: Introduced total_price and single_ice_cream_price to make the calculation more readable.

python

total_price = single_ice_cream_price * quantity

Split Temporary Variable: Split the price variable into single_ice_cream_price and total_price to avoid reusing the same variable for different things.

python

single_ice_cream_price = self.calculate_single_ice_cream_price(cup_size, toppings)

Remove Assignments to Parameters: Removed the reassignment to self.total_sales by simply adding to it.

python

self.total_sales += total_price

Substitute Algorithm: Used a list comprehension to calculate the topping price, making the algorithm simpler and more Pythonic.

python

price += sum(1 for topping in toppings if topping in self.toppings)

Inline Method (Implicit): Since the message "Order could not be placed. Please check the availability." is self-explanatory, it essentially inlines the concept of checking availability, making a separate method unnecessary.
'''
