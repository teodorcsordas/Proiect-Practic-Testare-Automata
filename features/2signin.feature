Feature: Sign in
  Scenario: Empty email field
    Given I am on the signin page
    When I enter correct password
    And I click on Autentificare button
    Then I should see an error tip
  Scenario: Empty password Field
    Given I am on the signin page
    When I enter correct password
    And I click on Autentificare button
    Then I should see an error tip
  Scenario: Incorrect email
    Given I am on the signin page
    When I enter incorrect email
    And I enter correct password
    And I click on Autentificare button
    Then I should recive an error message
  Scenario: Incorrect password
    Given I am on the signin page
    When I enter correct email
    And I enter incorrect password
    And I click on Autentificare button
    Then I should recive an error message
  Scenario: Successfully sign in
    Given I am on the signin page
    When I enter correct email
    And I enter correct password
    And I click on Autentificare button
    Then I should recive a successfuly signed in message


