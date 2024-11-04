# app/routes.py
from flask import render_template, redirect, url_for, flash, request
from . import db
from .models import User
from .forms import RegistroForm
from flask_login import login_user, logout_user

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistroForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuario registrado con éxito.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
