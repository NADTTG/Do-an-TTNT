# Bài Toán 8 Quân Hậu

Ứng dụng Python Tkinter mô phỏng và giải bài toán 8 quân hậu trên bàn cờ 8x8 bằng 3 hướng tiếp cận:

- DFS (Depth-First Search / Backtracking)
- BFS với Priority Queue / Heuristic
- Hill Climbing

---

## Giới thiệu

Bài toán 8 quân hậu là một bài toán kinh điển trong trí tuệ nhân tạo và tìm kiếm trạng thái.  
Mục tiêu là đặt 8 quân hậu lên bàn cờ 8x8 sao cho không có hai quân hậu nào tấn công nhau theo hàng, cột hoặc đường chéo.

Project này được xây dựng nhằm:

- minh họa cách hoạt động của các thuật toán tìm kiếm và tối ưu hóa,
- so sánh hiệu quả giữa các phương pháp giải,
- hiển thị kết quả trực quan bằng giao diện đồ họa Tkinter.

---

## Tính năng

- Chọn thuật toán bằng radio button
- Giải bài toán bằng nút **GIẢI BÀI TOÁN**
- Hiển thị bàn cờ và vị trí các quân hậu
- Xem nhiều nghiệm với DFS / BFS Priority
- Hỗ trợ tự động chuyển nghiệm
- Làm mới bàn cờ khi cần

---

## Demo giao diện

### 1. Giao diện chính
![Giao diện chính](../Images/anh1_1.png)

Ảnh này minh họa màn hình ban đầu của chương trình, nơi người dùng có thể chọn thuật toán để giải bài toán.

### 2. Kết quả khi dùng DFS
![DFS](../Images/anh1_3.png)

DFS dùng backtracking để duyệt và tìm tất cả các nghiệm hợp lệ của bài toán.

### 3. Kết quả khi dùng BFS
![BFS](../Images/anh1_4.png)

BFS trong project được cài đặt theo hướng ưu tiên trạng thái bằng heuristic và `heapq`.

### 4. Kết quả khi dùng Hill Climbing
![Hill Climbing](../Images/anh1_5.png)

Hill Climbing bắt đầu từ trạng thái ngẫu nhiên và cố gắng giảm xung đột cho đến khi tìm được nghiệm.

### 5. DFS tìm được 92 nghiệm
![DFS 92 solutions](../Images/anh1_2.png)

Đây là ảnh cho thấy DFS có thể tìm ra toàn bộ 92 nghiệm của bài toán 8 quân hậu.

---

## Ý tưởng hoạt động

### DFS
- Đặt quân hậu lần lượt theo từng hàng
- Kiểm tra vị trí an toàn
- Nếu đi vào ngõ cụt thì quay lui
- Lưu tất cả nghiệm hợp lệ

### BFS Priority
- Mỗi trạng thái bàn cờ được đánh giá bằng heuristic
- Trạng thái có heuristic nhỏ hơn sẽ được ưu tiên xử lý trước
- Tiếp tục mở rộng cho đến khi tìm được nghiệm

### Hill Climbing
- Khởi tạo ngẫu nhiên vị trí quân hậu
- Sinh các trạng thái lân cận
- Chọn trạng thái có ít xung đột hơn
- Dừng khi đạt trạng thái tối ưu hoặc không cải thiện được nữa

---

## Cách chạy

```bash
pip install -r requirements.txt
python app.py
