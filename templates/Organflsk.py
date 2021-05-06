from flask import Flask, render_template

app = Flask(__name__)
<<<<<<< HEAD
=======

>>>>>>> 54918f49675bfedc8bc568056e1f5e37d9b84cdd
@app.route("/")
def home():
    return render_template("index1.html")

if __name__ == '__main__':
    app.run()
<<<<<<< HEAD

#import datetime

#x = datetime.datetime.now()
#print(x)
=======
>>>>>>> 54918f49675bfedc8bc568056e1f5e37d9b84cdd
