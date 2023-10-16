from pelicula.pelicula import pelicula
from flask.json import jsonify
import json


class pelicula_DAO:
    def __init__(self):
        self.peliculas = []
        self.id_pelicula=1

    def nueva_pelicula(self, nombre, genero):
        for movie in self.peliculas:
            if movie.nombre == nombre:
                return False
        nueva_pelicula = pelicula(self.id_pelicula, nombre, genero)
        self.peliculas.append(nueva_pelicula)
        self.id_pelicula+=1
        return True

    def pelicula_por_genero(self,genero):
        respuesta = {}
        for peli in self.peliculas:
            if peli.genero==genero:
                return json.dumps([movie.dump() for movie in self.peliculas if movie.genero==genero], indent=4)
        respuesta = {
            "Estado": "Error",
            "Mensaje": f"No Existe El Género: {genero}."
            }
        return jsonify(respuesta)
        
    
    def actualizar_pelicula(self, nombre, genero):
        for movie in self.peliculas:
            if movie.nombre == nombre:
                if genero is not None:
                    movie.genero = genero
                    return True
        return False
