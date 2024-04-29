from selenium.webdriver.edge.options import Options
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv


# aria-label="Next"
def main_job():
        chrome_options = Options()
        chrome_driver = "chromedriver.exe"
        driver = webdriver.Chrome(service=Service(chrome_driver), options=chrome_options)
        wait = WebDriverWait(driver, 30)

        # open url
        in_URL = 'https://www.google.com/maps/contrib/101578067960377424029/photos/@27.097811,81.0914709,3a,75y,90t/data=!3m7!1e2!3m5!1sAF1QipNmi498rlwohIhmQexAmH3sVqwTuJjEnJsSHdrW!2e10!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipNmi498rlwohIhmQexAmH3sVqwTuJjEnJsSHdrW%3Dw365-h273-k-no!7i4160!8i3120!4m3!8m2!3m1!1e1?entry=ttu'
        driver.get(in_URL)
    
        wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//button[contains(@aria-label, 'Next')]")))
        while True:
               sleep(0.3)
               driver.find_element(By.XPATH,
                                    "//button[contains(@aria-label, 'Next')]").click()
               currenturl = driver.current_url
               try:
                link = currenturl.split('!1s')[-1].split('!')[0]
                gps = currenturl.split('@')[-1].split(',')[0]+','+currenturl.split('@')[-1].split(',')[1]
                row = [link,gps]

                with open('main.csv', 'a',newline='') as csvfile:
                # creating a csv writer object 
                        csvwriter = csv.writer(csvfile) 
                                
                        # writing the fields 
                        csvwriter.writerow(row) 
               except:
                pass
  
main_job()