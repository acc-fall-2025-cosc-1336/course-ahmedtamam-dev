# Named constant for tax rate
TAX_RATE = 0.0675  # 6.75%

def get_sales_tax_amount(meal_amount):
    """
    Calculate sales tax based on the meal amount.
    """
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount, tip_rate):
    """
    Calculate tip amount based on the meal amount and tip rate.
    """
    return meal_amount * tip_rate

def get_total_bill(meal_amount, sales_tax, tip_amount):
    """
    Calculate the total bill amount.
    """
    return meal_amount + sales_tax + tip_amount 