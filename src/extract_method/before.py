# Extract Method

def calculate_total_price(cost):
    tax_rate = 0.08  # 8% tax
    total_price = cost + (cost * tax_rate)
    return total_price
