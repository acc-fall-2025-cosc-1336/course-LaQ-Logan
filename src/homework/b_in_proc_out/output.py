def multiply_numbers(num1, num2):
    return num1 * num2

tax_rate = 0.065

# How much sales tax based on cost of the meal and tax rate which is 6.5%
def get_sales_tax_amount(meal_amount):
    return meal_amount * tax_rate

# How much tip based on cost of the meal and tip rate which is provided by the user
def get_tip_amount(meal_amount, tip_rate):
    return meal_amount * tip_rate

# Total cost of the meal that is the sum of the meal amount, tip amount, and tax amount
def get_total_cost(meal_amount, tip_amount, tax_amount):
    return meal_amount + tip_amount + tax_amount