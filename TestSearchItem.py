import unittest
from selenium import webdriver
import time
from Index import Index
from PageItems import PageItems
from DressItem import DressItem
from selenium.webdriver.chrome.options import Options

class SearchCases(unittest.TestCase):
    
    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        self.driver = webdriver.Chrome("Chromedriver.exe", chrome_options=option)
        self.driver.get("http://automationpractice.com/index.php")
        self.IndexPage = Index(self.driver)
        self.driver.implictly_wait(5)
        self.ItemsPage = PageItems(self.driver)
        self.DressItem = DressItem(self.driver)

    @unittest.skip("Por el momento no ejecutar")
    def test_search_no_elements(self):
        self.IndexPage.search("hola")
        self.assertEqual(self.ItemsPage.return_no_elements_text, 'No results were found for your search "hola"')
        self.driver.save_screenshot("No_element.jpg")

    def test_search_find_dresses(self):
        self.IndexPage.search("dress")
        self.assertTrue('DRESS' in self.ItemsPage.return_section_title())

    def test_search_find_tshirts(self):
        self.IndexPage.search("t-shirt")
        self.assertTrue('"T-SHIRT"' in self.ItemsPage.return_section_title())

    def test_nuevo(self):
        self.IndexPage.search("t-shirt")
        self.ItemsPage.click_orange_button()
        self.DressItem.enter_quantity("25")
        self.DressItem.add_elements(3)
        number = self.ItemsPage.get_number_of_elements()
        self.assertTrue(number == "28")

    def test_selections(self):
        self.IndexPage.search("t-shirt")
        self.ItemsPage.select_by_text("Product Name: A to Z")
        self.ItemsPage.select_by_value("reference:asc")
        self.ItemsPage.select_by_index(4) 

    def test_dresses_options(self):
        self.IndexPage.click_dresses()
        self.ItemsPage.click_checkbox(2)
        self.ItemsPage.click_checkbox(4)
        self.ItemsPage.click_color(2)
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
