from behave import *

@given ("sign_in: I am a user on sign-in page")
def step_impl(context):
    context.sign_in_object.navigate_to_sign_in_page()

@when("sign_in: Type 'abc' for the email")
def step_impl(context):
    context.sign_in_object.add_email('abc')

@then("sign_in: Verify error ‘Please enter a valid email address!’ is displayed")
def step_impl(context):
    context.sign_in_object.verify_no_valid_email_msg_displayed()

# //////////// T2

@when("sign_in: Input 'abc@yahoo.com' for email")
def step_impl(context):
    context.sign_in_object.add_email('abc')

@then("sign_in: Verify if log in btn is disabled")
def step_impl(context):
    context.sign_in_object.verify_login_btn_is_disable()

# ///////////T3 Verify if error message is displayed when typing the correct email and clearing the password

@when("sign_in: Type 'abc@yahoo.com' for email")
def step_impl(context):
    context.sign_in_object.add_email('abc@yahoo.com')

@when("sign_in: Input 'bla' for password and then clear it")
def step_impl(context):
    context.sign_in_object.add_and_clear_password_field()

@then("sign_in: Verify error ‘Please enter your password!’ is displayed")
def step_impl(context):
    context.sign_in_object.check_error_msg_no_pswd()

# ___@T4 Scenario: Verify that view password btn is working

# @when ("sign_in: Input 'abc@yahoo.com' for email")
# def step_impl(context):
#     context.sign_in_object.add_email('abc@yahoo.com')

@when ("sign_in: Type 'bla' for the password")
def step_impl(context):
    context.sign_in_object.add_password('bla')

@when ("sign_in: Click on the view password btn")
def step_impl(context):
    context.sign_in_object.view_password()

@then ("sign_in: Check that 'bla' password is visible")
def step_impl(context):
    context.sign_in_object.check_password_visible_btn()

# -----@T5 Log in with invalid email and password and check error message

@when ("sign_in: Input 'iulia.codeaza@yahoo.com' for the email")
def step_impl(context):
    context.sign_in_object.add_email('iulia.codeaza@yahoo.com')

@when ("sign_in: Input 'abc123!' for the password")
def step_impl(context):
    context.sign_in_object.add_password('abc123!')

@when ("sign_in: Press the log in btn")
def step_impl(context):
    context.sign_in_object.click_login_btn()

@then ("sign_in: Check that 'Invalid email/password combination' alert is displayed")
def step_impl(context):
    context.sign_in_object.check_alert_invalid_email_pass()

# ------@T6 Verify forgot password is working
@when ("sing_in: Click on 'Forgot password?' link")
def step_impl(context):
    context.sign_in_object.click_forgot_password_link()

@when ("forgot_password: Verify you are redirected to 'https://jules.app/forgot-password'")
def step_impl(context):
    context.sign_in_object.verify_url()

@when ("forgot_password: Input the email address 'iulia.codeaza@yahoo.com'")
def step_impl(context):
    context.sign_in_object.add_email('iulia.codeaza@yahoo.com')

@when ("forgot_password: Click on send email btn")
def step_impl(context):
    context.sign_in_object.send_email()

@then ("forgot_password: Verify alert 'Email Sent'")
def step_impl(context):
    context.sign_in_object.verify_alert_email_sent()
