from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class FoodForm(FlaskForm):
    food_name = StringField('Food name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    
    submit = SubmitField('Add to fridge!')

class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe name',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    submit = SubmitField('Add to recipe book!')


class UpdateFoodForm(FlaskForm):
    food_name = StringField('food name',
        validators=[
            DataRequired(),
            Length(min=3, max=20)
        ]) 
    submit = SubmitField('Update')

