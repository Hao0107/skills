# Detailed Guidelines & Domain Rules

Tài liệu này chứa các quy tắc chi tiết, chỉ được Agent nạp vào bộ nhớ khi thực thi tới Bước 2 của `SKILL.md`.

## 1. Tiêu chuẩn đánh giá (Evaluation Criteria)
- **Rule A (`[Tên quy tắc 1]`):**
  - Điều kiện đạt (`PASS`): [Mô tả ngưỡng hoặc điều kiện hợp lệ].
  - Điều kiện lỗi (`FAIL`): [Mô tả trường hợp vi phạm].
- **Rule B (`[Tên quy tắc 2]`):**
  - Điều kiện đạt (`PASS`): [Mô tả ngưỡng hoặc điều kiện hợp lệ].
  - Điều kiện lỗi (`FAIL`): [Mô tả trường hợp vi phạm].

## 2. Xử lý các trường hợp ngoại lệ (Edge Cases)
- **Trường hợp 1:** Nếu dữ liệu đầu vào rỗng -> Trả về trạng thái `SKIPPED` và thông báo rõ lý do.
- **Trường hợp 2:** Nếu phát hiện xung đột cấu hình -> Ưu tiên cấu hình trong project hiện tại hơn cấu hình mặc định.

## 3. Quy ước đặt tên & Định dạng (Conventions)
- Mọi file sinh ra tự động phải có hậu tố `.[loại_file]` và lưu tại thư mục `[đường_dẫn_đầu_ra]`.