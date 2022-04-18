import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())


def load_jobs(return_list=False):
    '''
    This function takes you to the list view of the jobs listings in the greenhouse listing.
    There's a default option to return all job listings on the page as a list.
    '''
    driver.get("https://www.freenome.com")
    driver.maximize_window()

    driver.find_element_by_link_text("Accept").click()
    driver.find_element_by_link_text("Careers").click()
    driver.find_element_by_link_text("Accept").click()
    driver.find_element_by_link_text("View Jobs").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it(
        (By.ID, "grnhse_iframe")))
    wait.until(EC.element_to_be_clickable(
        (By.PARTIAL_LINK_TEXT, "Engineer")))
    if return_list:
        list_of_countries = driver.find_elements_by_partial_link_text(
            "Engineer")

        return list_of_countries


driver.delete_all_cookies()
driver.get("chrome://settings/clearBrowserData")
driver.find_element_by_xpath("//settings-ui").send_keys(Keys.ENTER)

jobs = load_jobs(return_list=True)
job_names_raw = [i.text for i in jobs]
print("The url is currently", driver.current_url)
print("\n --- All Currently Available Engineer Jobs --- \n")

for job in job_names_raw:
    print(job)

print("\n Hope you found something you like! \n")
driver.quit()
