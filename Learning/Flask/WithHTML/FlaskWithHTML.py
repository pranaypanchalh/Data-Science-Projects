from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcomePage():
    name = "Pranay"
    surname = "Panchal"
    language = "Python"
    return render_template("index.html", name=name, surname=surname, language=language)

app.run(debug=True)
