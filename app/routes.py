from app import app

@app.route('/')
@app.route('/index')
def index():
    # return "Hello, Michał Fedorek!"
    return render_template("house.html")
# @app.route('/name/',defaults={'name':"Anonim"})
# @app.route('/name/<name>')
# def name(name = None):
#     return f"Hello, {name}!"

@app.route('/ekstrakcja-opini')
def ekstrakcja():
    return render_template("Ekstrakcja_opnii.html")

@app.route('/lista-produktow')
def lista_produktow():
    return render_template("Lista-produktów.html")

@app.route('/o-autorze')
def author():
    return render_template("autor.html")
@app.route('/produkt')
def produkt():
    return render_template("produkt.html")
@app.route('/wykresy')
def wykresy():
    return render_template("wykresy.html")