# Personal-Website
This is the repository for my [personal website](https://www.razeenahmad.com). This was built using the Python Flask micro web framework 
and was my first time fully utilizing git for a coding project.

## Flask Application
The Flask application is defined in *flaskSite.py*. Basic information for each portfolio item is held in *portfolioitems.py*. 
A list of dictionaries made it easier to use Jinga within the portfolio page template and automate HTML code creation for each post.
I kept this in a separate file to reduce clutter in the Flask application file.
*Procfile* holds the definitions for commands that are run upon starting up the app. Currently, this only helps defines the Flask app's web server.


## Templates Folder
This folder houses all the HTML code for each website. *mastertemplate.html* has the basic framework from which all other pages are built from. After creating 
the header and footer of each page, I created a block for the rest of the webpage body to be defined by each page.The **main-pages** folder
houses the html code for the main tabs of the website (Home, About, Portfolio, & Contact). 
*posttemplate.html* holds the basic framework for each portfolio item I post. When adding new posts/content, this template will be used to display it on its unique page.
The code for these pages is found under the **portfolio-items** folder.

## Static Folder
The static folder houses all static content of my website. This includes all images, PDF files, and CSS stylesheets.  

This website is fully deployed using the Heroku cloud application platform.
