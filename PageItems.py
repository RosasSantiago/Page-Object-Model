from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageItems:

    def __init__(self, my_Driver):
        self.sinresultados = '//*[@id="center_column"]/p'
        self.tittle_banner = '//*[@id="center_column"]/h1/span[1]'
        self.orange_button = "color_1"
        self.driver = my_Driver
        self.order = (By.ID, "SelectProductSort")
        self.checkbox = (By.CLASS_NAME, "checkbox")
        self.colorcheck = (By.CLASS_NAME, "color-option  ")

    def return_no_elements_text(self):
        return self.driver.find_element_by_xpath(self.sinresultados).text

    def return_section_title(self):
        return self.driver.fin_element_by_xpath(self.tittle_banner).text

    def click_orange_button(self):
        self.driver.find_element_by_id(self.orange_button).click()

    def select_by_text(self, text):
        order = Select(self.driver_find_element(*self.order))
        order.select_by_visible_text(text)

    def select_by_value(self, value):
        order = Select(self.driver_find_element(*self.order))
        order.select_by_value()

    def select_by_index(self, number):
        order = Select(self.driver_find_element(*self.order))
        order.select_by_index(number)

    def click_checkbox(self, number):
        self.driver.find_element(*self.checkbox)[number].click()

    def click_color (self, number):
        self.driver.find_elements(*self.colorcheck)[number].click()