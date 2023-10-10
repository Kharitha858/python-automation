*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Navigational Keywords
    Open Browser    https://godsownstay.com/    chrome
    Maximize Browser Window
    ${loc}=         Get Location
    Log To Console    ${loc}

    Sleep    3

    Go To    https://about.gitlab.com/
    Maximize Browser Window
    ${loc}=         Get Location
    Log To Console    ${loc}
    Sleep    3
    Go Back
    ${loc}=           Get Location
    Log To Console      ${loc}

    Sleep    3