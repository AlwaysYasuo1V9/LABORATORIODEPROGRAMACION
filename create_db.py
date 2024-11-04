from app import create_app, db

app = create_app()
with app.app_context():
    db.create_all()  # Esto creará las tablas definidas por tus modelos

    # Agregar un nuevo usuario
    new_user = User(username='nuevo_usuario', email='nuevo@correo.com')
    db.session.add(new_user)
    db.session.commit()
