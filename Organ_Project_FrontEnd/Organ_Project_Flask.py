from flask import Flask, render_template



@app.route('/')
def index():
    return render_template('Staticpage_Charts_graphs.html')


