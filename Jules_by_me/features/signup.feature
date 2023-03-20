Feature: Test the sign-up for jules.app website

  @T1 @create_account
  Scenario: Testing the Sign-up for personal with wrong e-mail
    When sing_in: I click the sign-up button
    When sing_up: I select personal radio button
    When sign_up: I send first name 'Iulia'
    When sign_up: I send last name 'Ciobanu'
    When sign_up: I set my email to  'abc'
    Then sign_up: I receive message: 'Please enter a valid email address.'







