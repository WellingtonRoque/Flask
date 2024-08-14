from flask import Flask, render_template

app = Flask(__name__)
"""
@app.route('/')
def principal():
    return render_template("home.html")

@app.route('/')
def principal():
    return render_template("css1.html")
    
@app.route('/')
def principal():
    return render_template("css2.html")
"""
@app.route('/')
def principal():
    return render_template("css3.html")

if __name__ == "__main__":
    app.run(debug=True)

"""
- Download de imagem
https://unsplash.com/pt-br
https://www.freeimages.com/pt
https://www.pexels.com/pt-br/
-------------------------------------------
- Conteudo sobre CSS
https://www.w3schools.com/css/default.asp

- RGB - online
https://www.rapidtables.com/web/color/RGB_Color.html
"""

