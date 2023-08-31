*** Settings ***
Library  SeleniumLibrary


*** Variables ***
#${browser}   chrome
#${url}  http://10.10.20.141:3000/

*** Test Cases ***
LoginTest
#    Create Webdriver    chrome   executable_path="webdriverscripts/chromedriver.exe"
	Open Browser    http://10.10.20.141:3000/   chrome
	Maximize Browser Window
	Click Element   xpath://div[@class='loginheadbtn']
	Click Element   xpath://span[normalize-space()='Login as Admin']
	Input Text      xpath://input[@placeholder='Your Username*']    raunakali
	Input Text      xpath://input[@placeholder='Your Password']     raunak@25
	Click Element   xpath://button[@type='submit']
    Close Browser



*** Keywords ***
#loginToApplication
#    Click Element   xpath://div[@class='loginheadbtn']
#	Click Element   xpath://span[normalize-space()='Login as Admin']
#	Input Text      xpath://input[@placeholder='Your Username*']    raunakali
#	Input Text      xpath://input[@placeholder='Your Password']     raunak@25
#	Click Element   xpath://button[@type='submit']
