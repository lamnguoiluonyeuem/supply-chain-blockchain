# Supply Chain Blockchain

+ Đây là ví dụ cơ bản về việc sử dụng Blockchain để quản lý và theo dõi các giao dịch trong chuỗi cung ứng.

## Mô tả

- Sổ cái giao dịch phi tập trung
- Dữ liệu bất biến và an toàn
- Theo dõi lịch sử sản phẩm theo thời gian thực

## Tính năng

1. Blockchain cơ bản:
+ Ghi lại các giao dịch vào một cuốn sổ cái phân tán, phi tập trung.
+ Đảm bảo tính bất biến và bảo mật thông tin giao dịch.

2. Chữ ký số cho giao dịch:
+ Mỗi giao dịch được ký bởi người gửi để đảm bảo tính hợp pháp và an toàn.
+ Xác minh chữ ký số trước khi thêm giao dịch vào blockchain.

3. Theo dõi tình trạng vận chuyển sản phẩm:
+ Theo dõi trạng thái của sản phẩm trong chuỗi cung ứng, như "đang sản xuất", "đang vận chuyển", "đã giao hàng".

4. API để quản lý Blockchain:
+ Sử dụng Flask để tạo endpoint API cho các chức năng như thêm giao dịch, đào (mine) block mới, và truy vấn toàn bộ chuỗi blockchain.

## Yêu cầu cài đặt

+ Để chạy dự án, cần cài đặt các thư viện Python sau

1. Cài đặt các thư viện cần thiết
+ Cryptography: Thư viện cho chữ ký số và mã hóa.
+ Flask: Thư viện để xây dựng API
```
pip install cryptography Flask
```

2. Cấu trúc thư mục và các tệp chính

+ blockchain.py: Mã nguồn chính cho blockchain và xử lý chữ ký số.
+ main.py: Thực hiện các giao dịch và kiểm tra tính năng của blockchain.
+ app.py: Tạo API endpoint với Flask.

## Triển Khai

1. Clone repository

```
git clone https://github.com/your-username/supply-chain-blockchain.git
cd supply-chain-blockchain
```

2. Cài đặt thư viện

```
pip install -r requirements.txt
```
(Tạo file requirements.txt nếu chưa có và thêm các thư viện cần thiết.)

3. Chạy mã nguồn

+ Chạy giao dịch và blockchain:
```
python3 main.py
```
+ Chạy API

## Tài Liệu

1. https://hbr.org/2020/05/using-blockchain-to-improve-supply-chain-management
2. https://www.sciencedirect.com/science/article/pii/S0260877419301405
```
python3 app.py
```

+ Truy cập API thông qua http://localhost:5000 để quản lý blockchain.

