*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Journeys Page

*** Test Cases ***
Journey Page Should Be Open
    Page Should Contain  City bike journeys

Page Contains Correct Journeys
    Page Should Contain  2.04 km in 8 minutes

Go To Next Page
    Click Link  next page
    Page Should Contain  4.28 km in 26 minutes

Go To Previous Page
    Click Link  next page
    Click Link  previous page
    Page Should Contain  2.04 km in 8 minutes

Click Station Link
    Click Link  Viiskulma
    Page Should Contain  Fredrikinkatu 19

Go To Stations View
    Click Link  Stations
    Page Should Contain  City bike stations