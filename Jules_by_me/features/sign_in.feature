Feature: Test the sign in for jules.app website

  Background:
    Given sign_in: I am a user on sign-in page

  @T1 @sign_in_incorrect_email_format
  Scenario: Verify if error message is displayed when not typing the correct email format
    When sign_in: Type 'abc' for the email
    Then sign_in: Verify error ‘Please enter a valid email address!’ is displayed

  @T2 @sign_in_correct_email_no_password
  Scenario: Verify if sign in btn is disable when typing the correct email and skipping the password input
    When sign_in: Input 'abc@yahoo.com' for email
    Then sign_in: Verify if log in btn is disabled
#
  @T3 @sign_in_correct_email_delete_password
  Scenario: Verify if error message is displayed when typing the correct email and clearing the password
    When sign_in: Type 'abc@yahoo.com' for email
    When sign_in: Input 'bla' for password and then clear it
    Then sign_in: Verify error ‘Please enter your password!’ is displayed







