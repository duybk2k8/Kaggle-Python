num_hours = int(input("Please put the hours of work: "))

def get_pay(x):
    pay_pretax = x * 15
    #Pre-tax pay, based on receving $15/hour

    pay_aftertax = pay_pretax * (1 - .12)
    #After-tax pay, based on being in 12% tax bracket
    return pay_aftertax

print("Your wage is", get_pay(num_hours), "dollars")