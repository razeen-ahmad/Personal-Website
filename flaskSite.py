from flask import Flask, render_template, url_for
from portfolioitems import *

app = Flask(__name__)
app.static_folder = 'static'

portfolioItemList = getPortfolio()


@app.route("/home")
@app.route("/")
def home():
    return render_template('/main-pages/home.html', page_name = "Home")

@app.route("/about")
def about():
    return render_template('/main-pages/about.html', page_name = "About")

@app.route("/portfolio")
def portfolio():
    return render_template('/main-pages/portfolio.html', page_name = "Portfolio", portfolio_items = portfolioItemList)

@app.route("/contact")
def contact():
    return render_template('/main-pages/contact.html', page_name = "Contact")

@app.route("/lululemon-report")
def lululemon():
    return render_template('/portfolio-items/lululemonreport.html', page_name = "Lululemon Report")

@app.route("/website-code")
def websitecode():
    return render_template('/portfolio-items/websitecode.html', page_name = "My Website Code")

if(__name__)=='__main__':
    app.run(debug = True)