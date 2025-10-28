from flask import Flask, render_template, request, flash, g, redirect, url_for

app = Flask(__name__)

app.secret_key = 'tu_clave_secreta_aqui'

@app.before_request
def load_logged_in_user():
    """Simula la carga del estado de la sesión antes de cada solicitud."""

    g.user_logged_in = False 

@app.context_processor
def inject_user():
    """Inyecta la variable user_logged_in en todas las plantillas."""
    return dict(user_logged_in=g.user_logged_in) 

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
        password = request.form["password"]
        repassword = request.form["repassword"]

        if password != repassword:
            flash("Las contraseñas no coinciden. Inténtalo de nuevo.", "danger")
        else:
            flash(f"¡Registro exitoso! Bienvenido/a {nombre} {apellido}. ¡Ahora puedes iniciar sesión!", "success")

            return redirect(url_for('login')) 
            
    return render_template("sesion.html", title="Registro de Cuenta")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == "test@ejemplo.com" and password == "123":
            g.user_logged_in = True
            flash(f"¡Bienvenido de nuevo, {email}!", "success")
            return redirect(url_for('inicio')) 
        else:
            flash("Error de inicio de sesión. Email o contraseña incorrectos.", "danger")

    return render_template("login.html", title="Iniciar Sesión")

@app.route('/perfil')
def perfil():
    g.user_logged_in = True 
    return render_template('perfil.html', title="Mi Perfil")

@app.route('/logout')
def logout():
    flash("👋 Has cerrado sesión correctamente.", "info")
    return redirect(url_for('inicio')) 


if __name__ == '__main__':
    app.run(debug=True)