#LIST METHODS
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets.append("Pluto")

# "append" is a method carried around by ALL objects, not just "planets" list
# => help(list.append) BUT NOT help(append) ===> append is a method stick with list, cannot stand alone like len or max

#why cell above have no output? => bcs it doesnt have a return
#method chỉ đổi internal, k xuất ra ngoài

#2 loại method
#1. method đổi luôn: như hàm append => list bị thay đổi
#2. method tạo dữ liệu mới: k đụng vào list gốc, chỉ tạo list mới (Ví dụ hàm sorted)
help(planets.append)
print(planets)

#pop removes and returns the last element
print(planets.pop())
print(planets)

#searching lists => index
print(planets.index('Earth')) # => print the location of the word

#check 1 giá trị có trong list k
print("Earth" in planets)

#ra hàm + số 3 ở cuối => add này là function k làm đổi list, có giá trị tương đương append
print(planets.__add__(["3"]))