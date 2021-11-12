# Introduction-to-Data-Science-DSP301x
#Tên dự án: Tính toán và phân tích điểm thi (Test Grade Calculator)

Tổng quan dự án

Trong bài tập lớn này, bạn cần viết một chương trình để tính toán điểm thi cho nhiều lớp với sĩ số hàng nghìn học sinh. Mục đích của chương trình giúp giảm thời gian chấm điểm. Bạn sẽ áp dụng các functions (hàm) khác nhau trong Python để viết chương trình với các tác vụ sau: 

Mở các tập tin văn bản bên ngoài được yêu cầu với exception-handling
Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng
Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubric) được cung cấp và báo cáo
Tạo tập tin kết quả được đặt tên thích hợp


Hướng dẫn chạy ứng dụng
  Đối với IDLE Python:
    Open file 'lastname_firstname_grade_the_exams.py' -> run -> run module(F5) -> enter filename
  Đối với JupyterLab(Jupyter NoteBook) 
    Create new notebook -> code -> %run lastname_firstname_grade_the_exams.py -> enter filename
  
  Lưu ý các file dữ liệu cần mở phải để trong cùng thư mục gốc với file 'lastname_firstname_grade_the_exams.py' và có phần mở rộng là '.txt'.
  Sau khi ứng dụng chạy thành công sẽ in ra báo cáo và lưu danh sách điểm của từng học sinh vào file '{tên file nhập vào}_grades.txt' cùng thư mục gốc với file lastname_firstname_grade_the_exams.py'.
  Để chạy ứng dụng cần cài đặt pandas và numpy.
