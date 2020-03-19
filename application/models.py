from application import db

ingredients = db.Table('ingredients',
        db.Column('food_id', db.ForeignKey('food.food_id')),
        db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.recipe_id')))

class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(20))
    component = db.relationship('Recipe', secondary=ingredients, backref=db.backref('ingredients_1', lazy = 'dynamic'))

class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
