import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_drinks')
def get_drinks():
    return render_template('drinks.html', drinks=mongo.db.drinks.find())


@app.route('/display_cocktail/<drink_id>')
def display_cocktail(drink_id):
    drinks = mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    ingredients = drinks["ingredients"]
    return render_template('cocktail_page.html', drinks=drinks, ingredients=ingredients)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)