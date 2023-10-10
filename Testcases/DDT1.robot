*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/Login_resources.robot
Suite Setup     openmybrowser
Suite Teardown  Close Browsers
Test Template   InvalidLogin


*** Test Cases ***          username                password
Right_username_empty_pwd    raunakali           ${EMPTY}

Right_username_wrong_pwd    raunakali           haritha

Wrong_username_right_pwd    haritha             raunak@25

Wrong_username_empty_pwd    haritha             ${EMPTY}

WWrong_username_wrong_pwd   haritha             haritha




*** Keywords ***
InvalidLogin
    [Arguments]     ${username}     ${password}
    Inputusername    ${username} 
    Inputpwd    ${password}
    Clickloginbutton
    Error message should be visible