*** Settings ***
Library     SeleniumLibrary




*** Keywords ***

Launch Browser
    [Arguments]     ${appurl}  ${appbrowser}
    open browser    ${appurl}  ${appbrowser}
    maximize browser window
    click element   xpath://span[text()=" Login as Admin"]
    ${title}=       get title
    [Return]    ${title}