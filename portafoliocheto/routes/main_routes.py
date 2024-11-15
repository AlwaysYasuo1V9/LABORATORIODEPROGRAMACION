from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    projects = [
        {
            'title': 'Project 1',
            'description': 'A web application built with Flask',
            'image': 'project1.jpg'
        },
        {
            'title': 'Project 2',
            'description': 'Mobile app development',
            'image': 'project2.jpg'
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