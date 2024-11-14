from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title="Inicio")

@bp.route('/about')
def about():
    return render_template('base.html', title="Sobre mí")
