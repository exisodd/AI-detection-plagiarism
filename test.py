import csv
import sys
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.ca/maps")

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

driver.get(r"https://app.copyleaks.com/v1/scan/ai/embedded")

time.sleep(10)