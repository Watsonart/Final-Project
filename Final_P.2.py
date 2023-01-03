from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://chykalophia.com")

driver.maximize_window()

#Linkedin
linkedin = driver.find_element("xpath", '//i [@class="fab fa-linkedin"]')
linkedin.click()

#Facebook
facebook = driver.find_element("xpath", '//i [@class="fab fa-facebook-f"]')
facebook.click()

#Twitter
twitter = driver.find_element("xpath", '//i [@class="fab fa-twitter"]')
twitter.click()

#Instagram
instagram = driver.find_element("xpath", '//i [@class="fab fa-instagram"]')
instagram.click()

#Youtube
youtube = driver.find_element("xpath", '//i [@class="fab fa-youtube"]')
youtube.click()

#Github
github = driver.find_element("xpath", '//i [@class="fab fa-github"]')
github.click()

#Behance
behance = driver.find_element("xpath", '//a[@aria-label="Chykalophia on Behance website"]')
behance.click()

#Cookie policy
cookie = driver.find_element("xpath", '//*[text()="Cookie Policy"]')
cookie.click()