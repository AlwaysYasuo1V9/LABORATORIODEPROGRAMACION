from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    projects = [
        {
            'title': 'Aula virtual',
            'description': 'Este es un proyecto que consiste en hacer un aula virtual que podria ser utilizada por alguna institucion ya sea como alumno o profesor',
            'image': 'aulavirtual.png'
            
        },
        {
            'title': 'Generador de laberintos',
            'description': 'Este proyecto consiste en un algoritmo que crea laberintos de forma aleatoria que siempre tienen entrada y salida, que podria ser utilizado para algun videojuego',
            'image': 'laberinto.png'
        }
    ]
    return render_template('index.html', title='Portfolio', projects=projects)

@bp.route('/bio')
def bio():
    schedule = {
        'Monday': '9:00 AM - 5:00 PM',
        'Tuesday': '9:00 AM - 5:00 PM',
        'Wednesday': '9:00 AM - 5:00 PM',
        'Thursday': '9:00 AM - 5:00 PM',
        'Friday': '9:00 AM - 4:00 PM'
    }
    return render_template('bio.html', title='Bio', schedule=schedule)