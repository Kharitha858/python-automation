*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Getall_links
    Open Browser    https://www.worldometers.info/geography/alphabetical-list-of-countries/        chrome
    Maximize Browser Window
    ${getalllinkscount}=     get element count       xpath://a
    Log To Console    ${getalllinkscount}

    @{Linkitems}    Create List
    FOR    ${i}    IN RANGE     1    ${getalllinkscount}+1
        ${linktext}=    Get Text        xpath:(//a)[${i}]
        Log To Console    ${linktext}
         
    END