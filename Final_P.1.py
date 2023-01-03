from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://chykalophia.com")

driver.maximize_window()

#Privacy policy
privacy = driver.find_element("xpath", '//*[text()="Privacy Policy"]')
privacy.click()