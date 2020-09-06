#This file is to store all portfolio items in a list of dictionaries. 
# This list will be imported into flask app and passed into portfolio page.

portfolioList = [
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
