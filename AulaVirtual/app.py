from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/aula_virtual_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Ejemplo de un modelo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return "conectao a la base de dato"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


import pymysql
pymysql.install_as_MySQLdb()
