import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome(executable_path='E:\\chromedriver\\chromedriver.exe')
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button=browser.find_element_by_id("book")
    button.click()
    x_sel = browser.find_element_by_id("input_value")
    x = x_sel.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    submit = browser.find_element(By.ID,'solve')
    submit.click()



finally:
    time.sleep(8)
    browser.quit()