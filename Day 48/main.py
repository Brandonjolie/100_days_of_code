from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_Driver_path = (
    "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 48/driver.exe"
)

driver = webdriver.Chrome(executable_path=chrome_Driver_path)


def five_second_clicks(button):
    timeout = time.time() + 5
    while True:
        if time.time() > timeout:
            return
        button.click()


def cookieClicker():
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    driver.implicitly_wait(15)
    language_select = driver.find_element(By.ID, value="langSelect-EN")
    language_select.click()
    driver.implicitly_wait(5)
    # driver.get("https://orteil.dashnet.org/cookieclicker/")
    cookie_button = driver.find_element(By.ID, value="bigCookie")
    five_minute_timeout = time.time() + 5 * 60
    while True:
        if time.time() > five_minute_timeout:
            break
        five_second_clicks(cookie_button)
        unlocked_elements = driver.find_elements(By.CSS_SELECTOR, value=".unlocked")
        prices = [
            int(f.find_element(By.CLASS_NAME, value="price").text.replace(",", ""))
            for f in unlocked_elements
        ]
        max_price = max(prices)

        cookies_text = driver.find_element(By.ID, value="cookies").text
        cookie_count = int(cookies_text.split(" ")[0].replace(",", ""))
        if cookie_count > max_price:
            unlocked_elements[prices.index(max_price)].click()
    print(cookies_text)
    driver.quit()


cookieClicker()
