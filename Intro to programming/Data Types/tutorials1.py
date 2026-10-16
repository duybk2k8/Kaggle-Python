#float
x = 22/7
round_pi = round(x, 5)
print(round_pi)
print(type(round_pi))

#1.0 is a float
y_float = 1.
print(y_float)
print(type(y_float))

#int
y = 14
print(y)
print(type(y))

#boolean
z_one = True
print(z_one)
print(type(z_one))

z_two = False
print(z_two)
print(type(z_two))

z_three = (1<2)
print(z_three)
print(type(z_three))

z_four = (5 < 3)
print(z_four)
print(type(z_four))

# "not" False => True
z_five = not z_four
print(z_five)
print(type(z_five))

#strings
w = "Hello, Python!"
print(w)
print(type(w))
print(len(w))

shortest_string = ""
print(type(shortest_string))
print(len(shortest_string))

my_number = "1.12321"
print(my_number)
print(type(my_number))
also_my_number = float(my_number)
print(also_my_number)
print(type(also_my_number))

#addstring
new_string = "abc" + "def"
print(new_string)
print(type(new_string))

#multiply string
newest_string = "abc" * 3
print(newest_string)
print(type(newest_string))

#if float => int ==> negative => round up, positive => round down

print(3 * True)
print(-3.1 * False)
print(type("abc" * False))
print(len("abc" * False))
# int * True => same number 
# int * False => 0
# string * True => same
# string * False => empty string (string with length zero)

#cộng boolean
print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)