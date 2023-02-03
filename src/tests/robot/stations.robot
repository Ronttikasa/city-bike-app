*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Home Page Should Be Open
    Page Should Contain  City bike stations in Espoo and Helsinki

Page Contains Correct Stations
    Page Should Contain  Hanasaari
    Page Should Not Contain  Nokkala

Go To Next Page
    Click Link  next page
    Page Should Contain  Nokkala

Go To Previous Page
    Click Link  next page
    Click Link  previous page
    Page Should Contain  Hanasaari

Go To Journeys
    Click Link  Journeys
    Page Should Contain  City bike journeys

Go To Station
    Click Link  Westendinasema
    Page Should Contain  Departing journeys

