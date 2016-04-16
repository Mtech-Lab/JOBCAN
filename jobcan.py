from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('https://ssl.jobcan.jp/login/pc-employee/?client_id=会社ID')


username = driver.find_element_by_xpath("//input[contains(@name, 'email')]")
username.send_keys("ログインID")


password = driver.find_element_by_xpath("//input[contains(@name, 'password')]")
password.send_keys("パスワード")

password.send_keys(Keys.RETURN)


push = driver.find_element_by_xpath("//p[contains(@name, 'adit_item')]")
push.click()


driver.quit()
