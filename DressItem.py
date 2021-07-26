class DressItem:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.quantity = "quantity_wanted"
        self.plus = "icon-plus"

    def enter_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity).clear().send_keys(quantity)


    def add_elements(self, quantity):
        for i in range(quantity):
            self.driver.find_element_by_class_name(self.plus).click()

    def get_number_of_elements(self):
        return self.find_elements_by_id(self.quantity).get_attribute("value")

