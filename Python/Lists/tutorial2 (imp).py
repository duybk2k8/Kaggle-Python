#INTERLUDE: OBJECT
x = 12
# x is real number => imaginary part is 0 (3.00000)
print(x.imag) # => in ra phần imaginary

c = 12 + 3j #3j là phần ảo
print(c.imag)
print(c.real) #in phần thực

#attribute => dữ liệu đi kèm object => k có dấu () 
#attribute chỉ view dữ liệu, k đụng j vào cả + chỉ chuẩn bị

#method => có dấu () => sẽ làm
# ví dụ: x.bit_length => chỉ chuẩn bị, lấy ra hàm (chưa chạy)
#x.bit_length() => tính ra giá trị số bit luôn
#có thể đổi hàm, hoặc chỉ in ra gtri tức thời, k đổi hàm (như append vs __add__)

#function: hàm riêng VD: len(x)
#method là function đặc biệt => gắn với object
#attribute là non-function => k làm j cả
#ví dụ len([1,2,3]) => k phụ thuộc vào object nào
#x=12, x.bit_length() => phụ thuộc vào x

print(x.bit_length)
print(x.bit_length())

#pass functions to the "help" function
help(x.bit_length)