*** Settings ***


*** Test Cases ***
TC1 User Registartion Test
    [Tags]  Regression
    Log To Console    this is user registration test
    Log To Console    User registration test is over
    
TC2 user login test
    [Tags]  sanity
    Log To Console    this is login test
    Log To Console    login test is over

TC3 change user settings
    [Tags]  Regression
    Log To Console    this is change user settings test
    Log To Console    Change user settings is over

TC4 Logout test
    [Tags]  sanity
    Log To Console    This is logout test
    Log To Console    logout test is over
