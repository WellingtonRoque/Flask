from flask import Flask, render_template, request

app = Flask(__name__)

frutas=[]

#adicionar os metodos HTTP GET e POST para manipular o servidor
@app.route('/', methods=["GET", "POST"])
def principal():
    #frutas = ["morango", "Uva", "Maça", "Laranja"]
    #frutas=[]
    if request.method == "POST":      #verifica se o metodo chamado == POST
        if request.form.get("fruta"): #verifica se o campo fruta foi preenchido
            frutas.append(request.form.get("fruta")) #inclui valores no final da lista
    return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
    notas = {"aluno1": 5, "aluno2": 6, "aluno3": 7, "aluno4": 8}
    return render_template("sobre.html", notas=notas)

if __name__ == '__main__':
      app.run(port=8084, host='0.0.0.0', debug=True, threaded=True)