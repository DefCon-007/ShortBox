import tinyurl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("/Users/ayush/Dropbox/CODE/Python/VirtualENVs/ShortBox/chromedriver")
driver.get('http://expirebox.com/')
file_upload = driver.find_element_by_id('fileupload')
print ("Uploading file please wait")
file_upload.send_keys("/Users/ayush/Dropbox/CODE/ACCESS_TOKEN")

del_button = driver.find_element_by_xpath("//button[@class='btn btn-danger btndel']")
time.sleep(5)
del_button.click()
driver.switch_to_window(driver.window_handles[1])
del_link = driver.current_url + "?proceed=1"
down_link = driver.find_element_by_xpath("//a[@class='btn btn-xs btn-success btn-download']").get_attribute('href')
print ("Download link : " + tinyurl.create_one(down_link))
print ("Delete link : " + tinyurl.create_one(del_link))
# while True :
#     try:
#         main_link = driver.find_element_by_xpath("//a[@class='btn btn-md btn-primary btn-download btn-block ']")
#         break
#     except :
#         print (driver.current_url)
#         pass
#print (main_link.get_attribute('href'))
# print (driver.current_url)

