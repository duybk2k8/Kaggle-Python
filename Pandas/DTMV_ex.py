import pandas as pd
reviews = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

#1)
n_missing_prices = reviews[pd.isnull(reviews.price)].shape[0]
#shape trả về tuple (số dòng, số cột) => lấy dòng th => shape[0]

#4)
reviews_per_region = reviews.region_1.fillna("Unknown").value_counts()
#replace unknown thì nó chỉ trả lại 1 series th

reviews_per_region.index     # danh sách tên vùng
reviews_per_region.values    # danh sách số đếm