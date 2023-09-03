import logging

import yaml
from selenium.webdriver.common.by import By

from BaseApp import BasePage


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
            logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operate with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f'We found text {text} in field {element_name}')
        return text


    def send_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login_form')


    def send_password(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='password_form')


    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NAME_FIELD'], word, description='enter_name')


    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_EMAIL_FIELD'], word, description='enter_emai')


    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'], word, description='enter_content')

    # get text


    def get_error_message(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error label')



    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT'], description='contact')


    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_US_BUTTON'], description='send')


    def subbmit_login(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')
