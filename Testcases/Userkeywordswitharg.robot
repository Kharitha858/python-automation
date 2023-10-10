*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://www.godsownstay.com/
${browser}  chrome

*** Test Cases ***
TC1
    Launch Browser      ${url}      ${browser}
    input text  xpath://input[@placeholder='Your Username*']    raunakali
    input text  xpath://input[@placeholder='Your Password']     raunak@25


*** Keywords ***

Launch Browser
    [Arguments]     ${appurl}  ${appbrowser}
    open browser    ${appurl}  ${appbrowser}
    maximize browser window
    click element   xpath://span[text()=" Login as Admin"]