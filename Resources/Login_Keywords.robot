*** Settings ***
Library     SeleniumLibrary
Variables   ../PageObejects/Locators.py


*** Keywords ***
Open my Browser
    [Arguments]     ${Site URL}     ${Browser}
    Open Browser    ${Site URL}     ${Browser}
    Maximize Browser Window
    Sleep    3
    Click Element    ${txt_clickbtn}
Enter Username
    [Arguments]     ${usename}
    Input Text    ${txt_loginusername}   ${usename}
    
Enter Password
    [Arguments]     ${password}
    Input Text    ${txt_loginpassword}    ${password}


Click Login
    Click Button    ${btn_Login}

#GOSshould visible
#    Page Should Contain    Godsownstay.com

Close my browser
    Close Browser
