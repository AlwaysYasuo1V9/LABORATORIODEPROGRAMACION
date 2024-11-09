from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'  # Cambia esta clave por una más segura

# Lista de usuarios simulada con contraseñas hasheadas
usuarios = {
    'lucas@gmail.com': generate_password_hash('123456')  # Contraseña hasheada
}

@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        return render_template('index.html', title="AULA VIRTUAL", materias=['Matematica', 'Historia', 'Lengua', 'Biología', 'Programacion', 'Laboratorio de programacion', 'Sistemas y telecomunicaciones', 'Base de datos'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Verificar si el usuario existe y si la contraseña es correcta
        if email in usuarios and check_password_hash(usuarios[email], password):  # Usamos check_password_hash para verificar el hash
            session['logged_in'] = True
            session['user'] = email
            return redirect(url_for('index'))
        else:
            return "Correo o contraseña incorrectos", 401  # Mensaje de error si las credenciales son incorrectas
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
