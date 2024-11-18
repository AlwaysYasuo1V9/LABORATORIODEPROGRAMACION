from flask import Flask
from flask_login import LoginManager
from models.user import db, User
from routes import main_routes, auth_routes
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(main_routes.bp)
app.register_blueprint(auth_routes.bp, url_prefix='/auth')


with app.app_context():
    db.create_all()
   
    if not User.query.filter_by(username='lucas@gmail.com').first():
        hashed_password = bcrypt.generate_password_hash('123456').decode('utf-8')
        new_user = User(username='lucas@gmail.com', password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print("Initial user created - Email: lucas@gmail.com, Password: 123456")

if __name__ == '__main__':
    app.run(debug=True)