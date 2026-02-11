from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/q1")
def q1():
    return render_template("q1.html")

@app.route("/correct_q1")
def correct_q1():
    return render_template("correct_q1.html")

@app.route("/q2")
def q2():
    return render_template("q2.html")

@app.route("/correct_q2")
def correct_q2():
    return render_template("correct_q2.html")

@app.route("/q3")
def q3():
    return render_template("q3.html")

@app.route("/wrong")
def wrong():
    return render_template("wrong.html")

@app.route("/final")
def final():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)