from flask import request, render_template, redirect\
    , url_for, current_app as app
from .import bp as app

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')