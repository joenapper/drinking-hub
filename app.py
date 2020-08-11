import math
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Define the app, and set the MONGO_URI secret key
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


# Landing Page
@app.route('/')
def home():
    liquors = mongo.db.liquors.find()
    return render_template('index.html', liquors=liquors)


# Shows all drinks / cocktails
@app.route('/get_drinks')
def get_drinks():
    liquors = mongo.db.liquors.find()
    # Pagination & display settings
    current_page = int(request.args.get('current_page', 1))
    total_drinks = mongo.db.drinks.count()
    drinks_per_page = 9
    num_pages = range(1, int(math.ceil(total_drinks / drinks_per_page)) + 1)
    drinks = mongo.db.drinks.find().sort('_id', -1).skip(
        (current_page - 1) * drinks_per_page).limit(drinks_per_page)

    x = current_page * drinks_per_page
    first_result_num = x - drinks_per_page + 1
    last_result_num = x if x < total_drinks else total_drinks

    return render_template('drinks.html',
                           drinks=drinks,
                           liquors=liquors,
                           current_page=current_page,
                           pages=num_pages,
                           first_result_num=first_result_num,
                           last_result_num=last_result_num,)


# Search for recipes with regex method
# Results of the search returned with the for loop in searched.html
@app.route("/find_cocktails")
def find_cocktails():
    query = request.args.get("search").capitalize()
    search_term = mongo.db.drinks.find({"liquors": {"$regex": query}})
    search = search_term
    no_of_docs = mongo.db.recipes.count_documents(
        {"liquors": {"$regex": query}})
    return render_template("searched.html",
                           search=search_term,
                           no_of_docs=no_of_docs)


# Displays all content for selected cocktail
@app.route('/display_cocktail/<drink_id>')
def display_cocktail(drink_id):
    drinks = mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    # Uses .split() method to display ingredients
    ingredients = drinks["ingredients"].split(",")
    liquors = drinks['liquors'].split(",")
    return render_template('cocktail_page.html',
                           drinks=drinks,
                           ingredients=ingredients,
                           liquors=liquors)


# Add cocktail page
@app.route('/add_cocktail')
def add_cocktail():
    return render_template('add_cocktail.html',
                           liquors=mongo.db.liquors.find())


# Adds new recipe using a form and POST method
@app.route('/insert_cocktail', methods=['POST'])
def insert_cocktail():
    drinks = mongo.db.drinks
    drinks.insert_one(request.form.to_dict())
    # Redirects user to cocktail list
    return redirect(url_for('get_drinks'))


# Find the recipe by its ID then render the edit_cocktail.html file
@app.route('/edit_cocktail/<drink_id>')
def edit_cocktail(drink_id):
    drinks = mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    # Uses .split() method to display ingredients
    ingredients = drinks["ingredients"].split(",")
    liquors = drinks['liquors'].split(",")
    return render_template('edit_cocktail.html',
                           drinks=drinks,
                           ingredients=ingredients,
                           liquors=liquors)


# Update the article after editing it using JSON
@app.route('/update_cocktail/<drink_id>', methods=['POST'])
def update_cocktail(drink_id):
    drinks = mongo.db.drinks
    drinks.update({'_id': ObjectId(drink_id)},
                  {
        'liquors': request.form.get('liquors'),
        'name': request.form.get('name'),
        'image': request.form.get('image'),
        'ingredients': request.form.get('ingredients'),
        'notes': request.form.get('notes')
    })
    # When the cocktail is updated, redirect the user to the cocktail list
    return redirect(url_for('get_drinks'))


# Find a recipe by its ID then remove it from the database
@app.route('/delete_cocktail/<drink_id>')
def delete_cocktail(drink_id):
    mongo.db.drinks.remove({'_id': ObjectId(drink_id)})
    # Redirects to cocktail list to confirm deletion to the user
    return redirect(url_for('get_drinks'))


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/privacypolicy')
def privacy_policy():
    return render_template('priv-pol.html')


# Host,Port and Debug set
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
