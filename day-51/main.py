import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PROMISED_DOWN = 500
PROMISED_UP = 50
TWITTER_EMAIL = "aalwa049@yahoo.com"
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()

        sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, value='.start-button a')
        go_button.click()

        sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                           '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                           '2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                             '2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        sleep(2)
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                         '2]/div/input')
        email.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                               '2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        sleep(2)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                            '3]/div/label/div/div[2]/div[1]/input')

        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                 '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                                 '1]/div/div/div/div[2]/div['
                                                                 '1]/div/div/div/div/div/div/div/div/div/div['
                                                                 '1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                                '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                                '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')

        tweet_button.click()

        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
