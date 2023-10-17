*** Settings ***

Suite Setup        log to console  Opening Browser
Suite Teardown      log to console  Closing Browser
Test Setup         log to console    opening application
Test Teardown       log to console      closing application


*** Test Cases ***
TC1 prepaid Recharge
    Log To Console    this is prepaid recharge

TC2 postpaid Recharge
    Log To Console    this is postpaid recharge

TC3 search
    Log To Console    this is a search test case
    
TC4 advance search
    Log To Console    this is a advance search testcase