import json
from flask import Flask, render_template, redirect, url_for, request
from forms import TypeForm, FastFoodForm, RestaurantForm, SearchForm
from search_api import search
import os

from dotenv import load_dotenv


load_dotenv()

user_info = {
    "restaurant_choice": "",
    "latitude": "",
    "longitude": ""
}

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/type", methods=["GET", "POST"])
def type():
    form = TypeForm()

    if form.validate_on_submit():
        if form.restaurant.data:
            return redirect(url_for("restaurants"))
        elif form.fast_food.data:
            return redirect(url_for("fast_foods"))

    return render_template("type.html", form=form)


@app.route("/restaurants", methods=["GET", "POST"])
def restaurants():
    form = RestaurantForm()

    if form.validate_on_submit():
        if form.chinese.data:
            user_info["restaurant_choice"] = "chineserestaurants"
        elif form.french.data:
            user_info["restaurant_choice"] = "frenchrestaurants"
        elif form.hamburger.data:
            user_info["restaurant_choice"] = "hamburgerrestaurants"
        elif form.indian.data:
            user_info["restaurant_choice"] = "indianrestaurants"
        elif form.italian.data:
            user_info["restaurant_choice"] = "italianrestaurants"
        elif form.japanese.data:
            user_info["restaurant_choice"] = "japaneserestaurants"
        elif form.mexican.data:
            user_info["restaurant_choice"] = "mexicanrestaurants"
        elif form.middle_eastern.data:
            user_info["restaurant_choice"] = "middleeasternrestaurants"
        elif form.pizza.data:
            user_info["restaurant_choice"] = "pizzarestaurants"
        elif form.seafood.data:
            user_info["restaurant_choice"] = "seafoodrestaurants"
        elif form.sushi.data:
            user_info["restaurant_choice"] = "sushirestaurants"
        elif form.thai.data:
            user_info["restaurant_choice"] = "thairestaurants"
        elif form.vietnamese.data:
            user_info["restaurant_choice"] = "vietnameserestaurants"
        return redirect(url_for("location"))

    return render_template("restaurants.html", form=form)


@app.route("/fast_foods", methods=["GET", "POST"])
def fast_foods():
    form = FastFoodForm()

    if form.validate_on_submit():
        if form.mcdonalds.data:
            user_info["restaurant_choice"] = "McDonald's"
        elif form.wendys.data:
            user_info["restaurant_choice"] = "Wendy's"
        elif form.harveys.data:
            user_info["restaurant_choice"] = "Harvey's"
        elif form.burger_king.data:
            user_info["restaurant_choice"] = "Burger King"
        elif form.aw.data:
            user_info["restaurant_choice"] = "AWCanada"
        return redirect(url_for("location"))

    return render_template("fast_foods.html", form=form)


@app.route("/location", methods=["GET", "POST"])
def location():
    form = SearchForm()

    if form.validate_on_submit():
        restaurants = search(user_info["restaurant_choice"], user_info["latitude"], user_info["longitude"])
        return render_template("results.html", restaurants=restaurants)
    
    return render_template("location.html", form=form)

@app.route("/grab_location", methods=["POST"])
def grab_location():
    json_output = request.get_json()
    python_output = json.loads(json_output)
    user_info["latitude"] = str(python_output["latitude"])
    user_info["longitude"] = str(python_output["longitude"])
    return python_output


if __name__ == "__main__":
    app.run(debug=True)
