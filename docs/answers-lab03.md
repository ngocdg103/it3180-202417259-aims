# Câu hỏi thảo luận — Lab 03

## 1. Merge base là gì? (Slide 43)
- **Định nghĩa**: *Merge base* là tổ tiên chung gần nhất (lowest common ancestor) của hai hoặc nhiều nhánh trong đồ thị commit của Git.
- **Vai trò trong giải quyết xung đột**:
  - Khi thực hiện lệnh merge, Git sử dụng thuật toán 3-way merge dựa trên 3 mốc: (1) phiên bản tại `merge base`, (2) phiên bản ở đỉnh nhánh hiện tại (`HEAD`), và (3) phiên bản ở đỉnh nhánh muốn gộp vào (`branch to merge`).
  - Git so sánh cả hai nhánh với `merge base` để xác định bên nào có sự thay đổi. Nếu cả hai nhánh cùng sửa đổi cùng một dòng code so với `merge base`, Git sẽ đánh dấu là một xung đột (merge conflict) để người lập trình viên tự giải quyết.
- Lệnh tìm merge base: `git merge-base <branch1> <branch2>`.

---

## 2. Vì sao trên các nhánh `master` và `release/*` bắt buộc phải dùng `git revert` thay vì `git reset`? (Slide 43)
- **Cơ chế khác biệt**:
  - `git reset`: Dời con trỏ nhánh lùi về quá khứ và **xóa bỏ** các commit khỏi lịch sử nhánh, làm thay đổi lịch sử commit đã được chia sẻ.
  - `git revert`: **Tạo một commit mới** có nội dung đảo ngược hoàn toàn những thay đổi do commit trước đó tạo ra mà vẫn giữ nguyên vẹn toàn bộ chuỗi lịch sử commit.
- **Nguyên nhân bắt buộc dùng revert trên nhánh chung**:
  - Các nhánh `master` và `release/*` là các nhánh công khai đã được push lên GitHub và chia sẻ cho cả nhóm/cộng đồng.
  - Nếu dùng `git reset` rồi `push --force`, lịch sử trên remote sẽ bị viết lại. Khi các thành viên khác pull về sẽ gặp lỗi nghiêm trọng về cấu hình và xung đột lịch sử (divergent branches).
  - Sử dụng `git revert` đảm bảo nguyên tắc bảo toàn lịch sử cấu hình (audit trail) trong SCM, giúp truy vết rõ ràng ai đã hủy bỏ thay đổi nào, vào lúc nào và vì lý do gì.
