import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)
 

@app.route("/")
@app.route("/home")
def home():
    """
    Renders Home Page
    """
    resources = mongo.db.resources.find()
    return render_template("index.html", resources=resources)
    

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the email is already in use
        registered_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if  registered_user:
            flash("Email already in use", "error")
            return redirect(url_for("register"))
        # Create a New Account
        newuseraccount = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # add account to the database
        mongo.db.users.insert_one(newuseraccount)
        # put the new user into 'session' cookie
        session["user_email"] = request.form.get("email").lower()
        flash("Account Successfully Created!", "correct")
        return redirect(url_for("profile", user_email=session["user_email"]))
    return render_template("register.html")


# fix it
@app.route("/search", methods=["GET", "POST"])
def search():
    # queries
    query = request.form.get("query")
    resources = list(mongo.db.resources.find({"$text": {"$search": query}}))
    # resources_list & users are for welcome screen for users that are not logged in
    # check for search results
    if len(resources) == 0:
        flash("No results, Please try again!", "error")
        return redirect(url_for("home"))
    return render_template(
        "index.html", resources=resources)


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check for existing account
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user["password"], request.form.get("password")):
                session["user_email"] = request.form.get("email").lower()
                # return first name and surname
                flash("Welcome, {0} {1}".format(
                    existing_user["first_name"].capitalize(),
                    existing_user["last_name"].capitalize()))
                return redirect(url_for(
                    "profile", user_email=session["user_email"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", "error")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            ("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


# Logout 
@app.route("/logout")
def logout():
    # remove user session and redirect to the login page
    if 'user_email' in session:
        flash("You logged out succesfully", "correct")
        session.pop("user_email")
        return redirect(url_for("home"))
    return render_template('home.html')


# Profile 
@app.route("/profile/<user_email>", methods=["GET", "POST"])
def profile(user_email):
    if 'user_email' in session:
        # grab all users list & the session user's email from database
        resources = list(mongo.db.resources.find())
        users = list(mongo.db.users.find())
        email = mongo.db.users.find_one(
            {"email": session["user_email"]})["email"]
        return render_template(
                "profile.html", user_email=email, users=users, resources=resources)
    return redirect(url_for("home"))


# resources 
@app.route("/resources")
def resources():
    resources = list(mongo.db.resources.find())
    # 8 items per page

    def get_resources(offset=0, per_page=8):
        return resources[offset: offset + per_page]
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    # check length
    total = len(resources)
    # render up to 8 resources 
    paginate_resources = get_resources(offset=offset, per_page=per_page)
    resourcespagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template("resources.html", resources=paginate_resources, page=page,
                           per_page=per_page, resourcespagination=resourcespagination,)


# New resource route
@app.route("/new_resource", methods=["GET", "POST"])
def new_resource():
    if 'user_email' in session:
        # get data from html form
        if request.method == "POST":
            resource = {
                "name": request.form.get("name"),
                "resource_category": request.form.get("resource_category"),
                "description": request.form.get("description"),
                "created_by": session["user_email"],
                "image": request.form.get("image"),
                "timestamp": datetime.now()
            }
            # insert resource on the database
            mongo.db.resources.insert_one(resource)
            email = session['user_email']
            flash("New Resource Successfully Added", "correct")
            return redirect(url_for("profile", user_email=email))
        # read data and sort in ascending order
        resource_category = mongo.db.resource_type.find().sort("resource_category", 1)
        return render_template("new_resource.html", resource_category=resource_category)
    return redirect(url_for("login"))


# Edit resource
@app.route("/edit_resource/<id>", methods=["GET", "POST"])
def edit_resource(id):
    if 'user_email' in session:
        # retrieve data from form
        if request.method == "POST":
            resource_edit = {
                "name": request.form.get("name"),
                "resource_category": request.form.get("resource_category"),
                "description": request.form.get("description"),
                "created_by": session["user_email"],
                "image": request.form.get("image"),
                "timestamp": datetime.now()
            }
            # update resource in DDBB
            mongo.db.resources.update({"_id": ObjectId(id)}, resource_edit)
            email = session['user_email']
            flash("resource details updated", "correct")
            return redirect(url_for("profile", user_email=email))
        resource = mongo.db.resources.find_one({"_id": ObjectId(id)})
        # read data and sort ascendingly
        resource_category = mongo.db.resource_type.find().sort("resource_category", 1)
        return render_template("edit_resource.html", resource_category=resource_category)
    return redirect(url_for("login"))


# Delete resource route
@app.route("/delete_resource/<id>")
def delete_resource(id):
    # allow users to delete resources if they are logged in
    if 'user_email' in session:
        mongo.db.resources.remove({"_id": ObjectId(id)})
        flash("resource deleted", "correct")
        # administrators are allowed to delete all resources 
        if session['user_email'] == "admin@topdevresources.com":
            return redirect(url_for("resources"))
        # if user redirect to users profile
        else:
            return redirect(url_for(
                "profile", user_email=session["user_email"]))


@app.route("/contact")
def contact():
    """
    Renders contact page
    """
    return render_template("contact.html")


@app.route("/aboutus")
def aboutus():
    """
    Renders About page
    """
    return render_template("aboutus.html")


@app.errorhandler(404)
def not_found_error(error):
    """
    404 error
    """
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Route to 500 Error
    """
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)