import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


url = "https://tracking.post.ir/search.aspx"
driver.get(url)

time.sleep(1)


search_box = driver.find_element(By.ID, "txtbSearch")
search_box.clear()
search_box.send_keys(input("shomare marsole ra vared konid : "))
search_box.send_keys(Keys.RETURN)

time.sleep(2)


soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()


tracking_info = []
rows = soup.select("#pnlResult .newrowdata")
for row in rows:
    cols = row.find_all("div", class_="newtddata")
    if len(cols) == 4:
        step = cols[0].text.strip()
        status = cols[1].text.strip()
        location = cols[2].text.strip()
        time = cols[3].text.strip()
        tracking_info.append((step, status, location, time))

for info in tracking_info:
    print(f"مرحله: {info[0]}")
    print(f"وضعیت: {info[1]}")
    print(f"موقعیت: {info[2]}")
    print(f"ساعت: {info[3]}")
    print("-" * 40)
