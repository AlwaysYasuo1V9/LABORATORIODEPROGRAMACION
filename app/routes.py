from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, User, Course
from flask_login import login_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica para el login
    pass

@main.route('/register', methods=['GET', 'POST'])
def register():
    # Lógica para el registro
    pass

@main.route('/courses', methods=['GET', 'POST'])
@login_required
def courses():
    # Lógica para gestionar cursos
    pass
