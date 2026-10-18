import pandas as pd
reviews = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
#giả sử 

# RENAMING
reviews.rename(columns={'points': 'score'})
# rename tên cột / index
#usually python dictionary is the most convenient
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# thường sẽ dùng set_index() thay vì rename index
reviews.set_index('Họ tên') #nó sẽ biến 1 cột có sẵn thành index

#rename_axis => đổi tên label đại diện cho trục
#nó k có tên khi gọi index column hay row => set tên
# => giúp định danh (giữ nguyên index, chỉ gán tên)
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
#wines là index cho hàng, còn nếu axis bằng column thì là index cho cột
#COMBINING
#concat() => gộp 2 dataframe thành 1 trục => hữu dụng khi có các dataframe chung cột chỉ khác data
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

# join() => combine different dataframe mà có chung index
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
#set index là cột mà 2 cái đó chung
left.join(right, lsuffix='_CAN', rsuffix='_UK')
#hữu dụng khi combine objects mà có index in common
#nó tạo thành 1 multiindex (tuple) => cho cả 2 data frame
#left.join(right) => lấy left r cho thêm right vào: ghép các dòng cùng giá trị với nhau: 1 video xuất hiện ở cả 2 nước, cùng title cùng trending => ghép thành 1 dòng
#left join: giữ toàn bộ dòng ở left (Canada) nếu k có UK thì NaN
# lsuffix rsuffix để nó thêm vào đuôi vì các index của column giống nhau => k bị trùng

#merge giống join