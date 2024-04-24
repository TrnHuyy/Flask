# Sử dụng base image Python
FROM python:3.9-slim

# Thiết lập thư mục làm việc của container
WORKDIR /app

# Sao chép tất cả các tệp từ thư mục hiện tại vào thư mục /app của container
COPY . .

# Cài đặt các dependency của ứng dụng
RUN pip install Flask Flask-Migrate Flask-SQLAlchemy

# Expose cổng mà Flask ứng dụng sẽ chạy trên
EXPOSE 5000

# Chạy lệnh để khởi động Flask ứng dụng
CMD ["python", "app.py"]
