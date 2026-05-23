# Bài Toán 8 Con Hậu

Ứng dụng Python Tkinter mô phỏng và giải bài toán 8 con hậu trên bàn cờ 8x8 bằng 3 hướng tiếp cận:

- DFS (Backtracking)
- BFS với Priority Queue / Heuristic
- Hill Climbing

---

## Giới thiệu

Bài toán 8 con hậu là một bài toán kinh điển trong trí tuệ nhân tạo và lý thuyết tìm kiếm.  
Mục tiêu là đặt 8 quân hậu lên bàn cờ 8x8 sao cho không có hai quân hậu nào tấn công lẫn nhau theo hàng, cột hoặc đường chéo.

Dự án này được xây dựng nhằm:

- Minh họa cách hoạt động của các thuật toán tìm kiếm và tối ưu hóa.
- So sánh hiệu quả giữa DFS, BFS Priority và Hill Climbing.
- Hiển thị lời giải trực quan bằng giao diện đồ họa Tkinter.

---

## Tính năng

- Chọn thuật toán bằng radio button
- Giải bài toán bằng nút `GIẢI BÀI TOÁN`
- Hiển thị bàn cờ 8x8 trực quan
- Duyệt qua nhiều nghiệm với DFS và BFS Priority
- Hỗ trợ chế độ tự động chuyển nghiệm
- Làm mới bàn cờ khi cần

---

## Demo giao diện

### 1. Màn hình chính
Ảnh giao diện ban đầu, trước khi giải bài toán.

![Màn hình chính](Images/ảnh-1-1.png)

---

### 2. Kết quả DFS
DFS dùng backtracking để tìm tất cả các nghiệm hợp lệ của bài toán 8 quân hậu.

![Kết quả DFS](Images/ảnh-1-3.png)

---

### 3. Kết quả BFS Priority
Phần BFS trong project hiện tại được cài đặt theo hướng dùng `heapq` và heuristic để ưu tiên trạng thái tốt hơn.  
Vì vậy, khi trình bày, nên mô tả chính xác là **BFS kết hợp Priority Queue / Best-First theo heuristic**.

![Kết quả BFS Priority](Images/ảnh-1-4.png)

---

### 4. Kết quả Hill Climbing
Hill Climbing khởi tạo trạng thái ngẫu nhiên và liên tục cải thiện để giảm xung đột.

![Kết quả Hill Climbing](Images/ảnh-1-5.png)

---

### 5. DFS hiển thị nhiều nghiệm
Ảnh này cho thấy DFS có thể tìm được toàn bộ 92 nghiệm của bài toán.

![DFS - 92 nghiệm](Images/ảnh-1-2.png)

---

## Cách chạy

### Yêu cầu
- Python 3.x

### Cài đặt
```bash
pip install -r requirements.txt
