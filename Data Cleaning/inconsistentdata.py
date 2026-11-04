#fuzzy matching tự động tìm từ trong list có cấu trúc giống chỉ sai 1 tí th
# get the top 10 closest matches to "south korea"

#matches = fuzzywuzzy.process.extract("south korea", countries, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

#top 10 chuỗi tương tự gần giống nhất với south korea
# fuzzywuzzy thư viện này so sánh chuỗi gốc, extract 
# tên, danh sách, limit, thuật toán đo tương đồng
# token_sort_ration: 
# 1) Chuyển thành chữ thường & xóa ký tự đặc biệt
# 2) Cắt chuỗi thành từ riêng biệt
# 3) Sắp xếp lại các từ theo thứ tự bảng chữ cái
# 4) Ghép lại và so sánh độ giống

# function to replace rows in the provided column of the provided dataframe
# that match the provided string above the provided ratio with the provided string
def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):
    #df là dataframe cần xử lý
    # column: tên cột muốn kiểm tra và thay thế dữ liệu
    # string_to_match: chuỗi mẫu muốn thay thế giá trị sai
    # min_ration: ngưỡng điểm tối thiểu quyết định xem chuỗi đủ giống nhau k
    # get a list of unique strings
    strings = df[column].unique()
    
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]
    #duyệt danh sách matches và lọc ra chuỗi số có điểm >= điểm cho phép
    # trong mỗi matches sẽ là 1 cặp tuple dạng (chuỗi tìm, điểm tương đồng)

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match #ghi đè bằng string_to_match
    
    # let us know the function's done
    print("All done!")

    professors['Graduated from'] = professors['Graduated from'].str.strip() # bỏ khoảng trắng