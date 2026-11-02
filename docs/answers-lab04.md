# Câu hỏi thảo luận — Lab 04

## 1. Vì sao chuẩn bị phát hành trên master trước mà không sửa trên nhánh release? (Slide 47)
- Nhánh `master` là "nguồn chân lý duy nhất" (Single Source of Truth) của dự án. Mọi thay đổi về phiên bản (`__version__`) và nhật ký thay đổi (`CHANGELOG.md`) cần được review và tích hợp chính thức vào master trước.
- Khi tạo nhánh `release/lab04` từ master sau khi đã chuẩn bị xong, nhánh release sẽ kế thừa ngay lập tức trạng thái hoàn chỉnh, sẵn sàng đóng gói và gắn tag mà không cần phải can thiệp thêm bất kỳ commit nào trên nhánh release.
- Tránh tình trạng nhánh release đi trước master, dẫn đến việc phải merge ngược từ release về master (vi phạm quy tắc của Release Flow).

---

## 2. Vì sao nhánh `release/*` không bao giờ merge ngược vào master? (Slide 52)
- Theo nguyên tắc Release Flow, master là nhánh luôn tiến về phía trước (fast-forward mindset).
- Việc merge cả nhánh `release/*` ngược vào master dễ tạo ra các vòng merge phức tạp (merge loops), mang theo những cấu hình hoặc thay đổi đặc thù của môi trường phát hành vào luồng phát triển chính.
- Trong trường hợp cần sửa lỗi khẩn cấp (hotfix) trên release, ta chỉ đưa commit sửa lỗi cần thiết về master bằng lệnh `git cherry-pick -x <FIX_SHA>` thông qua Pull Request, vừa giữ lịch sử master tuyến tính vừa đảm bảo truy vết chính xác.

---

## 3. So sánh mô hình Release Flow và GitFlow (Slide 52)

| Tiêu chí | Release Flow (rút gọn) | GitFlow |
|---|---|---|
| **Số nhánh chính vĩnh viễn** | 1 nhánh (`master`) | 2 nhánh (`main` và `develop`) |
| **Nhánh phát triển hàng ngày** | Tách từ `master` và gộp về `master` | Tách từ `develop` và gộp về `develop` |
| **Nhánh Release** | Tách từ `master`, đóng băng nộp bài/phát hành, không merge ngược lại | Tách từ `develop`, sau khi hoàn thiện merge vào cả `main` và `develop` |
| **Xử lý Hotfix** | Tạo từ `release/*`, vá rồi `cherry-pick` về `master` | Tạo từ `main`, vá xong merge vào cả `main` và `develop` |
| **Độ phức tạp & CI/CD** | Đơn giản, tinh gọn, rất phù hợp với CI/CD hiện đại | Khá cồng kềnh, dễ phát sinh xung đột khi merge 2 chiều |

---

## 4. Vì sao phiên bản này tăng lên `1.0.0` mà không phải là `0.4.0`? (Slide 52)
- Theo chuẩn đánh số phiên bản ngữ nghĩa (Semantic Versioning - SemVer: `MAJOR.MINOR.PATCH`):
  - Dòng phiên bản `0.y.z` (`v0.1.0` ... `v0.3.0` ở Lab 01–03) đại diện cho giai đoạn khởi tạo ban đầu, phần mềm còn đang trong giai đoạn thử nghiệm và API chưa ổn định.
  - Khi phần mềm đạt được tập tính năng cốt lõi hoàn chỉnh đầu tiên (First Production Release) sẵn sàng phát hành cho người dùng cuối sử dụng thực tế, số `MAJOR` được nâng lên `1.0.0`.
  - Việc lên `1.0.0` thể hiện một mốc cam kết về độ ổn định của API và độ tin cậy của sản phẩm.
