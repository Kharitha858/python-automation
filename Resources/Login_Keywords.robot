*** Settings ***
Library     SeleniumLibrary
Variables   ../PageObejects/Locators.py


*** Keywords ***
Open my Browser
    [Arguments]     ${Site URL}     ${Browser}
    Open Browser    ${Site URL}     ${Browser}
    Maximize Browser Window

Enter Username
    [Arguments]     ${usename}
    Input Text    ${txt_loginusername}   ${usename}
    
Enter Password
    [Arguments]     ${password}
    Input Text    ${txt_loginpassword}    ${password}


Click Login
    Click Button    ${btn_Login}

Verify Successful login
    Page Should Contain    Godsownstay.com

Close browser
    Close Browser
