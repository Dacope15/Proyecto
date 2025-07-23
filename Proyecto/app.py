from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/soporte_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Caso(db.Model):
    __tablename__ = 'casos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text, nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    estado = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return f"<Caso {self.id} - {self.titulo}>"

@app.route('/crear-caso', methods=['GET', 'POST'])
def crear_caso():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        estado = 'pendiente'  # Estado por defecto
        nuevo_caso = Caso(titulo=titulo, descripcion=descripcion, estado=estado)
        db.session.add(nuevo_caso)
        db.session.commit()
        return redirect(url_for('crear_caso'))

    casos = Caso.query.order_by(Caso.fecha_creacion.desc()).all()
    return render_template('crear_caso.html', casos=casos)


if __name__ == '__main__':
    app.run(debug=True)