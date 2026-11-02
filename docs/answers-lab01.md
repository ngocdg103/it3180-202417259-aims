# Câu hỏi thảo luận — Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`? (Slide 19)
- **Vị trí lưu trữ**:
  - Cấu hình `--global` được lưu trong file `~/.gitconfig` (trên Windows thường nằm tại `C:\Users\<Tên_User>\.gitconfig`).
  - Cấu hình `--local` được lưu trong file `.git/config` nằm bên trong thư mục gốc của repository cụ thể.
- **Phạm vi áp dụng & Sự khác biệt**:
  - `--global`: Áp dụng cho tất cả các repository của người dùng hiện tại trên máy tính, trừ khi repository đó có cấu hình local ghi đè.
  - `--local`: Chỉ áp dụng riêng cho repository hiện tại. Có độ ưu tiên cao hơn `--global` (local overrides global). Ví dụ: có thể dùng `--local` để đặt email công việc cho một repo công ty mà không ảnh hưởng đến email cá nhân toàn cục.

---

## 2. Vì sao dùng `git mv` thay vì di chuyển tệp thủ công? (Slide 26)
- Khi dùng lệnh di chuyển file thông thường của hệ điều hành, Git ban đầu sẽ hiểu là thao tác **xóa file cũ (deleted)** và **tạo một file mới chưa được theo dõi (untracked)**.
- `git mv` thực hiện đồng thời hai việc: di chuyển file trên hệ thống tệp và tự động đưa thao tác đó vào Staging Area (index).
- Giúp Git theo dõi chính xác lịch sử thay đổi của tệp qua các lần đổi tên hoặc tái cấu trúc thư mục, bảo toàn chuỗi commit khi dùng `git log --follow <tệp>`.

---

## 3. `release/lab01` có phải baseline không? (Slide 26)
- **Có, `release/lab01` chính là một baseline**.
- Theo định nghĩa trong Quản lý cấu hình phần mềm (SCM): *Baseline (đường cơ sở)* là một phiên bản cấu hình đã được kiểm tra, thống nhất, được đóng băng và chỉ có thể thay đổi thông qua quy trình kiểm soát thay đổi chính thức (Change Control).
- Nhánh `release/lab01` (và tag `v0.1.0`) đánh dấu mốc hoàn thành bài nộp của Lab 01, đóng vai trò là baseline để các bài thực hành tiếp theo (Lab 02 trở đi) tiếp tục phát triển.

---

## 4. Vì sao không commit thẳng lên master dù chỉ làm việc một mình? (Slide 26)
- **Tuân thủ kỷ luật SCM & Release Flow**: Giúp hình thành thói quen chuyên nghiệp trong phát triển phần mềm chuẩn mực.
- **Bảo vệ nhánh master**: Luôn giữ nhánh master ở trạng thái ổn định, sạch sẽ, có thể triển khai (deployable) bất cứ lúc nào.
- **Kiểm soát thay đổi (Change Control)**: Mọi thay đổi đều được phân tách rõ ràng theo nhánh tính năng (`feature/*`), nhánh tái cấu trúc (`refactor/*`) hoặc sửa lỗi (`bugfix/*`).
- **Khả năng hoàn tác an toàn**: Nếu một tính năng có lỗi hoặc bị hủy bỏ, ta có thể dễ dàng hủy bỏ nhánh hoặc revert Pull Request tương ứng mà không làm ảnh hưởng đến các phần code khác trên master.
