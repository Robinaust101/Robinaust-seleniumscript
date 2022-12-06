Feature: Login - cpa portal
  Scenario: Login functional test with valid data
    Given I launched firefox
    When I open login page
    And  I enter user name
    And I enter password
    And I click login
    And I click PMIS
    Then Login successful