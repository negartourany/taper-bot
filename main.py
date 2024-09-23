import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = r"D:\Games\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
drive = webdriver.Chrome(service=service)
drive.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = drive.find_element(By.ID,"cookie")
items = drive.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [i.get_attribute("id") for i in items]
timeout = time.time() + 5
five_min = time.time() + 60*5
while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = drive.find_elements(By.CSS_SELECTOR,"#store b")
        item_prices =[]
        for i in all_prices:
            text = i.text
            if text != "":
                price = int(text.split("- ")[1].replace(",",""))
                item_prices.append(price)
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = [item_ids[n]]

        money = drive.find_element(By.ID,"money").text
        if "," in money:
            money = money.replace(",","")
        cookie_count = int(money)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        try:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            # print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            print(to_purchase_id[0])
            drive.find_element(By.ID,f"{to_purchase_id[0]}").click()

        except ValueError:
            print("empty sucker")

        timeout = time.time() + 5





