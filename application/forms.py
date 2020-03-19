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
