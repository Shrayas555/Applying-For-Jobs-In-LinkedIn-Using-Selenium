from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
PHONE='YOUR NUMBER'
driver=webdriver.Chrome(executable_path='/Users/shrayasraju/Desktop/chromedriver')
action=ActionChains(driver)
driver.get('https://www.linkedin.com/home')

email=driver.find_element(By.XPATH,'//*[@id="session_key"]')

email.send_keys('shrayas5555@gmail.com')

password=driver.find_element(By.XPATH,'//*[@id="session_password"]')
password.send_keys('*******')

signin=driver.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/button')
signin.click()





time.sleep(15)

job=driver.find_element(By.XPATH,'//*[@id="global-nav"]/div/nav/ul/li[3]/a')
job.click()

time.sleep(15)

search=driver.find_element(By.XPATH,'/html/body/div[4]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
search.send_keys('python developer')

time.sleep(15)

search.send_keys(Keys.ENTER)


time.sleep(15)

easy=driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button')
easy.click()

time.sleep(10)

all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME,"fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR,"footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
time.sleep(5)
driver.quit()






