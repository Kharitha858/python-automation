*** Settings ***
Library     SeleniumLibrary
*** Test Cases ***
HandlingHTML_table
    Open Browser    https://testautomationpractice.blogspot.com/    chrome
    Maximize Browser Window
    #counting the rows
    ${rows}=    Get Element Count    xpath://table[@name='BookTable']/tbody/tr
    Log To Console    ${rows}
    #counting the columns
    ${colns}=   Get Element Count    xpath://table[@name='BookTable']/tbody/tr[1]/th
    Log To Console    ${colns}
    #get the data from the table
    ${data}=    Get Text    xpath://table[@name='BookTable']/tbody/tr[7]/td[1]
    Log To Console    ${data}
    #validations on table column
    Table Column Should Contain    xpath://table[@name="BookTable"]    2    Author
    #validations on table row 
    Table Row Should Contain    xpath://table[@name="BookTable"]     7    Amit
    #validations on table cell
    Table Cell Should Contain    xpath://table[@name="BookTable"]    4    3    Javascript
    #validations on table header
    Table Header Should Contain    xpath://table[@name="BookTable"]    Price

