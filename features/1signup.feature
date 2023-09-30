Feature: Register
  Background:
    Given I am on signup page

  Scenario: Existing email
    When I enter sign up data with existing email
    And I agree the confidentiality policy
    And I click on inregistrati-va button
    Then I should recive an error message

  Scenario: Empty prenume field
    When I enter sign up data without prenume
    And I agree the confidentiality policy
    And I click on inregistrati-va button
    Then I should see a red error tip

  Scenario: Empty nume field
    When I enter sign up data without nume
    And I agree the confidentiality policy
    And I click on inregistrati-va button
    Then I should see a red error tip

  Scenario: Empty telefon field
    When I enter sign up data without telefon
    And I agree the confidentiality policy
    And I click on inregistrati-va button
    Then I should see a red error tip

  Scenario: Empty e-mail field
    When I enter sign up data without email
    And I agree the confidentiality policy
    And I click on inregistrati-va button
    Then I should see a red error tip

  Scenario: Empty password field
    When I enter sign up data without password
    And I agree the confidentiality policy
    And I click on inregistrati-va button
    Then I should see a red error tip

  Scenario: Empty password confirmation field
    When I enter sign up data without password confirmation
    And I agree the confidentiality policy
    And I click on inregistrati-va button
    Then I should see a red error tip

  Scenario: Register without accepting privacy policy
    When I enter sign up data with existing email
    And I click on inregistrati-va button
    Then I should recive an privacy policy error tip