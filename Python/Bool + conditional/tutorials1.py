#def can_run_for_president(age):
#    """Can someone of the given age run for president in the US?"""
#    return age >= 35

#print("Can a 19-year-old run for president?", can_run_for_president(19))
#print("Can a 45-year-old run for president?", can_run_for_president(45))

def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age run for president in the US?"""
    return (age >= 35) and is_natural_born_citizen

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

print(False and True or True)
#True and True => True
#False and False => False
#True and False => False (Cả 2 cần True mới dc)
#True or False => True (chỉ cần 1 trong 2 cái True là đc)
#True or True => True
#False or False => False

have_umbrella = True
rain_level = 3
have_hood = False
is_workday = True
prepared_for_weather = (
    have_umbrella
    or ((rain_level < 5) and have_hood)
    or (not(rain_level >0 and is_workday))
)