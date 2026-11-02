# Câu hỏi thảo luận — Lab 02

## 1. Vì sao phải đồng bộ master trước khi gửi PR? (Slide 35)
- Trong môi trường phát triển song song nhiều nhánh, nhánh `master` liên tục tiến về phía trước do các PR khác đã được merge trước đó.
- Việc đồng bộ nhánh làm việc với `master` mới nhất (thông qua `git merge origin/master` hoặc `git rebase origin/master`) giúp:
  - Kiểm thử và phát hiện sớm xung đột tích hợp (merge conflicts) ngay tại môi trường phát triển của lập trình viên, thay vì để xung đột xảy ra trên GitHub khi merge PR.
  - Chạy lại toàn bộ test suite cục bộ để đảm bảo mã mới không làm vỡ các tính năng vừa được merge vào master (kiểm tra tính toàn vẹn tích hợp).
  - Giúp reviewer duyệt PR dễ dàng và việc merge diễn ra trơn tru.

---

## 2. Khi nào không được dùng `rebase`? (Slide 35)
- **Quy tắc vàng của Rebase (The Golden Rule of Rebase)**: *Tuyệt đối không rebase các commit đã được công khai hoặc chia sẻ với người khác* (ví dụ nhánh `master`, `release/*`, hoặc nhánh nhóm đang cùng làm việc).
- **Lý do**: Lệnh `rebase` viết lại toàn bộ lịch sử commit bằng cách tạo ra các mã băm SHA mới cho các commit được dời. Nếu rebase trên nhánh chung, các lập trình viên khác sẽ có lịch sử không nhất quán, dẫn đến tình trạng conflict hàng loạt khi kéo code (pull) về.
- Chỉ nên rebase trên nhánh cục bộ (local private branch) của bản thân trước khi push/tạo PR.

---

## 3. Nhánh `feature/*` khác nhánh `topic/*` ra sao? (Slide 35)
- **Nhánh `feature/*`**:
  - Dùng để phát triển một chức năng nghiệp vụ cụ thể cho người dùng cuối của phần mềm (ví dụ: `feature/cart-print`, `feature/sort-cart`, `feature/discount`).
  - Phạm vi thay đổi thường liên quan trực tiếp đến logic mã nguồn ứng dụng.
- **Nhánh `topic/*`**:
  - Dùng cho các chủ đề ngắn hạn, công việc phụ trợ hoặc cấu hình dự án, tài liệu, quy trình CI/CD (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/ci-unit-tests`, `topic/prepare-release-1.0.0`).
  - Phạm vi thường là tài liệu, quy ước mẫu, cấu hình công cụ quản lý cấu hình thay vì tính năng nghiệp vụ.
