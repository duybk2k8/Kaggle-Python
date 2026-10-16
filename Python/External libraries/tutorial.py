#IMPORT
import math
print("It's math! It has type {}". format((type(math))))
#math là module => thư viện nhỏ dc viết sẵn để dùng (như có hàm sqrt)

#dir là liệt kê tất cả tên, biến, hàm trong module
print(dir(math))

print("pi to 4 significant digits = {:.4}". format(math.pi))
#.4 là làm tròn đến 4 chữ số có nghĩa

print(math.log(32,2)) #hàm loga

#import mà đặt hàm thành shorter
import math as mt
print(mt.pi)
#or
import math
mt = math

from math import * #như thế này thì chỉ cần để là pi chứ k cần math.pi
print(pi, log(32, 2))
#k nên làm vậy
# ví dụ nếu để cả math cả numpy vào import *, chúng đều có hàm log nhưng có cách dùng khác nhau => bug

#import specific things
from math import log, pi
from numpy import asarray

#SUBMODULES
import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as..."
      ,dir(numpy.random)[-15:]
      )

#để truy cập submodule thì phải có 2 chấm
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)
print(rolls.mean()) #trung bình random  
print(rolls.tolist()) #đổi từ array sang list
#help(rolls) #tell me more
#type(rolls) #what is this thing

#print(rolls + 10) #list k cộng dc nma array dc
#print(rolls <= 3) #trả về boolean

xlist = [[1,2,3], [2,4,6],]
#Create a 2-dimensional array
x = numpy.asarray(xlist) #from list to array
print("xlist = {}\nx =\n{}". format(xlist, x))
print(x[1, -1]) #list truy vấn dc 2 chiều nhưng xlist thì k vdu: xlist[1,-1] => x

import tensorflow 
import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
a + b
#operations => phép toán dc thực hiện trên dữ liệu (tensor)
#operator overloading (nạp chồng toán tử)
# các hàm có dạng __xxx___ => nó sẽ ẩn phía sau sau những hàm chính ta dùng
#example: a+b => thực chất bên trong python đang dùng a.__add__(b)