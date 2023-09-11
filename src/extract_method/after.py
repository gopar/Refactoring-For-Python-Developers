from typing import Final

# Extract Method

def calculate_total_price(cost: float) -> float:
    total_price = cost + calculate_tax(cost)
    return total_price

def calculate_tax(cost: float) -> float:
    TAX_RATE: Final = 0.08  # 8% tax
    return cost * TAX_RATE
