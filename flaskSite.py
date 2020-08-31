from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', page_name = "Home")

@app.route("/about")
def about():
    return render_template('about.html', page_name = "About")

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html', page_name = "Portfolio")

if(__name__)=='__main__':
    app.run(debug = True)