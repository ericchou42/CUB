from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 設置 ChromeDriver 路徑
chrome_driver_path = "/Users/ericchou/Desktop/ai-chat/CUB/chromedriver"

# 設置 Chrome 瀏覽器選項
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # 全螢幕打開

# 啟動 Chrome 瀏覽器
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打開國泰世華銀行官網
url = "https://www.cathaybk.com.tw/cathaybk/"
driver.get(url)

# 等待網頁加載完成
time.sleep(5)  # 等待5秒

# 點擊左上角的選單按鈕
menu_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.hamburger-menu"))
)
menu_button.click()

# 等待選單出現，點擊 "個人金融"
personal_finance_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "個人金融"))
)
personal_finance_button.click()

# 點擊 "產品介紹"
product_intro_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "產品介紹"))
)
product_intro_button.click()

# 點擊 "信用卡列表"
credit_card_list_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "信用卡列表"))
)
credit_card_list_button.click()

# 等待信用卡列表頁面加載完成
time.sleep(5)

# 計算信用卡項目數量
credit_card_items = driver.find_elements(By.CSS_SELECTOR, ".credit-card-item")  # 假設每個項目使用這個CSS class
num_items = len(credit_card_items)
print(f"信用卡項目總數: {num_items}")

# 截取螢幕並保存
screenshot_path = "credit_card_list_screenshot.png"
driver.save_screenshot(screenshot_path)
print(f"信用卡列表截圖已保存到: {screenshot_path}")

# 關閉瀏覽器
driver.quit()