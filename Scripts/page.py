from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Selenium with Python" in self.driver.title
    
    def click_getting_started_menu_item(self):
        """Click in menu item 2. Getting Started"""
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(*MainPageLocators.GETTING_STARTED_MENU_ITEM))
        element = self.driver.find_element(*MainPageLocators.GETTING_STARTED_MENU_ITEM)
        element.click()

    def get_text_of_getting_started_menu_item(self):
        """Get inner text of menu item 2. Getting Started"""
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(*MainPageLocators.GETTING_STARTED_MENU_ITEM))
        element = self.driver.find_element(*MainPageLocators.GETTING_STARTED_MENU_ITEM)
        return element.get_attribute('innerText')

    def seekDuplicatedChars(self, text):
        """Seeking duplicated chars, ignoring case and spaces"""
        text_to_view = text.lower().replace(' ','')
        count = {}
        repeated_chars = 0
        for s in text_to_view:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1

        for key in count:
            if count[key] > 1:
                repeated_chars = 1
                print('Char: ' + key + ', appears: ' + str(count[key]) + ' times')

        return repeated_chars == 1