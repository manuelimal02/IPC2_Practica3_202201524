from flask import Flask
from flask_cors import CORS
from pelicula.pelicula_DAO import pelicula_DAO
from flask.globals import request
from flask.json import jsonify

manejador_pelicula=pelicula_DAO()
app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "<h1>Sevidor Levantado</h1>"

@app.route("/api/add-movie", methods=['POST'])
def agregar_pelicula():
    respuesta = {}
    nombre = request.json['name']
    genero = request.json['genre']
    if manejador_pelicula.nueva_pelicula(nombre, genero):
        respuesta = {
            "Estado": "Agregado",
            "Mensaje": f"Película: {nombre} Agregada Correctamente."
        }
        return jsonify(respuesta)
    else:
        respuesta = {
            "Estado": "No Agregado",
            "Mensaje": f"La Película: {nombre} Ya Fue Agregada."
        }
        return jsonify(respuesta)

@app.route("/api/all-movies-by-genre/<genero>", methods=['GET'])
def peliculas_por_genero(genero):
    return manejador_pelicula.pelicula_por_genero(genero)

@app.route("/api/update-movie", methods=['PUT'])
def actualizar_peliculas():
    respuesta = {}

    nombre = request.json['name']
    genero = request.json['genre']
    
    if manejador_pelicula.actualizar_pelicula(nombre, genero):
        respuesta = {
            "Estado": "Actualizado",
            "message": f"Película: {nombre} Actualizada Correctamente."
            }
        return jsonify(respuesta)
    else:
        respuesta = {
            "Estado": "Error",
            "Mensaje": f"No Existe La Película: {nombre}."
            }
        return jsonify(respuesta)

if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)