from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

WIKIPEDIA_MAIN_PAGE = "https://en.wikipedia.org/wiki/Main_Page"
COURSE_FORM_PAGE = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=COURSE_FORM_PAGE)

nmbr_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# nmbr_of_articles.click()

# all_portals = driver.find_element(By.XPATH, value='//*[@id="mp-other-content"]/ul/li[7]/b/a')
# all_portals.click()

# search_bar = driver.find_element(By.NAME, value="search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, value="fname")
first_name.send_keys("Ahmed")
last_name = driver.find_element(By.NAME, value="lname")
last_name.send_keys("Alwardani")
email = driver.find_element(By.NAME, value="email")
email.send_keys("aalwa049@gmail.com")
sign_up_button = driver.find_element(By.CSS_SELECTOR("form button"))
sign_up_button.click()

driver.close()
