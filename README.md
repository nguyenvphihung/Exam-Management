# Exam Management System

## Giới thiệu
Dự án **Exam Management System** là một hệ thống quản lý thi trực tuyến, hỗ trợ giáo viên và học sinh trong việc tổ chức, quản lý và tham gia các kỳ thi. Ứng dụng giúp tối ưu hóa quy trình tạo câu hỏi, tổ chức kỳ thi, và theo dõi kết quả thi một cách hiệu quả.

## Tính năng chính
1. **Quản lý câu hỏi**: Hỗ trợ tạo, sửa, xóa các câu hỏi trong hệ thống với các dạng câu hỏi đa dạng như tự luận, trắc nghiệm, v.v.
2. **Tổ chức thi**: Cho phép giáo viên tạo đề thi ngẫu nhiên dựa trên các CLO (Course Learning Outcomes) và thiết lập cấu trúc kỳ thi.
3. **Phân quyền người dùng**: Hệ thống phân quyền cho giáo viên và học sinh, đảm bảo an toàn và bảo mật thông tin.
4. **Theo dõi kết quả**: Hệ thống lưu lại kết quả bài thi của học sinh để giáo viên dễ dàng đánh giá.

## Yêu cầu hệ thống
- Python 3.8+
- Flask
- SQLite (hoặc MySQL nếu muốn mở rộng)
- Các thư viện cần thiết (liệt kê trong `requirements.txt`)

## Hướng dẫn cài đặt
1. **Clone repo**: Tải mã nguồn từ GitHub bằng cách:
   ```bash
   git clone https://github.com/username/Exam-Management.git
   ```
2. **Cài đặt các thư viện**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Thiết lập cơ sở dữ liệu**:
   - Tạo cơ sở dữ liệu SQLite hoặc MySQL và cập nhật thông tin cấu hình trong `config.py`.
   - Khởi tạo bảng trong database bằng lệnh:
     ```bash
     python setup_database.py
     ```

4. **Chạy ứng dụng**:
   ```bash
   python app.py
   ```
5. Truy cập vào trang web tại `http://127.0.0.1:5000/`.

## Hướng dẫn sử dụng

### Đăng nhập
- **Giáo viên** và **học sinh** có tài khoản riêng để đăng nhập vào hệ thống.
- **Giáo viên** có quyền truy cập để quản lý câu hỏi, tạo đề thi, và xem kết quả.
- **Học sinh** chỉ có thể tham gia thi và xem điểm sau khi hoàn tất bài thi.

### Tạo và quản lý câu hỏi
1. Sau khi đăng nhập với tư cách **giáo viên**, điều hướng đến phần **Quản lý câu hỏi**.
2. Tại đây, giáo viên có thể:
   - **Tạo câu hỏi mới**: Chọn loại câu hỏi (tự luận, trắc nghiệm) và nhập nội dung, đáp án đúng.
   - **Chỉnh sửa hoặc xóa câu hỏi**: Thực hiện thay đổi nội dung câu hỏi hiện có hoặc xóa nếu không cần thiết.

### Tổ chức kỳ thi
1. Giáo viên vào phần **Quản lý kỳ thi** để tạo các kỳ thi mới.
2. Khi tạo kỳ thi, giáo viên có thể:
   - Chọn số lượng câu hỏi và độ khó.
   - Thiết lập đề thi ngẫu nhiên từ ngân hàng câu hỏi dựa trên các CLO.
   - Đặt thời gian làm bài và giới hạn thời gian cho mỗi câu hỏi.

### Tham gia thi
1. **Học sinh** đăng nhập và vào mục **Tham gia kỳ thi** để làm bài thi.
2. Khi vào kỳ thi, hệ thống sẽ bắt đầu tính giờ tự động.
3. Sau khi hoàn thành bài thi, học sinh nộp bài để hệ thống chấm điểm tự động (nếu là bài trắc nghiệm) hoặc chấm điểm thủ công (nếu là bài tự luận).

### Xem kết quả
- Giáo viên có thể vào mục **Quản lý kết quả** để xem và xuất kết quả của từng học sinh.
- Học sinh có thể xem lại điểm và bài làm của mình tại mục **Kết quả cá nhân**.

## Đóng góp
Nếu bạn muốn đóng góp cho dự án, hãy fork repo và tạo pull request. Mọi ý kiến đóng góp và đề xuất cải tiến đều được hoan nghênh!

## Liên hệ
- Email: contact@example.com
- GitHub: [https://github.com/username/Exam-Management](https://github.com/username/Exam-Management)
```

Bạn có thể thay thế các thông tin như email và đường dẫn GitHub theo nhu cầu của mình.