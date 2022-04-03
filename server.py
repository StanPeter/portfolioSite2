from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import csv

app = Flask(__name__)

load_dotenv()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact(is_form="show"):
    if request.args:
        is_form = request.args["is_form"]

    return render_template("contact.html", is_form=is_form)


def write_to_file(data):
    with open("tempDatabase.txt", mode="a") as db:
        email = data["email"]
        subject = data["subject"]
        text = data["text"]
        file = db.write(f"\n{email},{subject},{text}")


def write_to_csv(data):
    with open("tempDatabase.csv", newline='', mode="a") as db:
        email = data["email"]
        subject = data["subject"]
        text = data["text"]
        csv_writer = csv.writer(
            db, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, text])
    pass


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)

            return redirect(url_for("contact", is_form="hide"))
        except:
            return 'Did not save correctly'
    return redirect("/")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found.html")
