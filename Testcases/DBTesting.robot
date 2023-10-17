*** Settings ***
Library     DatabaseLibrary
Library     OperatingSystem
Suite Setup     Connect To Database     pymysql     ${DBName}   ${DBUser}   ${DBPass}   ${DBHost}   ${DBPort}
Suite Teardown  Disconnect From Database

*** Variables ***
${DBName}       scott
${DBUser}       root
${DBPass}       admin
${DBHost}       127.0.0.1
${DBPort}       3306

*** Test Cases ***
#Create_person_table
#    ${op}=  Execute Sql String    Create table Person (id integer,first_name varchar(20),last_name varchar(20));
#    Log To Console    ${op}
#    Should Be Equal As Strings    ${op}  None

#Inserting Data in person Table
##     signle record
#    ${op}=  Execute Sql String    Insert into person values(777,"Bairavi","Tiger");
#    Log To Console    ${op}
#    Should Be Equal As Strings    ${op}    None

Multiple Records
    ${op}=  Execute Sql Script    ./Testdata/mydb_person_insertdata.sql
    Log To Console    ${op}
    Should Be Equal As Strings    ${op}    None
Check Bairavi record present in person table
    Check If Exists In Database    select id from scott.person where first_name="Bairavi";
Check David record not present in person table
    Check If Not Exists In Database    select id from scott.person where first_name="David";

Check person table exists in scott database
    Table Must Exist    person

Verify row count is zero
    Row Count Is 0    select id from scott.person where first_name="K";

Verify row count is equal to some value
    Row Count Is Equal To X  SELECT * FROM scott.person WHERE first_name="Kiran";   1

Verify row count is greater than some value
    Row Count Is Greater Than X    select id from scott.person where first_name="Bairavi";    0

Verify row coount is less than some value
    Row Count Is Less Than X    select id from scott.person where first_name="Bairavi";        4

Update record in person table
    ${op}=  Execute Sql String    Update scott.person set last_name='tellodu' where id=777;
    Log To Console    ${op}
    Should Be Equal As Strings    ${op}    None

Retrieve records from person table
    ${output} =    Execute SQL String    SELECT * FROM person;
    Log    ${output}
    Should Be Equal As Strings    ${output}    None

Delete record from person table
    ${op}=  Execute Sql String    delete from scott.person;
    Should Be Equal As Strings    ${op}    None