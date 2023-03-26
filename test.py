# from linkedin_api import Linkedin
#
# api = Linkedin(
#     "ellahellbound01@gmail.com", "idontthinkso123"
# )
# data = api.get_profile("sakib-ovi-667877189")
# print(data)
# # print(data["url"], data["staffCount"], data["phone"]["number"], data["name"], data["headquarter"]["country"])


from linkedin import linkedin, server

# app = server.quick_api(
#     "866i0ftyjtp1d9", "U4UblCcylJWnNRNs"
# )


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from linkedin_api import Linkedin


# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
wait = WebDriverWait(driver, 30)
driver.get("https://www.linkedin.com/home")

people_button = wait.until(EC.element_to_be_clickable((
    By.XPATH, "/html[1]/body[1]/nav[1]/ul[1]/li[2]/a[1]/span[1]"
))).click()

first_name_input = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//input[@placeholder='First Name']"
)))

first_name_input.click()
#time.sleep(5)
first_name_input.send_keys("Sakib")
#time.sleep(5)
last_name_input = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//input[@placeholder='Last Name']"
)))
last_name_input.click()
time.sleep(5)
last_name_input.send_keys("Ovi")

search_button = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//button[@data-tracking-control-name='people-guest_people-search-bar_base-search-bar-search-submit"
              "']//icon[@class='base-search-bar__search-icon onload mx-auto lazy-loaded']//*[name()='svg'] "
)))

search_button.click()

""" Scraping data """
# "//li//a[@class='app-aware-link']"
profile_urls = wait.until(EC.visibility_of_all_elements_located((
    By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/section[1]/ul[1]/li[1]/a[1]"
)))
# time.sleep(5)
usernames = []
api = Linkedin(
    "sakibovi123@gmail.com", "Idontthinkso123"
)
for url in profile_urls:
    print(url.get_attribute('href'))
    href = url.get_attribute("href")
    username = href.split("/")[-1]
    usr = username.split("?")[0]
    usernames.append(usr)
for usr in usernames:
    print(usr)
    driver.quit()
    result = api.get_profile(f"{usr}")
    print(
        result["lastName"], result["locationName"], result["firstName"], result["experience"][0]["companyName"], result["experience"][0]["title"]
    )