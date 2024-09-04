from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def principal():
    frutas = ["morango", "Uva", "Maça", "Laranja"]
    return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
    notas = {"aluno1": 5, "aluno2": 6, "aluno3": 7, "aluno4": 8}
    return render_template("sobre.html", notas=notas)

if __name__ == '__main__':
      app.run(port=8084, host='0.0.0.0', debug=True, threaded=True)