import pandas as pd
police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding='latin1')
# nó phải để thêm encode kia tại vì nó có nhiều thứ tiếng lẫn có thể k đọc dc => con latin1 này chấp nhận mọi kí tự bit từ 0 đến 255 ==> chấp nhận mọi thứ

#new_entry_help = sample_entry.decode("big5-tw")
#new_entry = new_entry_help.encode("utf-8")
# ban đầu sample_entry là bytes nhưng dc mã hóa theo big5-tw (bảng tiếng trung phồn thể)
#=> chỉ là dãy nhị phân => ép sang utf thì lỗi
#==> phải decode để giải mã về chuỗi str chuẩn
#encode lại vào utf8

#==> encode thì encode từ cái dạng đó sang str
#==> decode thì decode từ dạng j đó sang dạng này