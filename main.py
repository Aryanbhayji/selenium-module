#The selenium package is used to automate web browser interaction from Python

'''Selenium is essentially a remote control for your web browser. 
 Whether your goal is automated testing, web scraping, 
 or just automating boring data-entry tasks, this guide will give you the modern foundation you need 
 (specifically focusing on Selenium 4, which is the current standard).'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")



input_element = driver.find_element(By.CLASS_NAME , "gLFyf")
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

WebDriverWait(driver , 5).until(EC.presence_of_element_located((By.CLASS_NAME , "gLFyf")))

link = input_element.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim ")
link.click()


driver.quit()