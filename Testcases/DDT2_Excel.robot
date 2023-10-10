*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/Login_resources.robot
Library     DataDriver      ../Testdata/Logindata.xlsx  sheet_name=Sheet1
Test Setup      openmybrowser
Test Teardown   Close Browsers
Test Template   InvalidLogin

*** Test Cases ***
LoginTest_with_Excel
    log to console ${username}  and ${password}



*** Keywords ***
InvalidLogin
        [Arguments]         ${username}     ${password}
        Inputusername    ${username}
        Inputpwd    ${password}
        Clickloginbutton
        Error message should be visible