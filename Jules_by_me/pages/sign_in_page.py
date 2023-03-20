from pages.base_page import Base_page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


class Sign_in(Base_page):
    EMAIL = (By.XPATH, '//input[@type="text"]')
    EMAIL_ERROR=(By.XPATH, "/html/body/div/div/div[2]/form/div/div[1]/div/p")
    PASSWORD = (By.XPATH, '//input[@placeholder="Enter your password"]')
    PASSWORD_ERROR = (By.XPATH,'/html/body/div/div/div[2]/form/div/div[2]/div/p')
    LOGIN_BTN = (By.XPATH, '//div/button')
    VIEW_PASS_BTN = (By.XPATH,'//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/div')
    ALERT = (By.XPATH,"//*[@id='client-snackbar']/div/span")
    FORGOT_PASSWORD = (By.LINK_TEXT, "Forgot password?")
    SEND_EMAIL_BTN = (By.XPATH, "//button[@data-test-id='login-button']")
    ALERT_NO_ACCOUNT = (By.XPATH,"//*[@id='client-snackbar']/div/div/span")


    def navigate_to_sign_in_page(self):
        self.chrome.get( 'https://jules.app/sign-in' )

    def add_email(self,email):
        self.chrome.find_element(*self.EMAIL).send_keys(email)
        time.sleep(2)

    def verify_no_valid_email_msg_displayed(self):
        expected_msg = "Please enter a valid email address!"
        actual_msg = self.chrome.find_element(*self.EMAIL_ERROR).text
        assert expected_msg==actual_msg, f"Error: The {expected_msg} message is not displayed, instead {actual_msg} is displayed"
        time.sleep( 2 )
# ///////////////////T2

    def verify_login_btn_is_disable(self):
        enabled_login_btn = self.chrome.find_element(*self.LOGIN_BTN).is_enabled()
        assert enabled_login_btn == False, f"The button is enabled, it should be disabled"
        time.sleep( 2 )
# /////////////////T3
# Verify if error message is displayed when typing the correct email and clearing the password

    def add_and_clear_password_field(self):
        password = self.chrome.find_element(*self.PASSWORD)
        password.send_keys('bla')
        time.sleep( 2 )
        for i in range(3):
            password.send_keys(Keys.BACKSPACE)
        time.sleep( 2 )

    def check_error_msg_no_pswd(self):
        actual_msg = self.chrome.find_element(*self.PASSWORD_ERROR).text
        expected_msg = "Please enter your password!"
        assert actual_msg==expected_msg, f"Error: The error msg for clearing the password is not displayed"
        time.sleep( 2 )

# -----T4
    def add_password(self,password):
        self.chrome.find_element( *self.PASSWORD ).send_keys(password)

    def view_password(self):
        self.chrome.find_element(*self.VIEW_PASS_BTN).click()

    def check_password_visible_btn(self):
        password_text = self.chrome.find_element( *self.PASSWORD ).get_attribute('value')
        expected_password_text='bla'
        assert str(password_text) == expected_password_text, f"Error: The view password btn is not working"

# -------T5
#     add email
#     add password

    def click_login_btn(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()

    def check_alert_invalid_email_pass(self):
        actual_alert_msg = self.chrome.find_element( *self.ALERT ).text
        print( actual_alert_msg )
        expected_alert_msg = "Invalid email/password combination"
        assert str( actual_alert_msg ) == expected_alert_msg, f"Error: {expected_alert_msg}, actual {actual_alert_msg} "

# --------T6
    def click_forgot_password_link(self):
        self.chrome.find_element(*self.FORGOT_PASSWORD).click()

    def verify_url(self):
        url = self.chrome.current_url
        assert "forgot-password" in str( url ), f"Error: the link in not correct"

    # add_email
    def send_email(self):
        self.chrome.find_element(*self.SEND_EMAIL_BTN).click()

    def verify_alert_email_sent(self):
        actual_text = self.chrome.find_element(*self.ALERT_NO_ACCOUNT).text
        expected_text = "Email Sent"
        assert actual_text==expected_text, f"Error: The actual text is {actual_text} not the expected {expected_text}"






