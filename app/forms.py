from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Formulario de Login
class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

# Formulario CRUD
class ItemForm(FlaskForm):
    name = StringField('Nombre del ítem', validators=[DataRequired()])
    submit = SubmitField('Guardar')
