import pandas as pd
import numpy as np

# Kết quả thi chuẩn để so sánh
answer_key = 'B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D'
arr_scores = []

# Hàm tính số điểm của từng học sinh.
def mark(row):
    arr_key = answer_key.split(',')
    scores = 0
    i=0
    # Duyệt từng đáp án so sánh với kết quả chuẩn.
    for col in row:
        # Nếu là cột đầu tiên(Mã học sinh) hoặc không có đáp án thì bỏ qua.
        if i != 0 and col:
            if col == arr_key[i-1]:
                scores += 4
            else:
                scores -= 1
        i=i+1
    arr_scores.append([row[0], scores]) 

# Hàm ghi danh sách điểm của học sinh ra file text.
def write(df):
    rpPath = filename.strip()+'_grades.txt'
    with open(rpPath,'w') as f:
        for index, r in df.iterrows():
            f.write(str(r[0]) + ', ' + str(r[1]))
            f.write('\n')

# Nhập vào tên file dữ liệu
filename = input("Enter a filename: ")
if filename:
    try:
        filePath = filename.strip()+'.txt'
        total_valid = 0
        total_invalid = 0
        arrlist = []
        # Đọc file.
        with open(filePath, 'r') as file:
            print("Successfully opened ", filename)
            print('**** ANALYZING ****')
            # Đọc từng dòng của file, tách dữ liệu thành mảng phân cách bằng dấu ',', lưu dữ liệu vào biến chứa danh sách.
            for line in file:
                result = line.split(',')
                arrlist.append(result)
            file.close()
            # Tạo dataframe từ danh sách dữ liệu đã lấy ra khỏi file text.
            df = pd.DataFrame(arrlist)
            
            # Lọc dòng dữ liệu thừa hoặc thiếu các trường thông tin.
            invalid_1 =df.loc[(df.count(1) != 26)]
            # Lọc dòng dữ liệu mã học sinh không đúng định dạng.
            invalid_2 = df.loc[(df[0].str.get(0) != 'N') | (~df[0].str[1:].str.isnumeric()) | (df[0].str.len() != 9)]
            # Lọc dòng dữ liệu hợp lệ.
            valid = df.loc[(~df[0].isin(invalid_1[0])) & (~df[0].isin(invalid_2[0]))]
            
            # Duyệt từng dòng dataframe dữ liệu hợp lệ truyền vào hàm tính điểm.
            valid.apply(lambda row:  mark(row), axis=1)
            
            # Tạo dataframe từ danh sách điểm của học sinh đã được tính.
            df_scores = pd.DataFrame(arr_scores)
            # Sắp xếp dữ điểm của học sinh theo chiều tăng dần và đánh lại index.
            df_scores = df_scores.sort_values([1], ascending=[True]).reset_index(drop=True)
            
            # Tổng số dòng không hợp lệ.
            total_invalid = len(invalid_1) + len(invalid_2)
            # Tổng số dòng hợp lệ.
            total_valid = len(valid)
            # Điểm trung bình.
            mean_scores = round(df_scores[1].mean(), 2)
            # Điểm cao nhất.
            highest_scores = df_scores[1].max()
            # Điểm thấp nhất.
            lowest_scores = df_scores[1].min()
            # Miền giá trị.
            range_scores = highest_scores-lowest_scores
            # Giá trị trung vị.
            median_score = np.median(df_scores[1])
            
            # Gọi hàm lưu điểm vào file text.
            write(df_scores)
            
            # In ra báo cáo.
            print('Invalid line of data: does not contain exactly 26 values:')
            print(invalid_1)
            print('Invalid line of data: N# is invalid:')
            print(invalid_2)
            print('**** REPORT ****')
            print('Total valid lines of data: ', total_valid)
            print('Total invalid lines of data: ', total_invalid)
            print('Mean (average) score: ', mean_scores)
            print('Highest score: ', highest_scores)
            print('Lowest score: ', lowest_scores)
            print('Range of scores: ', range_scores)
            print('Median score: ', median_score)
    except:
        print("File cannot be found.")
else:
    print("Filename cannot be empty.")
