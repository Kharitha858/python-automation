*** Settings ***
Library     SeleniumLibrary



*** Variables ***

*** Test Cases ***
Handling dropdown and listboxes
    Open Browser      https://www.techlistic.com/p/selenium-practice-form.html  chrome
    Maximize Browser Window
    Sleep    5
    #selecting dropdowns options
    select from list by label   continents  Australia
    Sleep     3
    Select From List By Index    continents  5
    # selecting listbox options
    Select From List By Label    selenium_commands  Switch Commands
    Sleep    3
    Select From List By Label    selenium_commands  WebElement Commands
    Sleep    2

    #unselecting listbox
    Unselect From List By Label    selenium_commands  WebElement Commands
*** Keywords ***