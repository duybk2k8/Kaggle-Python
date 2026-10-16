#STRING SYNTAX
x = 'Pluto'
y = "Pluto"
print(x == y) # có thể viết bằng cả "" ''
print('My dog is named "Pluto"')

print('Pluto\'s a planet')
# dùng \ để escaping single quote

# \
print('What\'s up?')

# \"
print("That's \"cool\"")

# \\
print("Look, a mountain: /\\")

#\n
print("1\n2 3")

#triple quote syntax => k cần viết \n mà tự xuống dòng nó sẽ tự biết
triplequoted_hello = """hello 
world"""
print(triplequoted_hello)

#print auto add a newline character (\n), except we put another arguement like the end = ...
print("hello")
print("world")
print("hello", end = '')
print("pluto", end='')

#STRINGS ARE SEQUENCES
planet = 'Pluto'
print(planet[0])
print(planet[-3:])
print(len(planet))
#loop
print([char + '! ' for char in planet])
#TUY NHIÊN STRING K THAY ĐỔI VỊ TRÍ GIỐNG LIST DC
