# Knight's Tour - Thuật Toán và Cách Chạy

## Giới Thiệu
Dự án này triển khai thuật toán Knight's Tour (Hành Trình Quân Mã) trên bàn cờ kích thước tùy chọn (từ 5x5 đến 20x20) bằng Python. Thuật toán sử dụng phương pháp quay lui kết hợp với heuristic Warnsdorff để tìm đường đi, cho phép quân mã ghé thăm mỗi ô đúng một lần, bắt đầu từ ô do người dùng chọn.

## Thuật Toán
- **Phương pháp:** Quay lui (Backtracking) với heuristic Warnsdorff.
- **Cơ chế:**
  - Khởi tạo bàn cờ với tất cả ô bằng 0 (chưa ghé thăm).
  - Từ ô bắt đầu, thử tất cả 8 nước đi có thể của quân mã (hình chữ "L": 2 ô theo một hướng và 1 ô vuông góc).
  - Sử dụng heuristic Warnsdorff để ưu tiên nước đi đến ô có ít nước đi tiếp theo nhất, giảm nguy cơ bị kẹt.
  - Đánh dấu ô đã ghé thăm bằng số thứ tự (1, 2, ..., n²) và quay lui nếu không tìm được giải pháp.
- **Điều kiện thắng:** Quân mã ghé thăm tất cả n² ô trên bàn cờ.

## Các Tệp Trong Dự Án
- `knight_tour_app.py`: Mã nguồn chính của ứng dụng với giao diện Tkinter.
- `Knight_Tour_Guide.md`: Hướng dẫn chi tiết cách chơi trò chơi.
- `start_bg.png`: Hình nền cho màn hình khởi đầu (tùy chọn, cần đặt trong cùng thư mục).
- `algorithm.cpp`: Triển khai thuật toán bằng C++ (tham khảo).
- `README.md`: Tài liệu này.

## Yêu Cầu Hệ Thống
- Python 3.x
- Thư viện:
  - `tkinter` (thường đi kèm với Python)
  - `PIL` (Python Imaging Library/Pillow): Cài đặt bằng `pip install Pillow`

## Cách Chạy
1. **Cài đặt môi trường:**
   - Đảm bảo Python 3.x đã được cài đặt trên máy.
   - Cài đặt Pillow nếu chưa có: mở terminal và chạy `pip install Pillow`.

2. **Chuẩn bị tệp:**
   - Đặt tất cả các tệp (`knight_tour_app.py`, `Knight_Tour_Guide.md`, `start_bg.png`, v.v.) trong cùng một thư mục.
   - Nếu không có `start_bg.png`, chương trình sẽ hiển thị lỗi và thoát; bạn có thể thay thế bằng hình ảnh khác hoặc bỏ qua bằng cách sửa mã.

3. **Chạy chương trình:**
   - Mở terminal, điều hướng đến thư mục chứa dự án.
   - Chạy lệnh: `python knight_tour_app.py`.
   - Chương trình sẽ mở một cửa sổ giao diện.

4. **Thao tác:**
   - Nhập kích thước bàn cờ (5-20) trên màn hình khởi đầu và nhấn **START**.
   - Nhấp chuột trái vào ô bất kỳ trên bàn cờ để bắt đầu.
   - Quan sát quân mã di chuyển tự động, điều chỉnh tốc độ bằng thanh trượt, và tạm dừng bằng nút **Pause**.

5. **Kết thúc:**
   - Khi hoàn thành, màn hình **You Win!** sẽ hiển thị với số nước đi và thời gian.
   - Chọn **Play Again** để chơi lại hoặc **Exit Game** để thoát.
   - Dùng menu **Game > New Game** để khởi động lại hoặc **Exit** để thoát.

## Lưu Ý
- Nếu không tìm được giải pháp, thông báo lỗi sẽ xuất hiện; thử lại với ô khác.
- Tốc độ di chuyển có thể điều chỉnh (50ms đến 500ms) để phù hợp với trải nghiệm.
- Dự án sử dụng thuật toán Warnsdorff, không đảm bảo giải pháp cho mọi ô bắt đầu.

## Cải Tiến Tiềm Năng
- Thêm hiệu ứng âm thanh hoặc hình ảnh con mã thực tế.
- Tích hợp giao diện web bằng Flask hoặc Django.
- Tối ưu thuật toán bằng cách kết hợp thêm heuristic khác.

Chúc bạn thành công khi khám phá và chạy thuật toán Knight's Tour!