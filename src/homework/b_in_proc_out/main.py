import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.homework.b_in_proc_out.output import get_sales_tax_amount, get_tip_amount

def main():
    meal_amount = float(input("Enter the meal amount (e.g., 20.00): "))
    tip_rate = float(input("Enter the tip rate as a decimal (e.g., 0.15 for 15%): "))

    sales_tax = get_sales_tax_amount(meal_amount)
    tip_amount = get_tip_amount(meal_amount, tip_rate)
    total = meal_amount + sales_tax + tip_amount

    print("\n--- Receipt ---")
    print(f"Meal Amount:    ${meal_amount:.2f}")
    print(f"Sales Tax:      ${sales_tax:.2f}")
    print(f"Tip Amount:     ${tip_amount:.2f}")
    print(f"Total:          ${total:.2f}")

if __name__ == "__main__":
    main()
# Named constant for tax rate
TAX_RATE = 0.0675  # 6.75% 