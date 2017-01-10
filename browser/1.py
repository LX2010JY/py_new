from selenium import webdriver
import time
# 这里需要下载phantom浏览器
driver = webdriver.PhantomJS(executable_path='../../phantomjs.exe')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()