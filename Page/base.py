import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class base(object):

    def __init__(self, driver):
        self.driver = driver

    def find_xpath_elt(self,locator) -> object:
        return self.driver.find_element_by_xpath(locator)

    def find_xpath_elts(self,locator):
        return self.driver.find_elements_by_xpath(locator)

    # Hàm click
    def Click(self, element)  -> object:
        return element.click()

    # Hàm senkey
    def senkeys(self,element, values):
        element.send_keys(values)

    # Hàm clear
    def Clear_id(self,element):
        return element.clear()

    # Hàm chụp ảnh màn hình
    def screenshot(self,element,values):
        return element.screenshot(values)

    #get text
    def get_text(self,element):
        return element.text

    def get_height(self,element):
        a = element.size
        return a['height']

    def get_width(self,element):
        a = element.size
        return a['width']

# Hàm chuyển của sổ


























