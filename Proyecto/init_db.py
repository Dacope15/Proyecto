from app import app, db

with app.app_context():
    db.create_all()
    print("Tablas creadas exitosamente en la base de datos.")