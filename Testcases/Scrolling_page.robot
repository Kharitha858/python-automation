*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Scrolling Test
    Open Browser    https://www.worldometers.info/geography/alphabetical-list-of-countries/     chrome
    Maximize Browser Window
    # Scrolling page till it reach a pixel number
#    Execute Javascript  window.scrollTo(0,2500)
    Sleep    3
    #scrolling page till find element on page
    # syntax: scroll element into view "Path of the element"
#    Scroll Element Into View    xpath://td[text()="Kenya"]
#    Sleep    8
    # scrolling page till the bottom
    Execute Javascript         window.scrollTo(0,document.body.scrollHeight)
    Sleep    5

    # scrolling page till the bottom to top
    Execute Javascript         window.scrollTo(0,-document.body.scrollHeight)
    Sleep    3