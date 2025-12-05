FICA_RATE = 0.0765 # 7.65% FICA rate
FEDERAL_TAX_RATE = 0.08 # 8% federal tax rate

def get_gross_pay(hours_worked, hourly_rate): # Calculate gross pay with and without OT
    if hours_worked > 40:
        overtime_hours = hours_worked - 40 # Calculate overtime hours
        gross_pay = (40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5) # Calculate gross pay with overtime
    else:
        gross_pay = hours_worked * hourly_rate # Calculate gross pay without overtime
    return gross_pay

def get_fica_tax(gross_pay): # Calculate FICA tax
    return gross_pay * FICA_RATE # Calculate FICA tax by multiplying gross pay by FICA rate

def get_federal_tax(gross_pay): # Calculate federal tax
    return gross_pay * FEDERAL_TAX_RATE # Calculate federal tax by multiplying gross pay by federal tax rate
