# LAB — Adversarial Search: Minimax, Alpha-Beta, Heuristic & MCTS

*Intro to AI — Tuần 8. Thời lượng: ~2.5–3 giờ tại lớp. Làm bài chạy tay (không lập trình).*

## Quy ước chung

- Nút **▲ MAX** lấy **max** các con; nút **▼ MIN** lấy **min** các con. Giá trị ở lá là điểm cho MAX.
- Alpha-Beta duyệt **trái → phải**; cắt khi **α ≥ β** (nút MIN cắt khi v ≤ α; nút MAX cắt khi v ≥ β).
- **Luật vàng:** "MAX nuôi α, MIN nuôi β"; v cùng loại với nút (MAX→max từ −∞, MIN→min từ +∞).

**Thang điểm:** Câu 1: 30 · Câu 2: 25 · Câu 3: 25 · Câu 4: 20. (Các ý ★ là điểm thưởng.)

---

## Câu 1 — Minimax & Alpha-Beta trên cây (30đ)

Với **mỗi cây**: (1) tìm giá trị các nút và giá trị gốc bằng **Minimax**, cho biết nước đi tốt nhất của MAX; (2) chạy **Alpha-Beta** (trái→phải), **ghi α/β/v tại mỗi nút** và **liệt kê các lá bị cắt**.

**Câu 1a — cây 3 tầng:**

![Câu 1a](lab_images/p1_treeA_problem.png)

**Câu 1b — cây 4 tầng (có số âm):**

![Câu 1b](lab_images/p1_treeB_problem.png)

**Câu 1c — cây KHÔNG ĐỀU (nhiều tầng, phân nhánh khác nhau, lá ở nhiều độ sâu):**

Lưu ý: một số **lá nằm ngay ở tầng trên** (ví dụ giá trị 16, 12 là con trực tiếp của nút MIN). Khi tính, cứ dùng loại nút (MAX/MIN) theo tầng, và lá là giá trị cuối bất kể độ sâu.

![Câu 1c](lab_images/p1c_irregular_problem.png)

**★ Câu 1d (thưởng 5đ):** Với cây 1a, chỉ ra thứ tự duyệt các nhánh giúp Alpha-Beta **cắt nhiều nhất** và **ít nhất**; nêu độ phức tạp tốt nhất/tệ nhất.

---

## Câu 2 — Mô hình hóa game thật thành cây và giải (25đ)

### Câu 2a — Coin-row game (15đ)

**Luật:** một dãy đồng xu. Hai người **luân phiên**, mỗi lượt lấy **một xu ở đầu trái hoặc đầu phải** của dãy còn lại. Mỗi người muốn **tối đa tổng mệnh giá mình lấy**. Người đi trước là **MAX**. Quy ước **UTILITY = (tổng MAX) − (tổng MIN)**.

![Câu 2a](lab_images/p2_coinrow_problem.png)

1. (5đ) Mô hình hóa **6 thành phần**: S₀, PLAYER, ACTIONS, RESULT, TERMINAL-TEST, UTILITY.
2. (7đ) **Vẽ toàn bộ cây**, điền UTILITY ở lá; chạy **Minimax**: giá trị gốc và **nước đi đầu tối ưu**.
3. (3đ) Chiến lược **tham lam** (luôn lấy đầu lớn hơn) cho kết quả gì? Vì sao **không** tối ưu?

### Câu 2b — Nim (10đ)

**Luật:** có **5 viên sỏi**. Hai người luân phiên, mỗi lượt lấy **1 hoặc 2 viên**; **ai lấy viên cuối cùng thì THẮNG**. Người đi trước là **MAX**. Quy ước **UTILITY = +1 nếu MAX thắng, −1 nếu MIN thắng**.

1. (4đ) Mô hình hóa **6 thành phần** cho trò chơi này.
2. (4đ) **Vẽ cây trò chơi** (mỗi nút ghi số viên còn lại; cạnh ghi số viên lấy), điền UTILITY ở lá; chạy **Minimax** tìm giá trị gốc và **nước đi đầu tối ưu**.
3. (2đ) Người đi trước **thắng hay thua** nếu cả hai chơi tối ưu? (Gợi ý kiểm tra: các vị trí là **bội số của 3** viên là "thế thua" cho người sắp đi.)

---

## Câu 3 — Heuristic Alpha-Beta trên cờ vua (25đ)

Cây cờ vua quá lớn để duyệt tới hết ván, nên ta **tìm sâu 2 tầng rồi dừng** (Trắng đi → Đen đáp) và dùng **hàm đánh giá EVAL = chênh lệch chất (material)**: tổng giá trị quân Trắng − tổng giá trị quân Đen, với quy ước **Tốt (P) = 1, Mã (N) = Tượng (B) = 3, Xe (R) = 5, Hậu (Q) = 9**.

**Trắng đi (MAX).** Thế cờ hiện tại đang cân bằng chất (EVAL = 0):

