*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${LOGIN_URL}        https://www.godsownstay.com/
${BROWSER}          chrome


*** Keywords ***
openmybrowser
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
    Click Element    //span[text()=" Login as Admin"]

Close Browsers
    Close Browser

OpenLoginPage
    Go To    ${LOGIN_URL}


Inputusername
    [Arguments]     ${username}
    Input Text    xpath://input[@placeholder='Your Username*']    ${username}

Inputpwd
    [Arguments]     ${password}
    Input Text    //input[@placeholder='Your Password']    ${password}

Clickloginbutton
    Click Element    xpath://button[text()=" Login"]

Clicklogout
    Click Element    //div[@class='ant-space-item']
    Click Element    //p[normalize-space()='Logout']

Error message should be visible
    Page Should Contain    Invalid Usename or Password *

GOSshould visible
    Page Should Contain    Godsownstay.com














