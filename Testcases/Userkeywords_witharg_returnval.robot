*** Settings ***
Library     SeleniumLibrary
Resource   ../Resources/resources.robot
*** Variables ***
${url}      https://www.godsownstay.com/
${browser}  chrome

*** Test Cases ***
TC1
    ${Page Title}=      Launch Browser      ${url}      ${browser}
    Log To Console    ${Page Title}
    input text  xpath://input[@placeholder='Your Username*']    raunakali
    input text  xpath://input[@placeholder='Your Password']     raunak@25


