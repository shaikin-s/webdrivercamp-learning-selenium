from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://www.ebay.com/"
driver.get(url)
wait = WebDriverWait(driver, 3)
search_field = wait.until(EC.presence_of_element_located
                          ((By.XPATH, "//td[@class='gh-td-s']//input[@type='text']")))
print(driver.current_url)
search_field.send_keys("women watch")
search_button = driver.find_element(By.XPATH, "//*[@id='gh-btn']")
search_button.click()
search_header = wait.until(EC.presence_of_element_located
                           ((By.XPATH, "//h1[contains(@class, 'srp-controls__count-heading')"
                                       " and contains(., 'results for ')"
                                       " and contains(., 'women watch')]")))
print("Header verification successful.")
driver.quit()
