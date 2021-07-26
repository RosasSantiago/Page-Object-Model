from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Index:
    def __init__(self, myDriver):
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        self.driver = myDriver
        self.dresses_link = (By.XPATH, '//*[@title="Dressees"')

    def search(self,item):
        try:
            search_box = WebDriverWait(self.Drive,5).until(EC.presence_of_element_located(*self.query_top))
            search_box.send_keys(item)

        except: 
            print("No se encuentra lo que buscaste")

    def click_dresses(self):
        self.driver_find_elements(*self.dresses_link)[1].click()