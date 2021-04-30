import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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
            flash("Email already in use")
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
        flash("Account Successfully Created!")
        return redirect(url_for("profile", user_email=session["user_email"]))
    return render_template("register.html")


# fix it
@app.route("/search", methods=["GET", "POST"])
def search():
    # queries
    query = request.form.get("query")
    resources = list(mongo.db.resources.find({"$text": {"$search": query}}))
    # resources_list & users are for welcome screen for users that are not log in
    resources_list = list(mongo.db.resources.find())
    users = list(mongo.db.users.find())
    # check for search results
    if len(resources) == 0:
        flash("No results, Please try again!")
        return redirect(url_for("home"))
    return render_template(
        "home.html", resources=resources, resources_list=resources_list, user_list=users)


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
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/signout")
def signout():
    """
    Returns user to the Log In Page
    """
    flash("You have logged out", 'message')
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/catalog")
def catalog():
    """
    Renders contact page
    """
    resources = mongo.db.resources.find()
    return render_template("catalog.html", resources=resources)


@app.route("/contact")
def contact():
    """
    Renders contact page
    """
    return render_template("contact.html")


@app.errorhandler(404)
def not_found_error(error):
    """
    404 error
    """
    return render_template('404.html', error=error), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)