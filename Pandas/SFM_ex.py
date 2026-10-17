import pandas as pd
reviews = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
#5)
#create a variable xem title rượu nào có highest points to price ration
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
#hàm built in idxmax => truy vấn ra title dựa theo idx đó

#6) 
n_trop = reviews.description.map(lambda p: 'tropical' in p).sum()
n_fruity = reviews.description.map(lambda p: 'fruity' in p).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
#builtin sum tính tổng hết tất cả số lần dc mention description, true false tự thành 0, 1

#7)
def stars_points(row):
    if (row.points >= 95) or (row.country == 'Canada'):
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
star_ratings = reviews.apply(stars_points, axis='columns')
#nó sẽ xét từng row 1 tại trục là columns => xét từng rows => trả về 1 series 
#stars_points chỉ là công thức => nó dc apply nhận => apply xét hết row => trả về bảng mới
#stars_points được viết để xử lý một dòng, nên nó không tự lặp qua cả bảng được
