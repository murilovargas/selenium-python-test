from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GETTING_STARTED_MENU_ITEM = (By.LINK_TEXT, '2. Getting Started')
    GETTING_STARTED_MENU_ITEM_BY_TEXT = (By.PARTIAL_LINK_TEXT, 'Getting Started')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass