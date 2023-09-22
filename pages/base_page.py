import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.page_objects import PageObjects
from utils.wbdriver import WebDriver


class BasePage(WebDriver, PageObjects):

    def load_signin_page(self):
        self.driver.get(PageObjects.signin_page_url)

    def fill_signin_email(self, email):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, PageObjects.email_field_XPATH)))
        self.driver.find_element(By.XPATH, PageObjects.email_field_XPATH).send_keys(email)

    def fill_signin_password(self, password):
        self.driver.find_element(By.XPATH, PageObjects.password_field_XPATH).send_keys(password)

    def click_autentificare(self):
        button = self.driver.find_element(By.XPATH, PageObjects.autentificare_button_XPATH)
        button.click()

    def accept_cookie(self):
        permission_button = self.driver.find_element(By.XPATH, PageObjects.cookie_permission_button_Xpath)
        if permission_button.is_displayed():
            permission_button.click()
        else:
            pass

    def confirmation_signin(self):
        assert self.driver.find_element(By.XPATH, PageObjects.confirmation_message_XPATH).is_displayed()

    def signin_error(self):
        assert self.driver.find_element(By.XPATH, PageObjects.error_message_xpath).is_displayed()

    def signup_error(self):
        assert self.driver.find_element(By.XPATH, PageObjects.existing_email_error_XPATH).is_displayed()

    def error_tip(self):
        assert self.driver.find_element(By.XPATH, PageObjects.error_tip_XPATH).is_displayed()

    def signup_error_tip(self):
        assert self.driver.find_element(By.XPATH, PageObjects.signup_error_tip_Xpath).is_displayed()

    def privacy_policy_error(self):
        assert self.driver.find_element(By.XPATH, PageObjects.privacy_policy_button_XPATH).is_displayed()

    def click_inregistrativa(self):
        self.driver.find_element(By.XPATH, PageObjects.inregistrativa_button_XPATH).click()

    def fill_prenume(self, prenume):
        self.driver.find_element(By.XPATH, PageObjects.prenume_field_XPATH).send_keys(prenume)

    def fill_nume(self, nume):
        self.driver.find_element(By.XPATH, PageObjects.nume_field_XPATH).send_keys(nume)

    def fill_telefon(self, telefon):
        self.driver.find_element(By.XPATH, PageObjects.telefon_field_XPATH).send_keys(telefon)

    def fill_new_email(self, email):
        self.driver.find_element(By.XPATH, PageObjects.new_email_field_XPATH).send_keys(email)

    def fill_new_password(self, parola):
        self.driver.find_element(By.XPATH, PageObjects.new_password_field_XPATH).send_keys(parola)

    def confirm_password(self, parola):
        # self.driver.find_element(By.XPATH, PageObjects.confirm_password_field_XPATH).send_keys(parola)
        self.driver.find_element(By.CSS_SELECTOR, PageObjects.confirm_password_field_CSS).send_keys(parola)

    def load_signup_page(self):
        self.driver.get(PageObjects.signup_page_url)

    def agree_policy(self):
        self.driver.find_element(By.XPATH, PageObjects.privacy_policy_button_XPATH).click()
