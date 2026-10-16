#TUPLES => same as list
t = (1, 2, 3)
#t = 1, 2, 3 => equivalent
print(t)

#diff: they cannot be modified => cannot t[0] = 100

#turples are often used for functions that have multiple return values
#as_integer_ratio() => in ra cặp tuple mà có tử, phân số
x = 0.125
print(x.as_integer_ratio())
#or
numerator, denominator = x.as_integer_ratio()
print(numerator/denominator)

#swap variables
a = 1
b = 0
a, b = b, a
print(a, b)