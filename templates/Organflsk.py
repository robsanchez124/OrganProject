'''
Flask server calling the html code
* Add redirect to home page
'''

from flask import Flask, render_template
import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates/'))

jinja_var = {
    'images': ['/Users/guillermo/organproject/OrganProject/static/images/hispanic_proportioned.png', '/Users/guillermo/organproject/OrganProject/static/images/hispanic_transplanted.png']


}  
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Users/guillermo/organproject/OrganProject/Guillermo-HTML/About_us.html")
def about_us():
    return render_template("About_us.html")


@app.route("/Users/guillermo/organproject/OrganProject/Guillermo-HTML/Resources.html")
def resources():
    return render_template("Resources.html")

@app.route("/Users/guillermo/organproject/OrganProject/templates/templates/Research.html")
def research():
    # images = [{
    #     'hispanic_proportioned_wait': /Users/guillermo/organproject/OrganProject/static/images/hispanic_proportioned.png,
    #     'hispanic_transplanted': /Users/guillermo/organproject/OrganProject/static/images/hispanic_transplanted.png,
    #     'black_wait': /Users/guillermo/organproject/OrganProject/static/images/black_wait.png,
    #     'black_transplanted': /Users/guillermo/organproject/OrganProject/static/images/black_transplanted.png, 
    #     }]
    return render_template("Research.html")

@app.route("/Users/guillermo/organproject/OrganProject/Guillermo-HTML/Testimonies.html")
def testimonies():
    return render_template("Testimonies.html")


# I need other routes to return html for other pages
# Or create 1 other route and match the path of the route to one of the files
# ^^ Make a variable & return an html page based on the vriable

if __name__ == '__main__':
    app.run(debug = True)


