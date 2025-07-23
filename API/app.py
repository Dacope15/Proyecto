from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="soporte_db"
    )

@app.route('/', methods=['GET'])
def mostrar_datos():
    filtro = request.args.get('buscar', default='', type=str)

    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)

    if filtro:
        query = "SELECT * FROM casos WHERE titulo LIKE %s OR descripcion LIKE %s OR estado LIKE %s"
        cursor.execute(query, (f"%{filtro}%", f"%{filtro}%", f"%{filtro}%"))
    else:
        cursor.execute("SELECT * FROM casos")

    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template('index.html', resultados=datos, buscar=filtro)

if __name__ == '__main__':
    app.run(debug=True)