![Câu 3](lab_images/p3c_chess_position.png)

Xét **3 nước ăn quân ứng viên** của Trắng; với mỗi nước, Đen có **2 đáp trả** (ăn lại / không ăn lại). Bảng diễn biến và EVAL ở mỗi thế cờ lá (sau 2 nước, tính theo *thay đổi* chất so với hiện tại):

| Nước Trắng | Đáp trả của Đen | Diễn biến | EVAL |
|------------|------------------|-----------|------|
| **A: Nxd5** (Mã ăn Tốt d5) | Đen không ăn lại được (Mã an toàn) | Trắng +1 Tốt | **+1** |
| **A: Nxd5** | Đen đi dở, mất thêm 1 Tốt | Trắng +2 Tốt | +2 |
| **B: Rxe7** (Xe ăn Tượng e7) | …Rxe7 (Xe Đen ăn lại) | +Tượng(3) − Xe(5) | **−2** |
| **B: Rxe7** | Đen không ăn lại | +Tượng(3) | +3 |
| **C: Bxc6** (Tượng ăn Mã c6) | …bxc6 (Tốt ăn lại) | +Mã(3) − Tượng(3) | **0** |
| **C: Bxc6** | Đen không ăn lại | +Mã(3) | +3 |

**Yêu cầu:**
1. (8đ) Vẽ cây tìm kiếm 2 tầng (Trắng-MAX → Đen-MIN → EVAL) và chạy **Minimax**: tìm giá trị mỗi nước, giá trị gốc và **nước đi tốt nhất** cho Trắng.
2. (10đ) Chạy **Alpha-Beta** (trái→phải): **ghi α/β/v tại mỗi nút** và liệt kê các lá bị cắt.
3. (4đ) Giải thích bằng ngôn ngữ cờ vua vì sao nước tối ưu lại tốt hơn hai nước còn lại (gợi ý: "ăn Tốt sạch" vs "mất chất" vs "đổi ngang").
4. (3đ) Vì sao phải dùng **cutoff + EVAL** thay vì duyệt tới hết ván? EVAL (đếm chất) là *ước lượng thô* — điều này ảnh hưởng gì tới tính tối ưu? Nêu ràng buộc UTILITY(thua) ≤ EVAL ≤ UTILITY(thắng).

---

## Câu 4 — Monte-Carlo Tree Search (chạy tay) (20đ)

Cho cây MCTS hiện tại (gốc R, ba nước A, B, C; mỗi nút ghi **w/n** = số ván thắng / số lượt):

![Câu 4](lab_images/p4_mcts_init.png)

### Định nghĩa hàm UCB (Upper Confidence Bound)

Khi ở bước **Selection**, mỗi nút con được chấm điểm bằng:

**UCB(nút) = w/n  +  C · √( ln N / n )**

trong đó: **w** = số ván thắng đã tích lũy qua nút; **n** = số lượt đã đi qua nút; **N** = số lượt của **nút cha**; **C** = hằng số khám phá (ở đây **C = √2 ≈ 1.414**).

- Số hạng **w/n** = *tỉ lệ thắng* → phần **khai thác** (ưu tiên nút đang tốt).
- Số hạng **C·√(ln N / n)** = phần **khám phá** (thưởng cho nút **ít được thử**, n nhỏ).
- Quy ước: nút chưa từng thăm (n = 0) có UCB = **+∞** (phải thăm trước). Selection luôn chọn nút có **UCB lớn nhất**.

**Luật phá hòa:** khi UCB bằng nhau, ưu tiên theo thứ tự chữ cái (A < B < C).
**Hằng số hỗ trợ tính tay:** ln 12 ≈ 2.485, ln 13 ≈ 2.565, ln 14 ≈ 2.639.
**Kết quả 3 ván mô phỏng cho sẵn** (playout vòng 1, 2, 3): **THẮNG, THẮNG, THẮNG**.

**Yêu cầu:**
1. (12đ) Thực hiện **3 vòng lặp** MCTS. Mỗi vòng: tính **UCB** cho A, B, C → **chọn** nút (Selection) → dùng kết quả playout cho sẵn (Simulation) → **cập nhật w/n** của nút được chọn và của gốc (Back-propagation). Ghi rõ w/n sau mỗi vòng.
2. (3đ) Sau 3 vòng, **nước đi nào** được chọn để đi thật? Dựa vào tiêu chí gì?
3. (3đ) **Giả định:** nếu playout **vòng 1 là THUA**, hãy tính lại UCB ở **vòng 2** và cho biết nút nào được chọn. Điều này minh họa tính chất gì của MCTS?
4. (2đ) Giải thích ý nghĩa hai số hạng trong công thức UCB (khai thác vs khám phá).

---

*Nộp: toàn bộ cây/bảng đã điền + lời giải. Nhớ ghi rõ bước tính α/β/v (Câu 1, 3) và UCB (Câu 4).*
