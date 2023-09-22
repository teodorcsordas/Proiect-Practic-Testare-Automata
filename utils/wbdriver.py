from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class WebDriver:
    driver = webdriver.Chrome()
    driver.maximize_window()

    def quit(self):
        self.driver.quit()
