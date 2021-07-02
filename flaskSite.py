from flask import Flask, render_template, url_for, request, redirect
from portfolioitems import *

app = Flask(__name__)
app.static_folder = 'static'

portfolioItemList = getPortfolio()

@app.before_request
def enforceHttpsInHeroku():
  if request.headers.get('X-Forwarded-Proto') == 'http':
    url = request.url.replace('http://', 'https://', 1)
    code = 301
    return redirect(url, code=code)


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

@app.route("/vti-covid-outlook")
def vtifund():
    return render_template('/portfolio-items/vtifundreport.html', page_name = "VTI Fund Report")

@app.route("/thomas-irving-trade-analysis")
def itvki():
    return render_template('/portfolio-items/isaiahVkyriereport.html', page_name = "Thomas-Irving Stat Analysis")

@app.route("/website-code")
def websitecode():
    return render_template('/portfolio-items/websitecode.html', page_name = "My Website Code")

@app.route("/bballplayersearch")
def bballplayersearch():
    return redirect("http://bballplayersearch.herokuapp.com/")

@app.route("/semesterplanningapp")
def semesterplanningtool():
    return render_template('/portfolio-items/semesterplanningtool.html', page_name = "Java Semester Planning Tool")

if(__name__)=='__main__':
    app.run(debug = True)