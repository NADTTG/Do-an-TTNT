import tkinter as tk
from tkinter import ttk, messagebox
import random
import heapq 
import time
import threading

# ======================================================
# PHẦN THUẬT TOÁN 8 QUÂN HẬU (DFS, BFS với Priority Queue, HILL CLIMBING)
# ======================================================

class EightQueensSolver:
    """Giải thuật 8 quân hậu - Hỗ trợ DFS, BFS với Priority Queue, Hill Climbing"""
    
    def __init__(self):
        self.N = 8  # Cố định N = 8
    
    # ========== 1. THUẬT TOÁN DFS (Depth-First Search) - Backtracking ==========
    def solve_dfs(self):
        """Giải 8 quân hậu bằng DFS (Backtracking) - Tìm tất cả nghiệm"""
        solutions = []
        
        def is_safe(board, row, col):
            for r in range(row):
                if board[r] == col or abs(board[r] - col) == abs(r - row):
                    return False
            return True
        
        def backtrack(board, row):
            if row == self.N:
                solutions.append(board[:])
                return
            
            for col in range(self.N):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)
                    board[row] = -1
        
        board = [-1] * self.N
        backtrack(board, 0)
        return self._convert_to_positions(solutions)
    
    # ========== 2. THUẬT TOÁN BFS VỚI HÀNG ĐỢI ƯU TIÊN (Priority Queue) ==========
    def _heuristic_bfs(self, board):
        """
        Hàm heuristic cho BFS ưu tiên
        Tính số cặp quân hậu đang tấn công nhau + số hàng đã đặt
        Giá trị càng nhỏ càng được ưu tiên
        """
        attacks = 0
        queens_count = 0
        n = self.N
        
        # Đếm số quân hậu đã đặt và số xung đột
        for i in range(n):
            if board[i] != -1:
                queens_count += 1
                for j in range(i + 1, n):
                    if board[j] != -1:
                        if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                            attacks += 1
        
        # Heuristic = số xung đột * 10 - số quân hậu (ưu tiên đặt được nhiều hậu)
        return attacks * 10 - queens_count
    
    def solve_bfs_priority(self):
        """
        Giải 8 quân hậu bằng BFS với hàng đợi ưu tiên (Priority Queue)
        Sử dụng heapq - phần tử có giá trị heuristic NHỎ NHẤT được xử lý trước
        Tìm tất cả nghiệm
        """
        solutions = []
        visited = set()
        n = self.N
        
        initial_board = [-1] * n
        initial_heuristic = self._heuristic_bfs(initial_board)
        
        priority_queue = []
        heapq.heappush(priority_queue, (initial_heuristic, 0, tuple(initial_board), 0))
        
        while priority_queue:
            heur, depth, board_tuple, row = heapq.heappop(priority_queue)
            board = list(board_tuple)
            
            if row == n and heur == -8:
                if board not in [list(sol) for sol in solutions]:
                    solutions.append(board[:])
                continue
            
            state_key = tuple(board)
            if state_key in visited:
                continue
            visited.add(state_key)
            
            if row >= n:
                continue
            
            for col in range(n):
                is_safe_pos = True
                for r in range(row):
                    if board[r] == col or abs(board[r] - col) == abs(r - row):
                        is_safe_pos = False
                        break
                
                if is_safe_pos:
                    new_board = board[:]
                    new_board[row] = col
                    new_heuristic = self._heuristic_bfs(new_board)
                    
                    heapq.heappush(priority_queue, 
                                 (new_heuristic, row + 1, tuple(new_board), row + 1))
        
        unique_solutions = []
        for sol in solutions:
            if sol not in unique_solutions:
                unique_solutions.append(sol)
        
        return self._convert_to_positions(unique_solutions)
    
    # ========== 3. THUẬT TOÁN HILL CLIMBING ==========
    def _evaluate(self, positions):
        """Tính số xung đột giữa các quân hậu"""
        attacks = 0
        n = self.N
        for i in range(n):
            for j in range(i + 1, n):
                if positions[i] == positions[j] or abs(positions[i] - positions[j]) == abs(i - j):
                    attacks += 1
        return attacks
    
    def _get_neighbors(self, positions):
        """Tạo trạng thái lân cận (di chuyển 1 quân hậu trong cùng hàng)"""
        neighbors = []
        n = self.N
        for i in range(n):
            for j in range(n):
                if j != positions[i]:
                    new_positions = positions[:]
                    new_positions[i] = j
                    neighbors.append(new_positions)
        return neighbors
    
    def solve_hill_climbing(self, max_restarts=200):
        """Giải 8 quân hậu bằng Hill Climbing (chỉ tìm 1 nghiệm tối ưu)"""
        
        def single_hill_climbing(max_iterations=1000):
            current = [random.randint(0, self.N - 1) for _ in range(self.N)]
            
            for _ in range(max_iterations):
                current_attacks = self._evaluate(current)
                
                if current_attacks == 0:
                    return current
                
                neighbors = self._get_neighbors(current)
                best = min(neighbors, key=self._evaluate)
                best_attacks = self._evaluate(best)
                
                if best_attacks >= current_attacks:
                    return None
                
                current = best
            return None
        
        for _ in range(max_restarts):
            result = single_hill_climbing()
            if result is not None:
                return self._convert_to_positions([result])
        
        return []
    
    def _convert_to_positions(self, solutions):
        """Chuyển đổi nghiệm từ dạng mảng cột sang dạng tọa độ (row, col)"""
        result = []
        for sol in solutions:
            positions = []
            for row, col in enumerate(sol):
                if col != -1:
                    positions.append((row, col))
            result.append(positions)
        return result


