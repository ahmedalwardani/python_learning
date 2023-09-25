from selenium import webdriver
from selenium.webdriver.common.by import By

IPHONE_CASE_LINK = ("https://www.amazon.ca/TAURI-iPhone-15-Pro-Protection/dp/B0CBBKM879/ref=sr_1_6?keywords=iphone+15"
                    "%22%22+pro+case&qid=1695469065&sr=8-6")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

# price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"The price is {price_dollars.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.text)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.close()
# driver.quit()
