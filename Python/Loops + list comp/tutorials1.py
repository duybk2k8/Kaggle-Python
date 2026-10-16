#LOOPS
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end = ' ')
#planet => variable name use trong hàm
#planets: set of values to loop

#can be used in tuples
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult

print(product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
#print all the uppercase letters
for char in s:
    if char.isupper():
        print(char, end = '')

#RANGE
for i in range(5):
    print("Doing important work. i =", i)

#WHILE
i = 0
while i < 10:
    print(i, end = ' ')
    i += 1

#LIST COMPREHENSIONS
squares = [n**2 for n in range(10)]
print(squares)

#or

squares = []
for n in range(10):
    squares.append(n**2)
#print(squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

loud_short_planets = [planet.upper() + '!' 
                      for planet in planets 
                      if len(planet) < 6]
print(loud_short_planets)

print([32 for planet in planets])