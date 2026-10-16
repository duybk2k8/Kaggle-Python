numbers = {'one':1, 'two':2, 'three':3}
#'one', 'two', 'three' là keys, 1,2,3 => corresponding value
print(numbers['one']) #=> dùng keys để lấy ra giá trị

#có thể gán thêm vào dics, có thể đổi giá trị
numbers['eleven'] = 11
print(numbers)

numbers['one'] = 'Pluto'
print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)
print('Saturn' in planet_to_initial)

#loop in dics
for k in numbers:
    print("{} = {}". format(k, numbers[k]))

#dics key + dics value
print(' '. join(sorted(planet_to_initial.values())))
#hàm .values là để lấy giá trị từ key 
#ví dụ 'one'.value => 1
print(numbers.values()) #=> tạo ra 1 list có hết value

#items => lấy cả cặp (key, value) => gọi là item
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"". format(planet.rjust(10), initial))
#rjust(10) nghĩa là nếu tên hành tinh <10 ký tự => nó sẽ thêm khoảng trắng bên trái cho đủ 10 kí tự
