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
    return render_template("register.html")


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