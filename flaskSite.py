from flask import Flask, render_template, url_for

app = Flask(__name__)
app.static_folder = 'static'

portfolioItemList = [
    {
        "Title": "Lululemon Report",
        "Subtitle" : "A deeper look at Lululemon Athletica, Inc. from a fundamental perspective.",
        "BackgroundImage" : "/static/Images/YogaClass.jpg"
    },
    {
        "Title": "Lululemon Report",
        "Subtitle" : "A deeper look at Lululemon Athletica, Inc. from a fundamental perspective.",
        "BackgroundImage" : "/static/Images/YogaClass.jpg"
    }
]


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', page_name = "Home")

@app.route("/about")
def about():
    return render_template('about.html', page_name = "About")

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', page_name = "Portfolio", portfolio_items = portfolioItemList)

@app.route("/contact")
def contact():
    return render_template('contact.html', page_name = "Contact")

if(__name__)=='__main__':
    app.run(debug = True)