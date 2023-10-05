import os
from selenium import webdriver
from time import sleep

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = "livescorehq"
USERNAME = "aalwa049@yahoo.com"
PASSWORD = "test12345"
LOGIN_URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get(url=LOGIN_URL)
        sleep(5)

        email_input = self.driver.find_element(By.NAME, value="username")
        email_input.send_keys(USERNAME)

        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(PASSWORD)

        sleep(2)
        password_input.send_keys(Keys.ENTER)
        sleep(5)

        # do_not_save_pw_button = self.driver.find_element(By.CSS_SELECTOR, value="._ac8f .x1i10hfl")
        # do_not_save_pw_button.click()
        # sleep(5)
        #
        # no_notifications_button = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div/div['
        #                                                                    '2]/div/div/div/div/div[2]/div/div/div['
        #                                                                    '3]/button[2]')
        # no_notifications_button.click()
        # sleep(5)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element(By.CSS_SELECTOR, value='.xl565be ._alvs')
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does. The method
            # can accept the script as well as a HTML element. The modal in this case, becomes the arguments[0] in
            # the script. Then we're using Javascript to say: "scroll the top of the modal (popup) element by the
            # height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CLASS_NAME, value="_acan")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div['
                                                                         '2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
