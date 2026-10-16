#LIST BASIC FUNCTIONS
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # Comma after last element is optional
]

# list có thể mix
my_fav_things = [32, 'raindrops on roses', help]

#print(my_fav_things[2])

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#elements at the end
print(planets[-1])
print(planets[-2])

#slicing
print(planets[0:3])

#bỏ đầu => auto 1
#bỏ đít => auto full
print(planets[:3])
print(planets[3:])
print(planets[1:-1]) #all planets except the first and last
print(planets[-3:]) #all last 3 planets

#length
print(len(planets))

#CHANGING LIST
planets[3] = 'Malacandra' 
print(planets)

#change multiple variables
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

#sorted => alphabetical order
sorted(planets)
print(sorted(planets)) 
#nó chỉ sort ở đấy thôi nhưng list vẫn giữ nguyên phải cho cả sort vào mới dc

#sum => tổng
primes = [2, 3, 5, 7]
print(sum(primes))
print(max(primes))

print(my_fav_things)