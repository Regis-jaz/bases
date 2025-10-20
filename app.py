from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', title="Inicio")

@app.route('/animales')
def animales():
    return render_template('animales.html', title="Animales Exóticos")

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html', title="Vehículos Antiguos")

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html', title="Las Maravillas del Mundo")

@app.route('/acerca')
def acerca():
    return render_template('acerca.html', title="Acerca de...")

@app.route('/sesion', methods=["GET", "POST"])
def sesion():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        fechadenacimiento = request.form["fechadenacimiento"]
        genero = request.form["genero"]
        email = request.form["email"]
        password = request.form["password"]
        repassword = request.form["repassword"]

        if password != repassword:
            flash("Las contraseñas no coinciden", "danger")
        else:
            flash(f"Registro exitoso para {nombre} {apellido}", "success")

    return render_template("sesion.html")

if __name__ == '__main__':
    app.run(debug=True)