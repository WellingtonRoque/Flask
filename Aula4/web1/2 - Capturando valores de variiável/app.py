from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def principal():
    nome = "Joaquim"
    idade = 23
    #------------------
    fruta1 = "morango"
    fruta2 = "Uva"
    fruta3 = "Maça"
    fruta4 = "Laranja"


    return render_template("index.html", nome=nome, idade=idade)
    """
    return render_template("index.html",
                            fruta1=fruta1,
                            fruta2=fruta2,
                            fruta3=fruta3,
                            fruta4=fruta4)
    """



if __name__ == "__main__":
    app.run(debug=True)