from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    frutas = ["morango", "Uva", "Maça", "Laranja"]
    return render_template("index.html", frutas=frutas)

if __name__ == "__main__":
    app.run(debug=True)