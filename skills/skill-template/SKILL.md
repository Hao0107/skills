---
name: skill-template
description: Mô tả chức năng chính của skill trong 1 câu. Sử dụng khi người dùng yêu cầu [liệt kê 2-3 tình huống/từ khóa kích hoạt cụ thể]. KHÔNG sử dụng khi [nêu trường hợp ngoại lệ dễ nhầm lẫn với skill khác].
license: MIT
compatibility: Antigravity CLI, Claude Code
metadata:
  author: anhhao
  version: "1.0.0"
---

# [Tên Hiển Thị Của Skill]

## 1. Objective (Mục tiêu)
- **Đầu vào (Input):** [Mô tả dữ liệu, đường dẫn file, hoặc tham số người dùng sẽ cung cấp].
- **Nhiệm vụ (Process):** [Tóm tắt ngắn gọn công việc cốt lõi mà skill này giải quyết].
- **Đầu ra (Deliverable):** [Kết quả cuối cùng trả về: file mới, báo cáo JSON, hay đoạn code đã tối ưu].

## 2. Prerequisites & Context Check (Kiểm tra điều kiện)
Trước khi bắt đầu, thực hiện kiểm tra nhanh:
- Xác nhận các file/thư mục mục tiêu có tồn tại trong workspace hay không.
- Nếu thiếu thông tin quan trọng (ví dụ: `[tên_tham_số_bắt_buộc]`), dừng lại và hỏi người dùng ngay lập tức.

## 3. Execution Workflow (Quy trình thực thi)
Thực hiện tuần tự các bước sau:

1. **Bước 1 — Thu thập & Xử lý tự động (Run Script):**
  Gọi script hỗ trợ để lấy dữ liệu chính xác (thay `<skill_dir>` bằng đường dẫn tới thư mục skill này):
  ```bash
  python3 <skill_dir>/scripts/run_task.py --input "<target_path>"

2. **Bước 2 — Tra cứu quy chuẩn (Load References):**
  Đọc file references/guidelines.md để nắm các quy tắc nghiệp vụ và tiêu chuẩn đánh giá.

3. **Bước 3 — Tổng hợp & Định dạng đầu ra (Format Output):**
  Dựa trên kết quả từ Bước 1 và quy tắc ở Bước 2, tạo kết quả cuối cùng tuân thủ đúng cấu trúc mẫu tại assets/output-schema.json.
  
4. **Bước 4 — Kiểm chứng (Verification):**
  Kiểm tra lại kết quả đầu ra xem đã đáp ứng đủ các tiêu chí trong references/guidelines.md chưa trước khi phản hồi cho người dùng.