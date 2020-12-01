from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/works")
def works():
    return render_template("works.html")


@app.route("/work")
def work():
    return render_template("work.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/components")
def components():
    return render_template("components.html")


@app.route("/*")
def not_found():
    return "not found"
