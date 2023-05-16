# pip install selenium==4.9.0
# You need to have Google Chrome Installed.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# set option for Chrome
options = webdriver.ChromeOptions()
# detach Chrome so it doesn't disappear when the code exits
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# go to the panel
driver.get("http://192.168.0.1/")
# doesn't seem necessary
# driver.set_window_size(1536, 912)
driver.find_element(By.ID, "pcPassword").send_keys("123456")
driver.find_element(By.ID, "pcPassword").send_keys(Keys.ENTER)
driver.switch_to.frame(2)
driver.find_element(By.ID, "a38").click()
driver.find_element(By.ID, "a44").click()
driver.switch_to.default_content()
driver.switch_to.frame(4)
driver.find_element(By.ID, "reboot").click()
assert driver.switch_to.alert.text == "确认重新启动路由器？"
# wait 3 seconds before accepting alert
time.sleep(3)
driver.switch_to.alert.accept()
