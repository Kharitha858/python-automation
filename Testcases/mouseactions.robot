*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Mouseactions
    #Right click:
    Open Browser    https://swisnl.github.io/jQuery-contextMenu/demo.html       chrome
    Maximize Browser Window
    Open Context Menu    //span[text()="right click me"]
    Sleep    3

    #Double click:
    Go To   https://testautomationpractice.blogspot.com/    
    Maximize Browser Window
    Double Click Element    //button[text()="Copy Text"]
    Sleep    3
    
    #drag and drop
    Drag And Drop    //div[@id="draggable"]    //div[@id="droppable"]
    Sleep    3