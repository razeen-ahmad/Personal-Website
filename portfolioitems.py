#This file is to store all portfolio items in a list of dictionaries. 
# This list will be imported into flask app and passed into portfolio page.

portfolioList = [
    {
        "Title": "Lululemon Report",
        "Subtitle" : "A deeper look at Lululemon Athletica, Inc. from a fundamental perspective.",
        "BackgroundImage" : "YogaClass.jpg"
    },
]

#Function to get list of portfolio items
def getPortfolio():
    return portfolioList
