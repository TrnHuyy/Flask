# Kiến thức Python Flask

## Python Core
Ngôn ngữ lập trình phổ biến, dễ dàng sử dụng

## OOP trong Python
Các khái niệm quan trọng:
- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance
- Data Abstraction

## Các tool hỗ trợ

## REST API
REST API (hay RESTful API) là một tiêu chuẩn dùng trong việc thiết kế API cho các ứng dụng web (thiết kế Web services) để tiện cho việc quản lý các resource. Nó chú trọng vào tài nguyên hệ thống (tệp văn bản, ảnh, âm thanh, video...), bao gồm các trạng thái tài nguyên được định dạng và được truyền tải qua HTTP.

Chức năng quan trọng nhất của REST là quy định cách sử dụng các HTTP method (như GET, POST, PUT, DELETE…) và cách định dạng các URL cho ứng dụng web để quản các resource.

REST hoạt động chủ yếu dựa vào giao thức HTTP. Các hoạt động cơ bản nêu trên sẽ sử dụng những phương thức HTTP riêng.

- GET (SELECT): Trả về một Resource hoặc một danh sách Resource.
- POST (CREATE): Tạo mới một Resource.
- PUT (UPDATE): Cập nhật thông tin cho Resource.
- DELETE (DELETE): Xoá một Resource.

## SQLALchemy
SQLAlchemy dùng để tương tác với cơ sở dữ liệu quan hệ một cách linh hoạt và hiệu quả. 

SQLAlchemy cung cấp các công cụ và thư viện cho việc tạo và thực thi các truy vấn SQL, quản lý liên kết giữa đối tượng Python và dữ liệu trong cơ sở dữ liệu.

SQLAlchemy cung cấp bộ công cụ mạnh mẽ để ánh xạ dữ liệu cơ sở dữ liệu vào các đối tượng Python. Điều này cho phép lập trình viên làm việc với dữ liệu thông qua các đối tượng và phương thức Python thay vì sử dụng ngôn ngữ truy vấn SQL một cách trực tiếp.

## Alembic
Alembic có thể xem như là Git cho database, giúp theo dõi những thay đổi về dữ liệu trong database

## Flask-Migrate
Giúp đồng bộ hóa cơ sở dữ liệu với code mà không phải xóa đi tạo lại. 

Flask-migrate sẽ ánh xạ các mô hình được viết trong code sang cơ sở dữ liệu

## Câu hỏi
SQLALchemy có thể ánh xạ dữ liệu như Migrate, vậy điểm khác nhau là gì?

Alembic để cấu hình database nhưng có thể ánh xạ bằng Migrate rồi thì cần gì cấu hình? -> alembic có rollback còn Migrate cũng có rollback