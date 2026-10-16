#dataframe
import pandas as pd
reviews = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
#giả sử 

reviews.country
#access country property (column)

reviews.country
# chỉ dùng khi nó k trùng với built in function
reviews['country']
#khi tên cột có khoảng trắng đặc biệt / trùng tên với built-in function

#lấy single value
reviews['country'][0]

#Pandas indexing works in one of two paradigms.
#1) INDEX-BASED SELECTION => select data based on its numerical position in the data
#====> loc
reviews.iloc[0] #first row
#loc and iloc are row-first, column second >< python

#get column

reviews.iloc[:, 0]
#: => lấy tất cả các dòng, 0 -> cột đầu tiên
reviews.iloc[:3, 0]
# lấy 3 dòng đầu ở cột đầu tiên
#a:b => từ a đến b-1
#specific index through list
reviews.iloc[[0, 1, 2], 0]

reviews.iloc[-5:]
#last 5

#2) LABEL-BASED SELECTION
reviews.loc[0, 'country'] #get first entry in reviews
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
#[rows:columns]

#iloc: a:b => từ a đến b-1
#loc: a:b => từ a đến b

reviews.set_index("title")
#create a new row with index title

reviews['critic'] = 'everyone'
reviews['critic']
#create a new column name critic + every value in it is everyone
reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards'] #iterate from len -> 0

reviews.country == 'Italy' #check whether the wine is italian or not
reviews.loc[reviews.country == 'Italy'] # đưa các row mà có country = italy
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)] #AND
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)] #OR
reviews.loc[reviews.country.isin(['Italy', 'France'])]  #multiple values
reviews.loc[reviews.price.notnull()] #isnull => check xem có phải empty k (NaN)

