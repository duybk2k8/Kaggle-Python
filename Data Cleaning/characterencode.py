# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
#import charset_normalizer

# set seed for reproducibility
np.random.seed(0)

# start with a string
before = "This is the euro symbol: €"

# check to see what datatype it is
type(before)

# encode it to a different encoding, replacing characters that raise errors
after = before.encode("utf-8", errors="replace")

# check the type
type(after)
#bytes : tất cả cái mã hóa đều về byte, utf 8 là công thức để chuyển về byte
#b'This is the euro symbol: \xe2\x82\xac'
print(after.decode("utf-8"))
# phải dùng đúng encoding map, ở đây là utf-8

# look at the first ten thousand bytes to guess the character encoding
with open("../input/kickstarter-projects/ks-projects-201801.csv", 'rb') as rawdata:
    #result = charset_normalizer.detect(rawdata.read(10000))
#open(...,'rb') => mở file ở chế độ đọ nhị phân (r là read, b là binary) => chưa cần đọc chữ ra hiển thị, chỉ cần bốc nguyên đống mã nhị phân thô để đem đi soi
#with ... as rawdata => tự động đóng khi xong xuôi, trái rò rỉ
#rawdata.read(10000) đọc 10000 byte đầu tiên
#charset_normalizer chấm điểm đoán xem nó thuộc mã nào
# save our file (will be saved as UTF-8 by default!)
#kickstarter_2016.to_csv("ks-projects-201801-utf8.csv")
