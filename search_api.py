from lib2to3.pytree import convert
import requests
import os
import json

from dotenv import load_dotenv


load_dotenv()


def validate_keys(key, dictionary):
    if key == "opening_hours":
        if key not in dictionary:
            dictionary[key] = {"open_now": "N/A"}
        elif dictionary[key] == {}:
            dictionary[key] = {"open_now": "N/A"}

    if key not in dictionary:
        dictionary[key] = "N/A"


def convert_price_level(dictionary):
    if dictionary["price_level"] == 1:
        dictionary["price_level"] = "$"
    elif dictionary["price_level"] == 2:
        dictionary["price_level"] = "$$"
    elif dictionary["price_level"] == 3:
        dictionary["price_level"] = "$$$"
    elif dictionary["price_level"] == 4:
        dictionary["price_level"] == "$$$$"


def clean_results(response):
    # assign json results to variable
    api_json = response.text

    # convert json object to Python dictionary
    api_dict = json.loads(api_json)

    # store value of "results" key i.e. a list of the restaurants, inside a variable
    restaurants = api_dict["results"]

    # delete all useless keys in every dictionary
    collection_rest = []
    for i in restaurants:

        validate_keys("business_status", i)
        validate_keys("opening_hours", i)
        validate_keys("price_level", i)
        validate_keys("rating", i)
        validate_keys("user_ratings_total", i)

        convert_price_level(i)

        restaurant = {
            "business_status": i["business_status"],
            "formatted_address": i["formatted_address"],
            "name": i["name"],
            "opening_hours": i["opening_hours"]["open_now"],
            "price_level": i["price_level"],
            "rating": i["rating"],
            "user_ratings_total": i["user_ratings_total"],
        }

        collection_rest.append(restaurant)

    return collection_rest


def search(name, latitude, longitude):
    url = (
        "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
        + name
        + "&location="
        + latitude
        +","
        + longitude
        + "&key="
        + os.environ.get("API_KEY")
    )

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    search_results = clean_results(response)

    return search_results
