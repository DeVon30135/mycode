#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to
@app.route("/correct")
def correct():
    return "CORRECT!\n"

@app.route("/")
@app.route("/start")
def start():
    return render_template("quizmaker.html")

@app.route("/try_again")
def try_again():
    return render_template("try_again.html")

@app.route("/answer", methods = ["POST", "GET"])
def answer():
    if request.method == "POST":
        solution = request.form.get("nm").lower()
        if solution == "blue" or solution == "blue paint":
            correct = True
        else:
            correct = False
    
    elif request.method == "GET":
        solution = request.args.get("nm")
        if solution == "red" or solution == "red paint":
            correct = True
        else:
            correct = False
    if correct:
        return redirect(url_for("correct"))
    else:
        return redirect(url_for("try_again"))


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

