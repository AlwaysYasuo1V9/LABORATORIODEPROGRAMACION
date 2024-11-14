from flask import Blueprint, render_template, redirect, url_for
from forms.login_form import LoginForm

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Aquí iría la lógica de autenticación
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form, title="Iniciar sesión")