# ======================================================
# PHẦN GIAO DIỆN ĐỒ HỌA (GUI) - PHONG CÁCH GIỐNG CODE THỨ 2
# ======================================================

class EightQueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bài Toán 8 Quân Hậu - DFS | BFS (Priority) | Hill Climbing")
        self.root.geometry("950x800")
        self.root.resizable(True, True)
        self.root.configure(bg="#2c3e50")
        
        # Biến lưu trạng thái
        self.N = 8
        self.algorithm = tk.StringVar(value="DFS")
        self.solutions = []
        self.current_index = 0
        self.cell_size = 60
        self.auto_play_running = False
        self.auto_id = None
        self.solving = False
        
        # Thiết lập giao diện
        self.setup_ui()
        
    def setup_ui(self):
        """Thiết lập toàn bộ giao diện - phong cách giống code thứ 2"""
        
        # ========== FRAME TIÊU ĐỀ ==========
        title_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        title_frame.pack(fill=tk.X, pady=(10, 0))
        
        title_label = tk.Label(title_frame, 
                               text="♕ BÀI TOÁN 8 QUÂN HẬU ♕",
                               font=("Arial", 22, "bold"),
                               bg="#2c3e50", fg="#ecf0f1")
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame,
                                  text="DFS | BFS (Priority Queue với heapq) | Hill Climbing Algorithm Visualizer",
                                  font=("Arial", 11),
                                  bg="#2c3e50", fg="#bdc3c7")
        subtitle_label.pack()
        
        # ========== FRAME ĐIỀU KHIỂN ==========
        control_frame = tk.Frame(self.root, bg="#34495e", relief=tk.RAISED, bd=2)
        control_frame.pack(fill=tk.X, padx=20, pady=15)
        
        # Dòng 1: Hiển thị N và chọn thuật toán
        row1 = tk.Frame(control_frame, bg="#34495e")
        row1.pack(pady=10)
        
        tk.Label(row1, text="Bàn cờ 8x8 (8 quân hậu)",
                font=("Arial", 13, "bold"), bg="#34495e", fg="#f1c40f").pack(side=tk.LEFT, padx=10)
        
        tk.Label(row1, text="|  Thuật toán:",
                font=("Arial", 12), bg="#34495e", fg="white").pack(side=tk.LEFT, padx=(20, 5))
        
        # Radio buttons cho thuật toán
        algo_frame = tk.Frame(row1, bg="#34495e")
        algo_frame.pack(side=tk.LEFT)
        
        dfs_rb = tk.Radiobutton(algo_frame, text="DFS", value="DFS", variable=self.algorithm,
                                 bg="#34495e", fg="white", selectcolor="#34495e",
                                 font=("Arial", 11, "bold"))
        dfs_rb.pack(side=tk.LEFT, padx=8)
        
        bfs_rb = tk.Radiobutton(algo_frame, text="BFS (Priority)", value="BFS", variable=self.algorithm,
                                 bg="#34495e", fg="white", selectcolor="#34495e",
                                 font=("Arial", 11, "bold"))
        bfs_rb.pack(side=tk.LEFT, padx=8)
        
        hill_rb = tk.Radiobutton(algo_frame, text="Hill Climbing", value="Hill Climbing", variable=self.algorithm,
                                  bg="#34495e", fg="white", selectcolor="#34495e",
                                  font=("Arial", 11, "bold"))
        hill_rb.pack(side=tk.LEFT, padx=8)
        
        self.solve_btn = tk.Button(row1, text="🎯 GIẢI BÀI TOÁN", font=("Arial", 12, "bold"),
                                    bg="#27ae60", fg="white", padx=20, pady=5,
                                    command=self.solve_problem)
        self.solve_btn.pack(side=tk.LEFT, padx=20)
        
        self.reset_btn = tk.Button(row1, text="🔄 LÀM MỚI", font=("Arial", 12, "bold"),
                                    bg="#e74c3c", fg="white", padx=20, pady=5,
                                    command=self.reset_board)
        self.reset_btn.pack(side=tk.LEFT, padx=5)
        
        # Dòng 2: Điều hướng nghiệm
        row2 = tk.Frame(control_frame, bg="#34495e")
        row2.pack(pady=10)
        
        self.prev_btn = tk.Button(row2, text="◀ NGHIỆM TRƯỚC", font=("Arial", 11),
                                   bg="#3498db", fg="white", padx=15, pady=3,
                                   command=self.prev_solution, state=tk.DISABLED)
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        self.solution_label = tk.Label(row2, text="Nghiệm: 0 / 0",
                                        font=("Arial", 13, "bold"),
                                        bg="#34495e", fg="#f1c40f")
        self.solution_label.pack(side=tk.LEFT, padx=20)
        
        self.next_btn = tk.Button(row2, text="NGHIỆM SAU ▶", font=("Arial", 11),
                                   bg="#3498db", fg="white", padx=15, pady=3,
                                   command=self.next_solution, state=tk.DISABLED)
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        self.auto_btn = tk.Button(row2, text="▶ TỰ ĐỘNG", font=("Arial", 11),
                                   bg="#f39c12", fg="white", padx=15, pady=3,
                                   command=self.toggle_auto_play, state=tk.DISABLED)
        self.auto_btn.pack(side=tk.LEFT, padx=20)
        
        # Thanh tiến trình
        self.progress = ttk.Progressbar(control_frame, mode='indeterminate', length=400)
        self.progress.pack(pady=10)
        
        # Label trạng thái
        self.status_label = tk.Label(control_frame,
                                      text="✨ Chọn thuật toán (DFS, BFS Priority, Hill Climbing) và nhấn 'GIẢI BÀI TOÁN' ✨",
                                      font=("Arial", 10, "italic"),
                                      bg="#34495e", fg="#ecf0f1")
        self.status_label.pack(pady=5)
        
        # ========== FRAME BÀN CỜ ==========
        board_frame = tk.Frame(self.root, bg="#ecf0f1", relief=tk.SUNKEN, bd=3)
        board_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
        
        self.board_canvas = tk.Canvas(board_frame, bg="#fdf6e3", highlightthickness=0)
        self.board_canvas.pack(expand=True, fill=tk.BOTH)
        
        # Ràng buộc sự kiện resize
        self.board_canvas.bind("<Configure>", self.on_resize)
        
        # ========== FRAME FOOTER ==========
        footer_frame = tk.Frame(self.root, bg="#2c3e50", height=40)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        footer_label = tk.Label(footer_frame,
                                 text="📌 DFS: Tìm tất cả 92 nghiệm | BFS (Priority Queue với heapq): Ưu tiên trạng thái có heuristic nhỏ nhất | Hill Climbing: Tìm 1 nghiệm tối ưu",
                                 font=("Arial", 9), bg="#2c3e50", fg="#7f8c8d")
        footer_label.pack(pady=8)
    
    def on_resize(self, event):
        """Xử lý khi cửa sổ thay đổi kích thước"""
        if self.solutions and self.current_index < len(self.solutions):
            self.draw_board(self.solutions[self.current_index])
        else:
            self.draw_board()
    
    def draw_board(self, solution=None):
        """Vẽ bàn cờ 8x8 và các quân hậu"""
        if self.board_canvas is None:
            return
        
        n = 8
        
        canvas_width = self.board_canvas.winfo_width()
        canvas_height = self.board_canvas.winfo_height()
        
        if canvas_width <= 10 or canvas_height <= 10:
            canvas_width = 500
            canvas_height = 500
        
        self.cell_size = min(canvas_width, canvas_height) // n
        if self.cell_size < 20:
            self.cell_size = 20
        
        board_size = self.cell_size * n
        start_x = (canvas_width - board_size) // 2
        start_y = (canvas_height - board_size) // 2
        
        self.board_canvas.delete("all")
        
        solution_set = set(solution) if solution else set()
        
        for i in range(n):
            for j in range(n):
                x1 = start_x + j * self.cell_size
                y1 = start_y + i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Màu ô cờ (giống bàn cờ vua)
                if (i + j) % 2 == 0:
                    color = "#f0d9b5"  # Ô sáng
                else:
                    color = "#b58863"  # Ô tối
                
                self.board_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#8b7355", width=1)
                
                # Vẽ quân hậu
                if (i, j) in solution_set:
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    radius = self.cell_size // 3
                    
                    # Vẽ vòng tròn nền
                    self.board_canvas.create_oval(center_x - radius, center_y - radius,
                                                   center_x + radius, center_y + radius,
                                                   fill="#e74c3c", outline="#c0392b", width=2)
                    
                    # Vẽ vương miện
                    crown_size = radius // 2
                    self.board_canvas.create_rectangle(center_x - crown_size, center_y - radius - crown_size//2,
                                                         center_x + crown_size, center_y - radius + crown_size//2,
                                                         fill="#f1c40f", outline="#e67e22", width=1)
                    
                    # Vẽ biểu tượng quân hậu
                    self.board_canvas.create_text(center_x, center_y, text="♕",
                                                    font=("Arial", radius, "bold"),
                                                    fill="white")
        
        # Vẽ số hàng và cột
        for i in range(n):
            self.board_canvas.create_text(start_x - 15, start_y + i * self.cell_size + self.cell_size // 2,
                                           text=str(i + 1), font=("Arial", 10, "bold"), fill="#2c3e50")
            self.board_canvas.create_text(start_x + i * self.cell_size + self.cell_size // 2, start_y - 15,
                                           text=str(i + 1), font=("Arial", 10, "bold"), fill="#2c3e50")
    
    def solve_problem(self):
        """Giải bài toán với thuật toán đã chọn"""
        if self.solving:
            return
        
        algo = self.algorithm.get()
        
        self.solving = True
        self.stop_auto_play()
        self.status_label.config(text=f"⏳ Đang giải với thuật toán {algo} (8 quân hậu)...")
        self.solve_btn.config(state=tk.DISABLED, text="⏳ ĐANG GIẢI...")
        self.progress.start()
        self.root.update()
        
        # Chạy trong thread riêng
        thread = threading.Thread(target=self._run_solver, args=(algo,))
        thread.daemon = True
        thread.start()
    
    def _run_solver(self, algo):
        """Chạy solver trong thread riêng"""
        solver = EightQueensSolver()
        
        start_time = time.time()
        
        if algo == "DFS":
            self.solutions = solver.solve_dfs()
        elif algo == "BFS":
            self.solutions = solver.solve_bfs_priority()
        else:  # Hill Climbing
            self.solutions = solver.solve_hill_climbing(max_restarts=200)
        
        elapsed_time = time.time() - start_time
        
        self.root.after(0, self._update_ui_after_solve, algo, elapsed_time)
    
    def _update_ui_after_solve(self, algo, elapsed_time):
        """Cập nhật giao diện sau khi giải xong"""
        self.progress.stop()
        self.solving = False
        self.solve_btn.config(state=tk.NORMAL, text="🎯 GIẢI BÀI TOÁN")
        
        if self.solutions:
            self.current_index = 0
            self.draw_board(self.solutions[0])
            count = len(self.solutions)
            
            self.status_label.config(text=f"✅ {algo}: Tìm thấy {count} nghiệm (Thời gian: {elapsed_time:.3f}s)")
            self.solution_label.config(text=f"Nghiệm: 1 / {count}")
            
            if count > 1:
                self.prev_btn.config(state=tk.NORMAL)
                self.next_btn.config(state=tk.NORMAL)
                self.auto_btn.config(state=tk.NORMAL)
            else:
                self.prev_btn.config(state=tk.DISABLED)
                self.next_btn.config(state=tk.DISABLED)
                self.auto_btn.config(state=tk.DISABLED)
        else:
            self.draw_board()
            self.status_label.config(text=f"❌ {algo}: Không tìm thấy nghiệm nào cho 8 quân hậu")
            self.solution_label.config(text="Nghiệm: 0 / 0")
            self.prev_btn.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.DISABLED)
            self.auto_btn.config(state=tk.DISABLED)
    
    def reset_board(self):
        """Reset bàn cờ về trạng thái ban đầu"""
        self.stop_auto_play()
        self.solutions = []
        self.current_index = 0
        self.draw_board()
        self.status_label.config(text=f"✨ Đã reset. Chọn thuật toán và nhấn 'GIẢI BÀI TOÁN' ✨")
        self.solution_label.config(text="Nghiệm: 0 / 0")
        self.prev_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.DISABLED)
        self.auto_btn.config(state=tk.DISABLED)
        self.auto_btn.config(text="▶ TỰ ĐỘNG", bg="#f39c12")
    
    def prev_solution(self):
        """Hiển thị nghiệm trước đó"""
        self.stop_auto_play()
        if self.solutions and self.current_index > 0:
            self.current_index -= 1
            self.draw_board(self.solutions[self.current_index])
            total = len(self.solutions)
            self.solution_label.config(text=f"Nghiệm: {self.current_index + 1} / {total}")
            self.update_nav_buttons()
    
    def next_solution(self):
        """Hiển thị nghiệm tiếp theo"""
        if self.solutions and self.current_index < len(self.solutions) - 1:
            self.current_index += 1
            self.draw_board(self.solutions[self.current_index])
            total = len(self.solutions)
            self.solution_label.config(text=f"Nghiệm: {self.current_index + 1} / {total}")
            self.update_nav_buttons()
            
            if self.auto_play_running:
                self.auto_id = self.root.after(800, self.auto_play_next)
    
    def auto_play_next(self):
        """Tự động chuyển sang nghiệm tiếp theo"""
        if self.auto_play_running:
            if self.current_index < len(self.solutions) - 1:
                self.next_solution()
            else:
                self.current_index = -1
                self.next_solution()
    
    def toggle_auto_play(self):
        """Bật/tắt chế độ tự động"""
        if not self.solutions or len(self.solutions) <= 1:
            return
        
        if self.auto_play_running:
            self.stop_auto_play()
        else:
            self.start_auto_play()
    
    def start_auto_play(self):
        """Bắt đầu chế độ tự động"""
        self.auto_play_running = True
        self.auto_btn.config(text="⏸ DỪNG", bg="#e67e22")
        self.prev_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.DISABLED)
        self.auto_id = self.root.after(800, self.auto_play_next)
    
    def stop_auto_play(self):
        """Dừng chế độ tự động"""
        if self.auto_id:
            self.root.after_cancel(self.auto_id)
            self.auto_id = None
        self.auto_play_running = False
        self.auto_btn.config(text="▶ TỰ ĐỘNG", bg="#f39c12")
        total = len(self.solutions)
        if total > 1:
            self.prev_btn.config(state=tk.NORMAL)
            self.next_btn.config(state=tk.NORMAL)
    
    def update_nav_buttons(self):
        """Cập nhật trạng thái nút điều hướng"""
        if not self.solutions:
            return
        total = len(self.solutions)
        self.prev_btn.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL if self.current_index < total - 1 else tk.DISABLED)


# ==================== CHẠY CHƯƠNG TRÌNH ====================
if __name__ == "__main__":
    root = tk.Tk()
    app = EightQueensGUI(root)
    root.mainloop()