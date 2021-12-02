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
@app.route("/incorrect/<answer>")
def incorrect(answer=False):
    print(answer)
    return render_template("quiz_flask.html", solution = answer)


@app.route("/answer", methods = ["POST"])
def answer():
    print(f"REQUEST JSON: {help(request)}")
    correct = False
    if request.json:
        print(request.json)
        solution = request.json["answer"].lower()
        if solution == "blue" or solution == "blue paint":
            correct = True

    if correct:
        return redirect(url_for("correct"))
    else:
        return redirect(url_for("incorrect", answer = solution))


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

