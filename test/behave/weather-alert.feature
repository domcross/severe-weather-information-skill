Feature: weather-alert
  Scenario: current weather alerts
    Given an English speaking user
     When the user says "are there any weather alerts nearby"
     Then "severe-weather-information-skill" should reply with dialog from "no.alerts.dialog"
