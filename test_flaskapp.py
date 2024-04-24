import pytest
from app import app, db  # Thay `your_application` bằng tên module của ứng dụng của bạn
from app import Todo  # Thay `your_application` bằng tên module của ứng dụng của bạn

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Đảm bảo rằng database được tạo mới và chưa có dữ liệu nào
    with app.app_context():
        db.create_all()

    yield client

    # Xóa toàn bộ dữ liệu trong database sau khi test hoàn thành
    with app.app_context():
        db.drop_all()

def test_update_task(client):
    # Tạo một task mới để test
    new_task = Todo(content='Test task')
    db.session.add(new_task)
    db.session.commit()

    # Gửi một POST request để cập nhật task với nội dung mới
    response = client.post(f'/update/{new_task.id}', data={'content': 'Updated task content'})

    # Kiểm tra xem request có thành công hay không
    assert response.status_code == 302  # 302 là mã trạng thái cho redirect

    # Kiểm tra xem task đã được cập nhật thành công trong database hay không
    updated_task = Todo.query.get(new_task.id)
    assert updated_task.content == 'Updated task content'

    # Kiểm tra xem nếu có một exception xảy ra trong quá trình cập nhật, thì nó sẽ được bắt và trả về thông báo lỗi
    response = client.post(f'/update/{new_task.id}', data={})  # Gửi một request không hợp lệ
    assert b'There was an issue updating your task' in response.data

    # Kiểm tra xem nếu request không phải là POST request thì trang update sẽ được hiển thị đúng cách
    response = client.get(f'/update/{new_task.id}')
    assert b'Update Task' in response.data
    assert b'Test task' in response.data
