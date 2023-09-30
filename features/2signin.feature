Feature: Sign in

  Background:
    Given I am on the signin page

  Scenario: Empty email field
    When I enter correct password
    And I click on Autentificare button
    Then I should see an error tip

  Scenario: Empty password Field
    When I enter correct password
    And I click on Autentificare button
    Then I should see an error tip

  Scenario: Incorrect email
    When I enter incorrect email
    And I enter correct password
    And I click on Autentificare button
    Then I should recive an error message

  Scenario: Incorrect password
    When I enter correct email
    And I enter incorrect password
    And I click on Autentificare button
    Then I should recive an error message

  Scenario Outline: Combination of incorrect email and password
    When I enter an incorrect "<email>" and "<password>"
    And I click on Autentificare button
    Then I should recive an error message
    Examples:
      |email                | password    |
      |lenu@ali.ro          |123456       |
      |mni@koli.fe          |Superpassword|
      |minione@yahoo.com    |safepass     |
      |email@email.com      |password     |
      |doiu@svrncs.es       |vocearomaniei|
      |lumea@viselor.itf    |9876543210   |
      |bunaziua@yahoo.ro    |SuPeRsAfEpAsSwOrD|

  Scenario: Successfully sign in
    When I enter correct email
    And I enter correct password
    And I click on Autentificare button
    Then I should recive a successfuly signed in message


