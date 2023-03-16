import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class SMSBot(webdriver.Chrome):
    def __init__(self, driver=webdriver.Chrome, teardown=False):
        self.driver = driver
        self.teardown = teardown
        # self.wait = WebDriverWait(self.driver, 25)
        super(SMSBot, self).__init__()
        self.maximize_window()
        self.implicitly_wait(10)

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.teardown:
            self.quit()

    def go_to_dashboard(self, url):
        try:
            self.get(url)
            print("Dashboard hit............")
        except:
            print("Url Not Found")

    def login_to_dashboard(self, username, password):
        try:
            wait = WebDriverWait(self, 25)
            name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Username']")))
            name.click()
            name.send_keys(username)
            passw = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "input[placeholder='Password']"
            )))
            passw.click()
            passw.send_keys(password)

            login = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "button[type='submit']"
            ))).click()
        except:
            print("Atrribute error")

    def find_campaign_section(self):
        try:

            wait = WebDriverWait(self, 25)
            camp = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "body > aside:nth-child(1) > nav:nth-child(2) > a:nth-child(6)"
            )))

            camp.click()
        except:
            print("Campaign not found!")

    def find_campaign_id(self):
        try:
            wait = WebDriverWait(self, 25)
            select_camp = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "a[href='https://sms.rayadvertising.com/campaign-details/CA10c2abdd46ff4089bb95ce1058636d12']"
            )))

            select_camp.click()

            print("campaign found......")
        except:
            print("Campaign id not found")

    def find_number_section(self):
        try:
            wait = WebDriverWait(self, 25)
            find_number_section = wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "body > aside:nth-child(1) > nav:nth-child(2) > a:nth-child(6)"
            )))
            find_number_section.click()
            print("number section clicked........")
        except:
            print("Error!")

    def clear_all_cookies(self):
        self.delete_all_cookies()
        print("Cookies CLeared!.....")


