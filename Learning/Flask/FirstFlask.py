from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcomePage():
    return "<p>Welcome to Flask</p>"


@app.route("/page<int:i>")
def page(i):
    return f"<p>This is {i}</p>"


app.run(debug=True)