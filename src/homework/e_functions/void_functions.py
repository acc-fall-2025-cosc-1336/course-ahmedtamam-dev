from value_return_functions import (
    get_gross_pay,
    get_fica_tax,
    get_federal_tax,
)


def display_payroll_check(hours, rate):
    """Display payroll check details."""
    gross = get_gross_pay(hours, rate)
    fica = get_fica_tax(gross)
    federal = get_federal_tax(gross)
    net = gross - (fica + federal)

    print(f"\nGross Pay:      {gross:.2f}")
    print(f"FICA:           {fica:.2f}")
    print(f"Federal Tax:    {federal:.2f}")
    print(f"Net Pay:        {net:.2f}\n")
