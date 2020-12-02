from flask import Flask, render_template, request, redirect, url_for
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
def contact(is_form="show"):

    if request.args:
        is_form = request.args["is_form"]

    print(is_form, "is_form")
    return render_template("contact.html", is_form=is_form)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    error = None
    if request.method == "POST":
        data = request.form.to_dict()

        print(data, "dataDDDDDDDDDDDDDDDD")
        return redirect(url_for("contact", is_form="hide"))
    else:
        return redirect("/")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html")
