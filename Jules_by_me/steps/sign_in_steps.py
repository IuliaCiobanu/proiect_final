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