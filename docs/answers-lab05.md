# Câu hỏi thảo luận — Lab 05

## 1. Vì sao ở Phần A chưa gắn tag v1.1.0 ngay khi tạo `release/lab05`? Nếu đã gắn rồi thì bây giờ phải phát hành v1.1.1? (Slide 60)
- **Quy tắc SCM**: *"Tag đã chia sẻ thì không xóa, không di chuyển"*. Tag đại diện cho một mốc phát hành bất biến (immutable baseline).
- Khi tạo nhánh `release/lab05`, phiên bản chưa chính thức giao cho người dùng mà vẫn đang trong quá trình kiểm toán và kiểm thử đóng gói. Việc chưa gắn tag giúp ta linh hoạt đưa các bản vá (hotfix phát hiện từ bản cũ) vào nhánh release trước khi chốt phát hành.
- Nếu đã gắn tag `v1.1.0` từ đầu, khi đưa hotfix vào, ta không thể di chuyển tag `v1.1.0` sang commit mới, mà bắt buộc phải phát hành phiên bản vá lỗi tiếp theo là `v1.1.1` theo chuẩn SemVer.

---

## 2. Ưu, nhược điểm của Upstream First (Microsoft Release Flow) so với Release First (Release Flow học phần) (Slide 64)

### Mô hình Upstream First (Microsoft):
- **Cơ chế**: Luôn sửa lỗi trên nhánh chính (`master`) trước, sau đó cherry-pick bản vá sang các nhánh `release/*` đang cần hỗ trợ.
- **Ưu điểm**:
  - Đảm bảo bug không bao giờ bị bỏ quên trên `master` (ngăn chặn lỗi xuất hiện trở lại ở các bản phát hành tương lai - avoid regression).
  - Quy trình đồng nhất: Mọi thay đổi đều bắt đầu từ một nơi duy nhất.
- **Nhược điểm**:
  - Khi cần phát hành hotfix khẩn cấp cho production, bản sửa lỗi phải đi qua quy trình kiểm duyệt trên `master` (nơi có thể đang chứa nhiều mã mới chưa ổn định) trước khi được đưa về nhánh release.

### Mô hình Release First (Học phần IT3180):
- **Cơ chế**: Tạo nhánh hotfix trực tiếp từ nhánh release bị lỗi (`release/lab04`), kiểm thử trên môi trường release, merge vào release và phát hành bản vá ngay, sau đó mới cherry-pick về `master` và các nhánh release khác.
- **Ưu điểm**:
  - Tốc độ phát hành bản vá cực nhanh cho phiên bản đang chạy trong thực tế mà không bị phụ thuộc vào tiến độ của master.
- **Nhược điểm**:
  - Nếu thiếu quy trình kiểm toán cấu hình chặt chẽ, lập trình viên rất dễ quên lan truyền bản vá ngược về `master` hoặc các dòng release song song khác.

---

## 3. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện? (Slide 64)
1. **Lệnh kiểm tra hành vi (Bash loop)**:
   ```bash
   for ref in v1.0.1 v1.1.0 master; do
       git switch --detach -q $ref; printf "%-8s " $ref
       python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
       print(len(search_by_title([D('The Lion King')], 'lion')))"
   done; git switch -q master
   ```
   Nếu quên lan truyền sang `release/lab05` (hoặc `v1.1.0`), kết quả in ra tại dòng `v1.1.0` sẽ là `0` thay vì `1`.

2. **Lệnh kiểm toán commit cherry-pick**:
   ```bash
   git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"
   ```
   Nếu quên, lệnh này sẽ chỉ trả về 1 commit (trên `master`) thay vì đủ 2 commit (trên `master` và `release/lab05`).

3. **Lệnh so sánh cherry giữa các nhánh**:
   ```bash
   git cherry -v origin/master origin/release/lab05
   ```
   Hoặc `git diff release/lab05 master -- aims/search.py` sẽ hiển thị sự khác biệt trong mã nguồn của hàm `search_by_title`.
