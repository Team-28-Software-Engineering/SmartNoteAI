# SmartNoteAI

## Giới thiệu
Đây là một ứng dụng notepad đơn giản được tích hợp với một chatbot sử dụng OpenAI API và các tính năng thú vị như nhận diện văn bản từ ảnh và nhận diện văn bản từ âm thanh. Ứng dụng cho phép người dùng viết và lưu trữ ghi chú cũng như tương tác với một trợ lý ảo để nhận được câu trả lời tự nhiên trên các câu hỏi và yêu cầu. Ứng dụng cung cấp khả năng nhận diện văn bản từ ảnh và nhận diện văn bản từ âm thanh và đưa ra màn hình cho người sử dụng.

Vào trang web này để xem giới thiệu và tải phần mềm này về
https://smartnoteai-68f02.web.app/


## Download for macos
Bạn có thể tải ứng dụng cho Macos [tại đây](https://drive.google.com/file/d/1eYQvJyxWkRRR-GYn87hw_L6tQkt6YNwo/view?usp=sharing)

## Cài đặt
### Yêu cầu
Cài đặt các thư viện cần thiết
```
pip install -r requirements.txt
```
### Cài đặt ffmpeg
Vì ffmpeg không thể cài đặt trực tiếp bằng lệnh pip trên window, bạn cần thực hiện theo các bước sau nếu muốn chương trình không xảy ra lỗi khi chạy
Tải ffmped [tại đây](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) và giải nén

Sau đó sao chép vđịa chỉ path của tệp bin trong forder đã giải nén và vào thanh tìm kiếm và mở Edit the System environment variables, sau đó mở Environment Variables 

Ở phần System Varibles, nhấn mục Path và nhấn Edit, sau đó nhấn New và thêm địa chỉ Path của tệp bin đã sao chép và nhấn ok để hoàn thành
Nếu bạn dùng macos có thể cài đặt bằng homebrew trên terminal

## Thiết lập OpenAI API Key

Nếu bạn muốn sử dụng tính năng chatbot(chat với chatgpt) của chúng tôi, bạn cần có một API key từ OpenAI. Bạn có thể lấy API của tài khoản của bạn [tại đây](https://platform.openai.com/api-keys).

Sau khi có API key, hãy nhập nó vào phần Nhập API_KEY khi bạn kích hoạt tính năng chatbot

## Sử dụng

### Chạy ứng dụng bằng lệnh sau:
```
python app.py
```

## Tính năng mở rộng

Có hầu hết các tính năng có trong một NotePad đơn giản và có thêm các tính năng đặc biệt như chatbot, nhận diện ảnh và nhận diện giọng nói

Cải thiện giao diện người dùng và trải nghiệm người dùng.

Tích hợp với các dịch vụ trợ lý ảo khác như Dialogflow, Alexa, hoặc Microsoft Bot Framework.


## Tác giả
Được phát triển bởi [Team-28-Software-Engineering].
