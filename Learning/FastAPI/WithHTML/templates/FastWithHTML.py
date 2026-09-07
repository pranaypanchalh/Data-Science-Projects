from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/")
def welcomePage():
    name = request.args.get("name")
    surname = request.args.get("surname")
    language = request.args.get("language")
    return render_template("index.html", name=name, surname=surname, language=language)

app.run(debug=True)
