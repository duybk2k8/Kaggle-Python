#METHODS
claim = "Pluto is a planet!"
planet = "Pluto"

print(claim.upper())
print(claim.lower()) 

print(claim.index('plan')) #vị trí của p

print(claim.startswith(planet))
print(claim.endswith('planet'))

#split + join
words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-') #chia xong gán biến luôn
print(year)
#join trc đó sẽ có cú pháp và kí tự muốn nó ghép
print('/'.join([month, day, year]))
print(' 👏 '.join([word.upper() for word in words]))

#FORMAT
print(planet + ', we miss you.')
#nếu cộng biến mà k phải string thì phải thêm str()
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

#or
print("{}, you'll always be the {}th planet to me.".format(planet, position))
#format k cần chuyển đổi string trong position

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
print("{} wieighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.". format(
    planet, pluto_mass, pluto_mass / earth_mass, population
))
#.2 là làm tròn đến 2 decimal point, .3% là format theo phần trăm + làm tròn đến 3 chữ số, ":," là là đánh phẩy (ví dụ như 52,350)

s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""". format('planet', 'dwarf planet')
print(s)