# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app
# define routes for / & /home, this function will be called when these are accessed
from application.models import Food

@app.route('/')
@app.route('/home')
def home():
    foodData = Food.query.first()
    return render_template('home.html', title='Home', food=foodData)

@app.route('/about')
def about():
 return render_template('about.html', title='about')
