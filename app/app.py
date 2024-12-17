from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto'

# Configuración correcta de la URI de conexión
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/flask_crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de SQLAlchemy
db = SQLAlchemy(app)

# Modelo de ejemplo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Formulario de Login utilizando WTForms
class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])

# Ruta para la página de login
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Aquí iría la lógica para verificar el usuario y la contraseña en la base de datos
        return redirect(url_for('welcome'))  # Redirigir a la página de bienvenida después de login

    return render_template('login.html', form=form)

# Ruta de bienvenida (después de login)
@app.route('/welcome')
def welcome():
    return "Ya estas logeado"

# Crear las tablas
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
