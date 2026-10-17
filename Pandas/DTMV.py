import pandas as pd
reviews = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

#DTYPES
reviews.price.dtype
#dtype('float64')
reviews.dtypes
#return the dtype of every column in the data frame
#strings do not get their own type => object

#can convert if it makes sense
reviews.points.astype('float64')

reviews.index.dtype
reviews[pd.isnull(reviews.country)]
#sử dụng notnull như trái ngược
#==> check xem cái nào null
reviews.region_2.fillna("Unknown")
#fill NaN với "Unknown"

#replace non-null data
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
#nó k lưu mà phải lưu vào biến mới
