*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/Login_Keywords.robot

*** Variables ***
${browser}      chrome
${siteURL}      https://godsownstay.com/
#${txt_clickbtn}     Login as Admin
${user}         raunakali
${pwd}          raunak@25

*** Test Cases ***
Login Test
    Open my Browser     ${Site URL}     ${Browser}
#    Maximize Browser Window
    Sleep    3
#    Click Button    ${txt_clickbtn}
    Enter Username    ${user}
    Enter Password    ${pwd}
    Click Login
#    GOSshould visible
    Close my browser
