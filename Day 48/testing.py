from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_Driver_path = (
    "//wsl.localhost/Ubuntu-20.04/home/bjolie/100daysofpython/Day 48/driver.exe"
)

driver = webdriver.Chrome(executable_path=chrome_Driver_path)


def scraping():
    try:
        driver.get("https://www.python.org/events/")
        event_times = driver.find_elements(By.TAG_NAME, "time")
        event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-title a")
        times_text = [f.text for f in event_times]
        titles_text = [f.text for f in event_titles]
        for _ in range(len(times_text)):
            print(f"Date: {times_text[_]} Title: {titles_text[_]}")
    except Exception as f:
        print(f)
        driver.quit()
    driver.quit()


def interacting():
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    words = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
    count = words.text
    # words.click()
    print(count)

    content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
    # content_portals.click()

    search = driver.find_element(By.NAME, value="search")
    search.send_keys("Python")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.quit()


def challenge_signup():
    link = "http://secure-retreat-92358.herokuapp.com/"
    driver.get(link)
    fname = driver.find_element(By.NAME, value="fName")
    fname.send_keys("brandon")
    lname = driver.find_element(By.NAME, value="lName")
    lname.send_keys("lastname")
    email = driver.find_element(By.NAME, value="email")
    email.send_keys("my_email@gmail.com")
    button = driver.find_element(By.CLASS_NAME, value="btn")
    button.click()


challenge_signup()
