import requests
from bs4 import BeautifulSoup

url = 'https://www.24h.com.vn/'
# Gửi yêu cầu GET đến trang web
response = requests.get(url)
# Kiểm tra nếu yêu cầu thành công
if response.status_code == 200:
    # Tạo đối tượng BeautifulSoup để phân tích trang HTML
    # html.parser là parser tích hợp sẵn của Python dùng để phân tích cấu trúc tài liệu HTML hoặc XML.
    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm tất cả các tiêu đề bài viết là thẻ a thông qua thuộc tính class
    titles = soup.find_all('a', attrs={'class': 'd-block fw-medium color-main hover-color-24h'})


    # In ra các tiêu đề
    index = 0
    for title in titles:
        # 'strip=True' để xóa các khoảng trắng đầu và cuối
        print(index, ': ', title.get_text(strip=True))
        index += 1
else:
    print('Không thể lấy dữ liệu từ trang web.')
