# Notepad with Chatbot Integration and Identify text from photos

## Giới thiệu
Đây là một ứng dụng notepad đơn giản được tích hợp với một chatbot sử dụng OpenAI API. Ứng dụng cho phép người dùng viết và lưu trữ ghi chú cũng như tương tác với một trợ lý ảo để nhận được câu trả lời tự nhiên trên các câu hỏi và yêu cầu. Ứng dụng cũng cung cấp khả năng nhận diện văn bản từ ảnh và đưa ra màn hình cho người sử dụng
Bạn có thể tải ứng dụng cho Macos [tại đây](https://drive.google.com/file/d/1jr3OzMJ-7vhLfysFtpeODii14OOy9bsl/view?usp=sharing)

## Cài đặt
### Yêu cầu
Python 3.x
PyQt5
OpenAI Python SDK

### Cài đặt PyQt5
```
pip install PyQt5
```
### Cài đặt OpenAI Python SDK
```
pip install openai
```
### Cài đặt PyEnchant
```
pip install pyenchant
```
### Cài đặt pydub
```
pip install pydub
```
### Cài đặt ffmpeg
Tải ffmped [tại đây](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) và giải nén

Sau đó sao chép vđịa chỉ path của tệp bin trong forder đã giải nén và vào thanh tìm kiếm và mở Edit the System environment variables, sau đó mở Environment Variables 

Ở phần System Varibles, nhấn mục Path và nhấn Edit, sau đó nhấn New và thêm địa chỉ Path của tệp bin đã sao chép và nhấn ok để hoàn thành
### Cài đặt Google Translate
```
pip install googletrans==4.0.0-rc1
```
## Thiết lập OpenAI API Key

Trước khi sử dụng ứng dụng, bạn cần có một API key từ OpenAI. Bạn có thể đăng ký [tại đây](https://platform.openai.com/api-keys).

Sau khi có API key, hãy thay đổi giá trị YOUR_OPENAI_API_KEY trong file main.py với API key của bạn.

## Sử dụng

### Chạy ứng dụng bằng lệnh sau:
```
python app.py
```
Viết văn bản trong ô soạn thảo ở phía trên.

Nhập câu hỏi hoặc yêu cầu của bạn vào ô chat ở phía dưới.

Nhấn Enter hoặc nhấp vào nút "Send" để gửi tin nhắn và nhận câu trả lời từ trợ lý ảo.


## Tính năng mở rộng

Có hầu hết các tính năng có trong một NotePad đơn giản và có thêm các tính năng đặc biệt như chatbot và nhận diện ảnh

Cải thiện giao diện người dùng và trải nghiệm người dùng.

Tích hợp với các dịch vụ trợ lý ảo khác như Dialogflow, Alexa, hoặc Microsoft Bot Framework.


## Tác giả
Được phát triển bởi [Team-28-Software-Engineering].


## Bản quyền
Ứng dụng được phân phối dưới giấy phép [tên giấy phép, ví dụ: MIT License]. Xem tệp LICENSE để biết chi tiết.
