# your_error_checker_script.py

def check_errors():
    # Đây là nơi để thực hiện các kiểm tra lỗi của bạn
    # Ví dụ: Kiểm tra tất cả các file Python có syntax lỗi sử dụng pylint
    import os
    import subprocess

    files = [f for f in os.listdir('.') if f.endswith('.py')]
    for file in files:
        subprocess.run(['pylint', file])


if __name__ == "__main__":
    check_errors()