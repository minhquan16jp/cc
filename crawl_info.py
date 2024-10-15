import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Đường dẫn tới ChromeDriver
CHROME_DRIVER_PATH = './chromedriver'  # Thay đường dẫn thực tế đến ChromeDriver

# Hàm khởi tạo Selenium và lấy thông tin từ trang web
def crawl_info():
    # Tạo một đối tượng Service cho ChromeDriver
    service = Service(CHROME_DRIVER_PATH)
    
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome(service=service)
    
    # URL trang cần crawl
    url = 'https://dmobile.vn/thay-man-hinh-samsung-s34-ultra'
    
    # Mở trang web
    driver.get(url)

    try:
        # Chờ trang web và JavaScript tải hoàn toàn, tối đa 20 giây
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "demo12"))
        )
        
        # Lấy nội dung từ phần tử sau khi JavaScript đã chạy
        info = element.text
        print("Nội dung thẻ demo12:", info)
        
        # Ghi nội dung vào file text
        with open("output.txt", "w") as f:
            f.write("Nội dung thẻ demo12: " + info)
        
    except Exception as e:
        print("Đã xảy ra lỗi:", str(e))
    
    finally:
        # Đóng trình duyệt
        driver.quit()

# Gọi hàm crawl khi chạy script
if __name__ == "__main__":
    crawl_info()
