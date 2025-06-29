# Hướng Dẫn Chơi Game Knight's Tour

## Giới Thiệu
Knight's Tour là một trò chơi cờ vua cổ điển nơi bạn điều khiển một quân mã (knight) di chuyển trên bàn cờ kích thước tùy chọn (từ 5x5 đến 20x20). Mục tiêu là đưa quân mã ghé thăm tất cả các ô trên bàn cờ đúng một lần, bắt đầu từ ô do bạn chọn.

## Cách Chơi

### 1. Khởi Động Trò Chơi
- Khi mở chương trình, bạn sẽ thấy màn hình khởi đầu với nền ảnh và một panel điều khiển.
- Nhập kích thước bàn cờ (một số nguyên từ 5 đến 20) vào ô nhập liệu "Board size (5–20)".
- Nhấn nút **START** để bắt đầu trò chơi.

### 2. Chọn Ô Bắt Đầu
- Sau khi nhập kích thước và nhấn **START**, bạn sẽ thấy một bàn cờ với các ô màu xen kẽ.
- Nhấp chuột trái vào bất kỳ ô nào trên bàn cờ để chọn ô bắt đầu cho quân mã. Đây sẽ là điểm xuất phát của hành trình.

### 3. Theo Dõi Hành Trình
- Sau khi chọn ô bắt đầu, quân mã (ký hiệu "♞") sẽ tự động di chuyển theo thuật toán Warnsdorff.
- Mỗi ô được ghé thăm sẽ hiển thị số thứ tự (bắt đầu từ 1) bằng màu đỏ, cho thấy thứ tự di chuyển.
- Quá trình di chuyển diễn ra tự động với tốc độ có thể điều chỉnh.

### 4. Điều Chỉnh Tốc Độ và Tạm Dừng
- Bên phải bàn cờ, có một thanh trượt **Animation speed (ms)** để điều chỉnh tốc độ di chuyển (từ 50ms đến 500ms).
- Nhấn nút **Pause** để tạm dừng hành trình; nhấn lại (chuyển thành **Resume**) để tiếp tục.
- Thanh **Move counter** hiển thị số nước đi hiện tại (ví dụ: "Move: 5/64" với bàn 8x8).
- Thanh **Timer** hiển thị thời gian đã trôi qua kể từ khi bắt đầu (đơn vị giây).

### 5. Kết Thúc Trò Chơi
- Nếu quân mã ghé thăm tất cả các ô (tổng số ô = kích thước bàn cờ x kích thước bàn cờ), trò chơi sẽ kết thúc.
- Một màn hình **You Win!** sẽ xuất hiện, hiển thị:
  - Số nước đi (tổng số ô).
  - Thời gian hoàn thành (tính bằng giây).
  - Hướng dẫn nhấp **Play Again** để chơi lại hoặc **Exit Game** để thoát.

### 6. Tùy Chọn Thêm
- Từ menu **Game** trên thanh menu, bạn có thể chọn:
  - **New Game** để khởi động lại trò chơi từ đầu.
  - **Exit** để thoát chương trình.

## Lưu Ý
- Nếu không tìm được giải pháp từ ô bắt đầu, một thông báo lỗi sẽ xuất hiện, và bạn có thể thử lại với ô khác.
- Tốc độ di chuyển có thể ảnh hưởng đến trải nghiệm; hãy điều chỉnh để phù hợp.
- Trò chơi sử dụng thuật toán Warnsdorff, đảm bảo hiệu quả nhưng không phải lúc nào cũng thành công với mọi ô bắt đầu.

## Mẹo Chơi
- Chọn ô ở trung tâm bàn cờ (ví dụ: ô (4,4) trên bàn 8x8) để tăng cơ hội thành công.
- Điều chỉnh tốc độ chậm (giá trị lớn hơn) nếu muốn quan sát rõ hơn từng nước đi.

Chúc bạn chơi vui vẻ và khám phá hết các thử thách của Knight's Tour!