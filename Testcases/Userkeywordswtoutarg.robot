*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://www.godsownstay.com/
${browser}  chrome

*** Test Cases ***
TC1
    Launch Browser
    input text  xpath://input[@placeholder='Your Username*']    raunakali
    input text  xpath://input[@placeholder='Your Password']     raunak@25


*** Keywords ***

Launch Browser
    open browser    ${url}  ${browser}
    maximize browser window
    click element   xpath://span[text()=" Login as Admin"]