from flask_wtf import FlaskForm
from wtforms import SubmitField


class TypeForm(FlaskForm):
    restaurant = SubmitField()
    fast_food = SubmitField()


class FastFoodForm(FlaskForm):
    mcdonalds = SubmitField()
    wendys = SubmitField()
    harveys = SubmitField()
    burger_king = SubmitField()
    aw = SubmitField()


class RestaurantForm(FlaskForm):
    vietnamese = SubmitField()
    chinese = SubmitField()
    indian = SubmitField()
    japanese = SubmitField()
    thai = SubmitField()
    seafood = SubmitField()
    sushi = SubmitField()
    hamburger = SubmitField()
    pizza = SubmitField()
    french = SubmitField()
    italian = SubmitField()
    mexican = SubmitField()
    middle_eastern = SubmitField()

class SearchForm(FlaskForm):
    search_results = SubmitField()
