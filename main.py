from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# log in w/ facebook, so we need your fb credentials here
EMAIL = "YOUR_FB_EMAIL"
PWD = "YOUR_FB_PWD"
TINDER_URL = "https://tinder.com/"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(TINDER_URL)
time.sleep(4)
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_id("email")
pwd = driver.find_element_by_id("pass")
email.send_keys(EMAIL)
pwd.send_keys(PWD)
pwd.send_keys(Keys.ENTER)

time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)

# - Click ALLOW for location.
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(2)
# - Click NOT INTERESTED for notifications.
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
time.sleep(2)
# - Click I ACCEPT for cookies
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
time.sleep(5)

# max of 100 swipes a day on Free tier
for n in range(100):
    try:
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button').click()
    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
