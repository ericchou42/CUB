from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 設置 ChromeDriver 路徑
chrome_driver_path = "你的/chromedriver/路徑"

# 設置 Chrome 瀏覽器選項
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # 全螢幕打開

# 啟動瀏覽器
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打開國泰世華銀行官網
url = "https://www.cathaybk.com.tw/cathaybk/"
driver.get(url)

# 等待網站完全加載
time.sleep(5)  # 可以根據網頁加載速度調整等待時間

# 截圖並保存
screenshot_path = "cathaybk_screenshot.png"
driver.save_screenshot(screenshot_path)
print(f"網站截圖已保存到: {screenshot_path}")

# 關閉瀏覽器
driver.quit()
