import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.maximize_window()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
browser.find_element_by_id("book").click()
browser.execute_script("window.scrollBy(0, 200);")
x = int(browser.find_element_by_id('input_value').text)
solution = math.log(abs(12 * math.sin(x)))
browser.find_element_by_id('answer').send_keys(str(solution))
browser.find_element_by_id('solve').click()
