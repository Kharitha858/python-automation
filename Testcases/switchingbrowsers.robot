*** Settings ***
Library         SeleniumLibrary

*** Test Cases ***
SwitchingtoMultiplebrowsers
        open browser  https://godsownstay.com/      chrome
        Maximize Browser Window
        Sleep    3


        Open Browser    https://gitlab.com/     chrome
        Maximize Browser Window
        Sleep    3

        Switch Browser    1
        ${title1}=  get title
        Log To Console    ${title1}

         Switch Browser    2
        ${title2}=  get title
        Log To Console    ${title2}


        Sleep    3
        Close all Browsers