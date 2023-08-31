*** Settings ***
Library     SeleniumLibrary

*** Variables ***


*** Test Cases ***
Testing radiobutton and checkbox
    Open Browser      https://www.techlistic.com/p/selenium-practice-form.html  chrome
    Maximize Browser Window
    #Selecting radio button
    Select Radio Button    sex     Female
    Select Radio Button    exp    2

    #Selecting checkbox
    Select Checkbox    Automation Tester
    Select Checkbox    Selenium Webdriver

    #Deselecting Checkbox
    Unselect Checkbox  Selenium Webdriver

*** Keywords ***