from flask import render_template, redirect, url_for
from application import app, db
from application.models import Food
from application.forms import FoodForm

@app.route('/')
@app.route('/home')
def home():
    foodData = Food.query.first()
    return render_template('home.html', title='Home', food=foodData)

@app.route('/recipes')
def recipes():
 return render_template('recipes.html', title='recipes')

@app.route('/fridge', methods=['GET', 'POST'])
def fridge():
    form = FoodForm()
    if form.validate_on_submit():
        foodData = Food(
            name = form.food_name.data,
        )

        db.session.add(foodData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('fridge.html', title='Fridge', form=form)
