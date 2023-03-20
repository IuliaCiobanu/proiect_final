from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


class Sign_up_page(Base_page):
    SIGN_UP_LINK = (By.XPATH, "//a[@data-test-id='sign-up-link']")
    PERSONAL_BUTTON = (By.XPATH, "//input[@value='personal']")
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='root']/div/div[4]/div[2]/div/div[5]/button/span[1]")
    INPUT = (By.XPATH, "//input[@type='text']")

    FIRST_NAME_CONTINUE_BUTTON = (By.XPATH, "//button[@data-test-id='first-name-continue-btn']")
    LAST_NAME_CONTINUE_BUTTON = (By.XPATH, "//button[@data-test-id='last-name-continue-btn']")
    EMAIL_CONTINUE_BUTTON = (By.XPATH, "//button[@data-test-id='email-continue-btn']")

    ERROR_MESSAGE = (By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/p')

    def navigate_to_sign_in_page(self):
        self.chrome.get( 'https://jules.app/sign-in' )


    def navigate_to_sign_up_page(self):
        self.chrome.find_element( *self.SIGN_UP_LINK ).click()
        time.sleep( 2 )

    def select_personal_button(self):
        self.chrome.find_element(*self.PERSONAL_BUTTON).click()
        time.sleep( 2 )
        self.chrome.find_element( *self.CONTINUE_BUTTON ).click()
        time.sleep( 2 )

    def send_first_name(self):
        self.chrome.find_element( *self.INPUT ).send_keys('Iulia')
        time.sleep( 2 )
        self.chrome.find_element(*self.FIRST_NAME_CONTINUE_BUTTON).click()
        time.sleep( 2 )

    def send_last_name(self):
        self.chrome.find_element( *self.INPUT).send_keys('Ciobanu')
        time.sleep( 2 )
        self.chrome.find_element( *self.LAST_NAME_CONTINUE_BUTTON ).click()
        time.sleep( 2 )

    def send_email_name(self):
        self.chrome.find_element( *self.INPUT ).send_keys("abc")
        time.sleep( 2 )
        # self.chrome.find_element(*self.EMAIL_CONTINUE_BUTTON).click()
        # time.sleep( 2 ) is not clickable- error


    def check_error_message_email(self):
        expected = "Please enter a valid email address."
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        assert expected == actual, f'The message is {actual} not the expected: {expected}'
        time.sleep( 2 )
