# HÀM DEFINE
def least_difference(a,b,c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4"""
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return min(diff1, diff2, diff3)
# """""" => dùng để gán khái niệm vào hàm đã đặt
print(least_difference(1, 10, 100), least_difference(1, 10, 10), least_difference(5, 6, 7))
help(least_difference)

# 2 khái niệm
# return: các bài về tính toán => cần return
# k return: => side effect => function "hành động" => chúng sẽ làm việc j đó (putting some text on the screen, writing to a file, or modifying an input)
# ví dụ side effect
def add_item(lst):
    lst.append(10)
    # mình k đặt hàm j cả k tính toán j thì k cần return

a = [1, 2, 10]
add_item(a)
print(a)
# >>> [1,2,10] => nó vẫn thêm 10
# nếu hàm cộng như least_difference thì sẽ trả về >>> "NONE" :
def least_difference(a,b,c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
print(least_difference(1, 10, 100), least_difference(1, 10, 10), least_difference(5, 6, 7))

mystery = print()
print(mystery)