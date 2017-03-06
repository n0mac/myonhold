from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
geckodriver="/Users/n0mac/Documents/driver/geckodriver"
driver = webdriver.Firefox(capabilities=caps, executable_path="/Users/n0mac/Documents/driver/geckodriver")
driver.get("http://vk.com")