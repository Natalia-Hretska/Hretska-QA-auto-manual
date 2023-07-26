from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage():
    PATH = "C:/Users/grets/Hretska-QA-auto-manual/"
    DRIVER_NAME = "chromedriver-win64/chromedriver-win64/chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service = Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
        