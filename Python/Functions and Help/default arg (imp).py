
#help(print) => hàm print có nhiều chức năng, ví dụ như "sep"
print(1, 2, 3, sep = ' < ')
print(1, 2, 3) # k có j thì nó sẽ auto sep = ' '

#DEFAULT ARGUMENT
def greet(who="Colin"):
    print("Hello,", who)
#nó để default là colin nếu k có giá trị nhập vào
#có giá trị truyền mới sẽ đè lên giá trị colin

greet()
greet(who = "Kaggle")
greet("world")
# 3 cách để làm, k cần phải viết đầy đủ
# nếu chỉ muốn in y nguyên cái colin => k cần j trong ()
# nếu thik tên khác thì điền hàm string vào đó là đủ
