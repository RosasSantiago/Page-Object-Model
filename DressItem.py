# Imports Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DressItem:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.quantity = (By.ID, "quantity_wanted")
        self.plus = (By.CLASS_NAME, "icon-plus")

    def enter_quantity(self, quantity):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.quantity)).clear().send_keys(quantity)
        
    def add_elements(self, quantity):
        for i in range(quantity):
            self.driver.find_element_by_class_name(self.plus).click()

    def get_number_of_elements(self):
        return self.find_elements_by_id(self.quantity).get_attribute("value")
    
 

