import pandas as pd
reviews = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

#3)
price_extremes = reviews.groupby(['variety']).price.agg([min, max])
#tạo ra 2 cột theo price, 1 cột min 1 cột max

sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
#sort cột min, max theo descending

#6)
country_variety_counts = reviews.groupby(['country', 'variety']).country.count().sort_values(ascending=False)
#chọn cột nào cũng dc vì nó sẽ đếm dựa theo tuple
#count chỉ có index và 1 dãy => series => k có by
#count chỉ đếm là có bao nhiêu row trong cột dc chọn, chứ k chia ra nữa => nhầm với value_counts => đếm số lần xuất hiện

#COUNT THÌ NHỚ CHỌN CỘT THÌ NÓ MỚI TÍNH DC
#nếu chọn price thì có nhiều chỗ có null thì nó sẽ k tính => chọn cái nào đảm bảo có đủ