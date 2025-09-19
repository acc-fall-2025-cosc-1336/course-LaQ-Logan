from output import multiply_numbers, get_sales_tax_amount, get_tip_amount, get_total_cost

tax_rate = 0.065

def main():
    meal_amount = float(input("Enter the meal amount: "))
    tip_rate = float(input("Enter the tip rate (as a decimal such as 15% = 0.15): "))

    sales_tax = get_sales_tax_amount(meal_amount)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total_cost = get_total_cost(meal_amount, tip_amount, sales_tax)

    print("\n Receipt")
    print(f"Meal Amount: ${meal_amount:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()