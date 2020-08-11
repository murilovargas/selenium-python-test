import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import page

class PythonSeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://selenium-python.readthedocs.io/")

    def test_search_in_python_org(self):
        #Load the main page
        main_page = page.MainPage(self.driver)
        #Checks if the word "Selenium with Python" is in title
        assert main_page.is_title_matches(), "selenium with python title doesn't match."
        #Clicking in the menu item 2. Getting Started
        main_page.click_getting_started_menu_item()
        #Getting text of element
        text = main_page.get_text_of_getting_started_menu_item()
        #Seeking duplicated chars
        assert main_page.seekDuplicatedChars(text), "there are not repeated chars"

    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()