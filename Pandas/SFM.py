import pandas as pd
reviews = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

reviews.points.describe()
# high-level summary
#type-aware => output changes based on the data type of the input

reviews.points.mean() #see the mean
reviews.points.median()
reviews.taster_name.unique() #create a list of unique values
reviews.taster_name.value_counts() #see a list of unique values và how often they occur (tần suất xuất hiện)

#map => đưa vào giá trị/quy tắc và áp quy tắc lên các ô dc chọn
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)
#nhận vào p, trả về p - mean
#map chỉ áp dc vào 1 cột, apply áp dc all

def center(p):
    return p - review_points_mean
#lambda chỉ là cách viết gọn hơn cho hàm này
#k tự lưu vào bảng
#expect a single value => return transformed version

#map chỉ dùng dc trên cột, apply dùng dc cả bảng dataframe
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
#apply lấy từng dòng của reviews, đưa vào hàm vào tham số row, trả về 1 bảng mới
#axis = 'columns' => hàm gộp hết cột, mỗi lần xử lý 1 dòng
#axis = 'index' => hàm gộp hết dòng, mỗi lần sử lý trọn 1 cột

#map and apply don't modify the original data they're called on

#built-in function
review_points_mean = reviews.points.mean() #median
reviews.points - review_points_mean

reviews.country + " - " + reviews.region_1
#combining strings

