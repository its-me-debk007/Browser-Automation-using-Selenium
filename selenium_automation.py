from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Edge('D:\\Test_Programs\\msedgedriver.exe')
browser.maximize_window()

browser.get('https://aktu.prutor.ai')
browser.find_element_by_xpath('//*[@id="header"]/div[2]/div/div[2]/ul/li[1]/a').click()
browser.find_element_by_id('user_login').send_keys('debashish2015442@akgec.ac.in')
browser.find_element_by_id('user_pass').send_keys('DBZsuper#2001',Keys.ENTER)
