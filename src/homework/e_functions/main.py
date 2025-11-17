from value_return import get_gross_pay, get_fica_tax, get_federal_tax

from void_func import display_payroll_check

def main():
    hours_worked = float(input("Enter hours worked: ")) # Prompt user for hours worked
    hourly_rate = float(input("Enter hourly rate: ")) # Prompt user for hourly rate

    gross_pay = get_gross_pay(hours_worked, hourly_rate) # Calculate gross pay
    fica = get_fica_tax(gross_pay) # Calculate FICA tax
    federal_tax = get_federal_tax(gross_pay) # Calculate federal tax

    display_payroll_check(gross_pay, fica, federal_tax, gross_pay - fica - federal_tax) # Display payroll check details

if __name__ == "__main__":
    main()