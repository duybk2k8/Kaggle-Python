#DATA FRAME
import pandas as pd
pd.DataFrame({'Yes' : [50, 21], 'No' : [131, 2]})

#not limited to integers
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
#keys are column names and values are a list of entries

#if want to declare specific index
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])


#SERIES
pd.Series([1, 2, 3, 4, 5])

#want to change index
pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
#series dont have column name, just have an overall name

wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
wine_reviews.shape #check how large (row, column)
wine_reviews.head() #view first five row
#muốn specify x hàng preview (x)
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()
#make pandas recognize and use that column for an index

#Đọc file => read_csv
#lưu file => to_csv
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals
animals.to_csv("cows_and_goats.csv")
#lấy gọi dataframe, tên đặt ở trong ngoặc