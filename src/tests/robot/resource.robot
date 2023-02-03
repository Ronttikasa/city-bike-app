*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${URL}  http://localhost:5000

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Home Page
    Go To  ${URL}

Go To Journeys Page
    Go To  ${URL}/journeys