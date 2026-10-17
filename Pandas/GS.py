import pandas as pd

reviews = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

reviews.groupby('points').points.count()
#giống value_counts()
#groupby tạo ra group of reviews mà có same points value, sau đó each of these groups thì grabbed the points() column and counted how many times it appeared

reviews.groupby('points').price.min()
#xem từng group chung points có price thấp nhất là bn
#=> group chung points => chọn cột price => lấy giá trị min

reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
#select the first wine reviewed from each winery

#group more than one column
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])
#pick out the best wine by country and province

#agg => run a diff functions 
reviews.groupby(['country']).price.agg([len, min, max])
#group by country => select cột price => tạo 1 bảng nhiều cột: len (tổng số loại rượu của nc đó) min (giá thấp nhất) max (giá cao nhất)

#MULTI-INDEXES
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed
#tạo ra các group chung country + province => chọn cột description

mi = countries_reviewed.index
type(mi)
#pandas.core.indexes.multi.MultiIndex
#Mỗi nhóm được xác định bởi cặp (country, province), nên pandas dùng cả hai làm index
#Nhãn của mỗi dòng là một tuple, ví dụ ('Argentina', 'Mendoza Province')

#converting back to regular index
countries_reviewed.reset_index()
#ví dụ argentina nhiều province thì bị nhân lên chứ k dc group chung nx

#SORTING
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')
#sort by length => ascending (lowest)
countries_reviewed.sort_values(by='len', ascending=False)
#want descending => ascending = False
#chỉ có by nếu nó là dataframe, còn series thì k cần

countries_reviewed.sort_index()
#sort by index (default order)

countries_reviewed.sort_values(by=['country', 'len'])
#sort more than 1 column, sort country trc, nếu country chung thì qua len