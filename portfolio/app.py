from flask import Flask
from models.user import db, User  # Aquí se importa también el modelo User
from routes import main_routes, auth_routes
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'  # Base de datos SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app)

# Inicializar la base de datos
db.init_app(app)

# Registrar rutas
app.register_blueprint(main_routes.bp)
app.register_blueprint(auth_routes.bp)

# Crear usuario inicial
with app.app_context():
    db.create_all()
    # Crear un usuario inicial si no existe
    if not User.query.filter_by(username='lucas@gmail.com').first():
        hashed_password = bcrypt.generate_password_hash('123456').decode('utf-8')
        new_user = User(username='lucas@gmail.com', password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print("Usuario inicial creado: lucas@gmail.com / Contraseña: 123456")

if __name__ == '__main__':
    app.run(debug=True)
