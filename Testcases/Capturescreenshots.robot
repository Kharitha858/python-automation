*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Capturescreenshots
    Open Browser    https://godsownstay.com/        chrome
    Maximize Browser Window
    Sleep    3
    Click Element    xpath://span[text()="Close"]
  #capturing element screenshot:
    Capture Element Screenshot    //*[@id="root"]/div/div/div[1]/div[1]/div[1]/div/img      C:/Users/CBT/PycharmProjects/GodsOwnStay/goslogo.png
   # capturing page screenshot:
   Capture Page Screenshot      C:/Users/CBT/PycharmProjects/GodsOwnStay/gospage.png
   
   
   #default 
   Capture Element Screenshot    //*[@id="root"]/div/div/div[1]/div[1]/div[1]/div/img       goslogo.png
   Capture Page Screenshot      gospage.png