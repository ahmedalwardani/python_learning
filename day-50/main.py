import os

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

TINDER_ENDPOINT = "https://tinder.com/"
FACEBOOK_EMAIL = "aalwa049@yahoo.com"
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get(url=TINDER_ENDPOINT)

sleep(2)

log_in_button = driver.find_element(By.XPATH, value='//*[@id="s1477815459"]/div/div[1]/div/main/div['
                                                    '1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()

sleep(2)

log_in_with_facebook_button = driver.find_element(By.XPATH, value='//*[@id="s-250565617"]/main/div/div/div['
                                                                  '1]/div/div/div[2]/div[2]/span/div[2]/button')
log_in_with_facebook_button.click()

sleep(2)

base_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]

driver.switch_to.window(facebook_login_window)

email_input = driver.find_element(By.XPATH, value='//*[@id="email"]')
email_input.send_keys(FACEBOOK_EMAIL)

sleep(2)

password_input = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password_input.send_keys(FACEBOOK_PASSWORD)
password_input.send_keys(Keys.ENTER)

sleep(2)

driver.switch_to.window(base_window)

sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="s-250565617"]/main/div/div/div/div[3]/button[1]')
allow_location_button.click()


not_interested_notifications_button = driver.find_element(By.XPATH, value='//*[@id="s-250565617"]/main/div['
                                                                          '1]/div/div/div[3]/button[2]')
not_interested_notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div['
                                                          '1]/div/div[2]/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value='.itsAMatch a')
            match_popup.click()

        except NoSuchElementException:
            sleep(2)

driver.quit()




