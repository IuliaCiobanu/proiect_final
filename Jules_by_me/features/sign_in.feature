Feature: Test the sign in for jules.app website

  Background:
    Given sign_in: I am a user on sign-in page

  @T1 @sign_in_incorrect_email_format
  Scenario Outline: Verify if error message is displayed when not typing the correct email format
    When sign_in: Type "<email>" for the email
    Then sign_in: Verify error ‘Please enter a valid email address!’ is displayed
    Examples:
      | email       |
      | abc.com     |
      | 123         |
      | sam         |
      | sdsf@sdfsdf |

  @T2 @sign_in_correct_email_no_password
  Scenario: Verify if sign in btn is disable when typing the correct email and skipping the password input
    When sign_in: Input 'abc@yahoo.com' for email
    Then sign_in: Verify if log in btn is disabled

  @T3 @sign_in_correct_email_delete_password
  Scenario: Verify if error message is displayed when typing the correct email and clearing the password
    When sign_in: Type 'abc@yahoo.com' for email
    When sign_in: Input 'bla' for password and then clear it
    Then sign_in: Verify error ‘Please enter your password!’ is displayed

  @T4 @Check_view_password_btn
  Scenario: Verify that view password btn is working
    When sign_in: Input 'abc@yahoo.com' for email
    When sign_in: Type 'bla' for the password
    When sign_in: Click on the view password btn
    Then sign_in: Check that 'bla' password is visible
  @T5 @invalid_email_and_password
  Scenario: Log in with invalid email and password and check error message
    When sign_in: Input 'iulia.codeaza@yahoo.com' for the email
    When sign_in: Input 'abc123!' for the password
    When sign_in: Press the log in btn
    Then sign_in: Check that 'Invalid email/password combination' alert is displayed

  @T6
  Scenario: Verify forgot password is working
    When sing_in: Click on 'Forgot password?' link
    When forgot_password: Verify you are redirected to 'https://jules.app/forgot-password'
    When forgot_password: Input the email address 'iulia.codeaza@yahoo.com'
    When forgot_password: Click on send email btn
    Then forgot_password: Verify alert 'Email Sent'

  @T7
  Scenario: Verify if Download on the App Store is working
    When sign_in: Click Download on the App Store icon
    Then sign_in: Verify if you are redirected on Apple Store

  @T8
  Scenario: Verify if Get it on Google Play is working
    When sign_in: Click Get it on Google Play icon
    Then sign_in: Verify if you are redirected on Google Play

  @T9
  Scenario: Verify if FAQ link is working
    When sign_in: Click on FAQ link
    Then sign_in: Verify if you are redirected on 'https://static.jules.app/faq.html'

  @T10
  Scenario: Log in with correct email and password
    When sign_in: Input 'iulia.codeaza@gmail.com' for the email
    When sign_in: Input 'Buburuza17!' for the password
    When sign_in: Press log in btn
    Then sign_in: Verify you are logged in





