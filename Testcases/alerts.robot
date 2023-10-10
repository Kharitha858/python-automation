*** Settings ***
Library     SeleniumLibrary

*** Variables ***


*** Test Cases ***
HandlingAlerts
    Open Browser    https://testautomationpractice.blogspot.com/    chrome

    Maximize Browser Window
    Sleep    3
    Click Element    //button[text()="Alert"]
    Sleep    3
#    Alert Should Be Present         I am an alert box!
#    Handle Alert    accept
    Handle Alert        leave


*** Keywords ***