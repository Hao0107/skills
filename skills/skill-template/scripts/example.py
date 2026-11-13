#!/home/anhhao/miniconda3/envs/py311/bin/python
"""
Template chuẩn cho script thực thi trong Agent Skill.
- Nhận tham số rõ ràng qua argparse.
- Đẩy lỗi ra stderr kèm exit code != 0 để Agent nhận biết khi thất bại.
- Trả kết quả chuẩn hóa dạng JSON ra stdout để Agent đọc trong 1 lượt.
"""
import argparse
import json
import sys
from pathlib import Path


def process_target(input_path: Path, option: str) -> dict:
    # 1. Kiểm tra đầu vào hợp lệ
    if not input_path.exists():
        print(f"[ERROR] Target path not found: '{input_path}'", file=sys.stderr)
        sys.exit(1)

    # 2. Đặt logic xử lý cốt lõi của bạn tại đây
    # (Ví dụ: parse file, gọi API nội bộ, kiểm tra cú pháp, tính toán...)
    try:
        result_data = {
            "target": str(input_path),
            "applied_option": option,
            "details": "Replace this with actual processed data"
        }
    except Exception as exc:
        print(f"[ERROR] Processing failed: {exc}", file=sys.stderr)
        sys.exit(2)

    return {
        "status": "success",
        "data": result_data
    }


def main():
    parser = argparse.ArgumentParser(
        description="Deterministic helper script for skill-template."
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the input file or directory."
    )
    parser.add_argument(
        "--option", "-o",
        default="default",
        help="Optional configuration parameter."
    )
    args = parser.parse_args()

    output = process_target(Path(args.input), args.option)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()