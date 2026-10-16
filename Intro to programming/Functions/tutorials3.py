num_hours = int(input("How many hours do you work? "))
hourly_wage = int(input("Your hourly wage? "))
tax_bracket = float(input("The taxt bracket? "))

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    #pre-tax pay
    pay_pretax = num_hours * hourly_wage
    #after-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax

print("Your wage is", get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket)) 