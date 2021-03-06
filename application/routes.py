from flask import render_template, redirect, url_for
from application import app, db
from application.models import Food, Recipe
from application.forms import FoodForm, RecipeForm, UpdateFoodForm

@app.route('/')
@app.route('/home')
def home():
    foodData = Food.query.all()
    return render_template('home.html', title='Home', food=foodData)

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    form = RecipeForm()
    if form.validate_on_submit():
        recipeData = Recipe(
            name = form.recipe_name.data,
        )

        db.session.add(recipeData)
        db.session.commit()
        return redirect(url_for('home'))


    return render_template('recipes.html', title='Recipe', form=form)

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


@app.route('/fridge/<food_name>', methods=['GET', 'POST'])
def delete_fridge(food_name):
    deleteme = Food.query.filter_by(name=food_name).first()
    db.session.delete(deleteme)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/updatefridge/<food_name>', methods=['GET', 'POST'])
def update_fridge(food_name):
    form = UpdateFoodForm()
    if form.validate_on_submit():
        newfoodData = Food(
            name = form.food_name.data,
        )
        deleteme = Food.query.filter_by(name=food_name).first()
        db.session.delete(deleteme)
        db.session.add(newfoodData)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('updatefridge.html', title='Update Fridge', form=form)


