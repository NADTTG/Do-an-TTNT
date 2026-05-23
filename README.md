# BÀI TOÁN 8 QUÂN HẬU

Ứng dụng Python Tkinter mô phỏng và giải bài toán 8 quân hậu trên bàn cờ 8x8 bằng 3 hướng tiếp cận:

- DFS (Depth-First Search / Backtracking)
- BFS với Priority Queue và Heuristic
- Hill Climbing

---

## Mục tiêu dự án

Bài toán 8 quân hậu là một bài toán kinh điển trong trí tuệ nhân tạo và lý thuyết tìm kiếm.  
Mục tiêu của dự án là:

- Minh họa cách hoạt động của các thuật toán tìm kiếm và tối ưu hóa.
- So sánh hiệu quả giữa DFS, BFS và Hill Climbing.
- Trực quan hóa nghiệm bằng giao diện đồ họa.
- Giúp người học hiểu rõ hơn về không gian trạng thái và kỹ thuật backtracking.

---

## Mô tả bài toán

Bài toán 8 quân hậu yêu cầu đặt 8 quân hậu lên bàn cờ kích thước 8x8 sao cho không có hai quân hậu nào tấn công lẫn nhau theo:

- Hàng ngang
- Cột dọc
- Đường chéo

Đối với bài toán 8 quân hậu, tổng số nghiệm hợp lệ là **92**.

---

## Tính năng của chương trình

- Chọn thuật toán giải bằng radio button.
- Hiển thị bàn cờ 8x8 trực quan.
- Vẽ quân hậu bằng biểu tượng `♕`.
- Xem nhiều nghiệm với DFS và BFS Priority.
- Hỗ trợ chuyển nghiệm trước / sau.
- Có chế độ tự động chuyển nghiệm.
- Làm mới bàn cờ khi cần.

---

## Các thuật toán được sử dụng

### 1. DFS (Depth-First Search)
DFS được cài đặt theo kiểu backtracking:

- Đặt quân hậu lần lượt theo từng hàng.
- Kiểm tra xem vị trí đặt có an toàn hay không.
- Nếu đi vào ngõ cụt thì quay lui.
- Thu thập tất cả các nghiệm hợp lệ.

### 2. BFS với Priority Queue
Trong chương trình, phần BFS được triển khai bằng `heapq` kết hợp heuristic:

- Mỗi trạng thái bàn cờ được gán một giá trị đánh giá.
- Trạng thái nào có heuristic nhỏ hơn sẽ được ưu tiên xử lý trước.
- Tiếp tục mở rộng các trạng thái tốt hơn cho đến khi tìm được nghiệm.

> Lưu ý: phần này thiên về **Best-First Search / Priority Search** hơn là BFS thuần.

### 3. Hill Climbing
Hill Climbing là phương pháp tối ưu hóa cục bộ:

- Khởi tạo ngẫu nhiên vị trí các quân hậu.
- Sinh các trạng thái lân cận.
- Chọn trạng thái có ít xung đột hơn.
- Dừng khi không thể cải thiện thêm hoặc tìm được nghiệm hợp lệ.

---

## Cách chạy chương trình

### Yêu cầu
- Python 3.x
- Thư viện `tkinter` (thường có sẵn trong Python)
- Các thư viện chuẩn: `random`, `heapq`, `time`, `threading`

### Chạy chương trình
```bash
python app.py
