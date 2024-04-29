from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver


# Navigate to a Google Maps URL with photos
url = input('url: ')
driver = webdriver.Chrome()
driver.get(url)

waited = False
while True:
    try:
        # Wait for the "Next" button to become clickable and click it
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='eU5Rrb L6Bbsd AnCkCf'][aria-label='Next']")))
        next_button.click()
        time.sleep(0.3)
        WebDriverWait(driver, 10).until(EC.title_contains("Google Maps"))
        current_url = driver.current_url
        with open('main.txt','a') as f:
            f.write(current_url+'\n')
            print(current_url)
    except:
        if waited == False:
            time.sleep(5)
            waited = True
        else:
            break
    

   
driver.quit()
