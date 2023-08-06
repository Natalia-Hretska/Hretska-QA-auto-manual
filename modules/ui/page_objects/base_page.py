from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class BasePage():
    PATH = "C:/Users/grets/Hretska-QA-auto-manual/"
    DRIVER_NAME = "chromedriver-win64/chromedriver-win64/chromedriver.exe"

    def __init__(self) -> None:
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        
        self.driver = webdriver.Chrome(
            service = Service(BasePage.PATH + BasePage.DRIVER_NAME), options=chrome_options 
        )
    def wait_for_element(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    def close(self):
        self.driver.close()
        