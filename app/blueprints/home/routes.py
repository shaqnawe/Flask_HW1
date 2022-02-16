from flask import request, render_template, redirect, url_for
from .import bp as app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')