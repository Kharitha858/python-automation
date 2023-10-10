*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
#*** Variables ***
#${ITEMS}     1 2 3 4 5
##${i}
#
*** Test Cases ***
##prints ouput in same line bcz we gave only one space
#Template with FOR loop1
#    FOR    ${i}    IN    1 2 3 4 5
#        Log To Console   ${i}
#
#    END
## prints ouput in diffrent lines bcz we gave 2 spaces
#Template with FOR loop2
#    FOR     ${i}    IN      1  2  3  4   5
#        Log To Console   ${i}
#    END
#
##Creating list using numbers
#Template with FOR loop3
#    @{ITEMS}    create list  1  2  3  4  5
#    FOR    ${i}    IN    @{ITEMS}
#       Log To Console    ${i}
#    END
#
## for loop using string
#Template with FOR loop4
#    FOR    ${i}    IN    hari bairavi ganesh jooly tiger
#       Log To Console    ${i}
#    END
#
## Creating list using strings
#Template with FOR loop5
#    @{family}   Create List     hari  bairavi  ganesh  jooly  tiger
#    FOR    ${i}    IN   @{family}
#       Log To Console    ${i}
#    END
#
## for loop with exit condition
#
#Template with FOR loop6
#    @{items}    create list     1  2  3  4  5
#    FOR    ${element}    IN    @{items}
#        Log To Console    ${element}
#        Exit For Loop If    ${element}==4
#    END

# For loop with nested for loop
Template with FOR loop7
    @{LIST1}    Create List     1 2 3 4 5
    @{LIST2}    Create List     6 7 8 9 10
    FOR    ${i}    IN    @{LIST1}
        Log To Console    ${i}
        FOR    ${j}    IN    @{LIST2}
          Log To Console  ${j}

        END
    END
