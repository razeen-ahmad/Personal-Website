#This file is to store all portfolio items in a list of dictionaries. 
# This list will be imported into flask app and passed into portfolio page.

portfolioList = [
    {
        "Title": "VTI Fund Outlook →",
        "Subtitle" : "Understanding how we recover from COVID-19 through a combination of technical analyses and macroeconomic factors.",
        "BackgroundImage" : "covideconomy.jpg",
        "Route" : "vtifund",
    },
    {
        "Title": "This Website →",
        "Subtitle" : "See how I coded this website from scratch.",
        "BackgroundImage" : "websitecode.jpg",
        "Route" : "websitecode",
    },
    {
        "Title": "Lululemon Report →",
        "Subtitle" : "A deeper look at Lululemon Athletica, Inc. from a fundamental perspective.",
        "BackgroundImage" : "YogaClass.jpg",
        "Route" : "lululemon",
    },
]

#Function to get list of portfolio items
def getPortfolio():
    return portfolioList
