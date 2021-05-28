'''
Flask server calling the html code
'''

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/Users/guillermo/organproject/OrganProject/Guillermo-HTML/Testimonies.html")
def testimonies():
    return render_template(Testimonies.html)
# I need other routes to return html for other pages
# Or create 1 other route and match the path of the route to one of the files
# ^^ Make a variable & return an html page based on the vriable

if __name__ == '__main__':
    app.run()


