skill-template/                          # Đổi tên thư mục này theo kebab-case (vd: my-new-skill)
├── SKILL.md                             # [1] File điều phối chính & Metadata định tuyến
├── scripts/                             # [2] Thư mục chứa code thực thi tự động
│   └── run_task.py                      # Script mẫu nhận input CLI và trả về JSON
├── references/                          # [3] Thư mục chứa tài liệu tra cứu chuyên sâu
│   └── guidelines.md                    # Quy tắc chi tiết, ngưỡng kiểm tra, kiến trúc
└── assets/                              # [4] Thư mục chứa khuôn mẫu đầu ra / cấu hình tĩnh
    └── output-schema.json               # Mẫu định dạng kết quả trả về