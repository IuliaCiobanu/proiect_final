from behave import *

@when('sing_in: I click the sign-up button')
def step_impl(context):
    context.sign_up_object.navigate_to_sign_up_page()

@when('sing_up: I select personal radio button')
def step_impl(context):
    context.sign_up_object.select_personal_button()

@when("sign_up: I send first name 'Iulia'")
def step_impl(context):
    context.sign_up_object.send_first_name()

@when("sign_up: I send last name 'Ciobanu'")
def step_impl(context):
    context.sign_up_object.send_last_name()

@when("sign_up: I set my email to  'abc'")
def step_impl(context):
    context.sign_up_object.send_email_name()

@then("sign_up: I receive message: 'Please enter a valid email address.'")
def step_impl(context):
    context.sign_up_object.check_error_message_email()