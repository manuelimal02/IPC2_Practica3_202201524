class pelicula:
    def __init__(self, peliculaID, nombre, genero):
        self.peliculaID = peliculaID
        self.nombre = nombre
        self.genero = genero
    
    def dump(self):
        return {
            'movieID': self.peliculaID,
            'name': self.nombre,
            'genre': self.genero,
        }