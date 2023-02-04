*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Station Page

*** Test Cases ***
Station Page Should Be Open
    Page Should Contain  Hanasaari
    Page Should Contain  Departing journeys

Click Station Link
    Click Link  Koivusaari (M)
    Page Should Contain  Sotkatie 11

Return To Stations List
    Click Link  Back to station list
    Page Should Contain  City bike stations