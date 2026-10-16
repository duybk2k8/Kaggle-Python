#bài 1
def greet(name, age=18):
    print("Hello", name, "you are", age, "years old")
greet("An")

#bài 2
def add(a,b):
    return a+b
print(add(2,3))

#bài 3
def is_even(n):
    return n % 2 == 0
print(is_even(5))

#bài 4:
def max_of_three(a,b,c):
    return max(a,b,c)
print(max_of_three(3,5,7))

#bài 5
def smart_greet(name = "Guest", language = "en"):
    if language == "en":
        print("Hello", name)
    elif language == "vi":
        print("Xin chào", name)
    else:
        print("Hi", name)
smart_greet("Thảo", "vi")

#bài 6
def power(base, exponent = 2):
    return base ** exponent
print(power(3))
print(power(2,3))

#bài 7
def introduce(name, age, city = "Unknown"):
    print(f"My name is {name}, I am {age}, from {city}")
#format list, cho biến vào thẳng string
introduce("An", 20)
introduce("Bình", 22, "Hanoi")
introduce(age=19, name="Linh")

