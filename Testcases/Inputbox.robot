*** Settings ***
Library      SeleniumLibrary


*** Variables ***


*** Test Cases ***
TestingInputBox
    Open Browser    http://10.10.20.141:3000/   chrome
    Maximize Browser Window
    Click Element   xpath://div[@class='loginheadbtn']
    Click Element   xpath://span[normalize-space()='Login as Admin']
    ${username_txt}     set variable       class:form-control
    Element Should Be Visible    ${username_txt}
    Element Should Be Enabled    ${username_txt}
    Input Text    ${username_txt}    raunakali
    ${password_txt}     Set Variable        class:form-control
    Element Should Be Visible    ${password_txt}
    Element Should Be Enabled    ${password_txt}
    Input Text    ${password_txt}   raunak@25
    Clear Element Text    ${password_txt}
    Close Browser

*** Keywords ***