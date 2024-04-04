from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    # //*[@id="login"]/div[1]/label/input
    LOCATOR_LOGIN_FIELD = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PASS_FILD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, '''button''')
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    LOCATOR_USER_NAME_FIELD = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]/a''')
    LOCATOR_NEW_POST_BTN = (By.CSS_SELECTOR, '''#create-btn''')
    LOCATOR_TITLE_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[1]/div/label/input''')
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea''')
    LOCATOR_CONTENT_FIELD = (By.XPATH, '''//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea''')
    LOCATOR_SAVE_BTN = (By.CSS_SELECTOR, '''#create-item > div > div > div:nth-child(7) > div > button > span''')
    LOCATOR_POST_TITLE_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div[1]/h1''')
    LOCATOR_CONTACT_FIELD = (By.CSS_SELECTOR, '''#app > main > nav > ul > li:nth-child(2) > a''')
    LOCATOR_CONTACT_NAME_FIELD = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
    LOCATOR_CONTACT_MAIL_FIELD = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, '''//*[@id="contact"]/div[3]/label/span/textarea''')
    #LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, '''#contact > div.submit > button > div''')
    LOCATOR_CONTACT_US_BTN = (By.XPATH,'''//*[@id="contact"]/div[4]/button''')

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} in {TestSearchLocators.LOCATOR_PASS_FILD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FILD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_user_text(self):
        user_name_field = self.find_element(TestSearchLocators.LOCATOR_USER_NAME_FIELD, time=3)
        text = user_name_field.text
        logging.info(f'We found text {text} in username field {TestSearchLocators.LOCATOR_USER_NAME_FIELD[1]}')
        return text

    def click_new_post_btn(self):
        logging.info('Click ' + ' new post button')
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, text):
        logging.info(f'Send {text} in {TestSearchLocators.LOCATOR_TITLE_FIELD[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(text)

    def enter_content(self, text):
        logging.info(f'Send {text} in {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(text)

    def enter_description(self, text):
        logging.info(f'Send {text} in {TestSearchLocators.LOCATOR_DESCRIPTION_FIELD[1]}')
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(text)

    def click_save_btn(self):
        logging.info('Click "Save" button')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    def get_res_text(self):
        post_title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE_FIELD, time=3)
        text = post_title_field.text
        logging.info(f'We found text {text} in post title field {TestSearchLocators.LOCATOR_POST_TITLE_FIELD[1]}')
        return text

    def click_contact_link(self):
        logging.info('Click "Contact" in main menu')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_FIELD).click()

    def enter_contact_name(self, text):
        logging.info(f'Send {text} in {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}')
        contact_name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        contact_name_field.clear()
        contact_name_field.send_keys(text)

    def enter_contact_mail(self, text):
        logging.info(f'Send {text} in {TestSearchLocators.LOCATOR_CONTACT_MAIL_FIELD[1]}')
        mail_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_MAIL_FIELD)
        mail_field.clear()
        mail_field.send_keys(text)

    def enter_contact_content(self, text):
        logging.info(f'Send {text} in {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}')
        contact_content_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        contact_content_field.clear()
        contact_content_field.send_keys(text)

    def click_contact_us_btn(self):
        logging.info('Click "Contact us" button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()
