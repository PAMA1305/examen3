from AmigosImaginarios import AmigoImaginarios

class PersonajeFav(AmigoImaginarios):
    def __init__(self):
        # Llamada al constructor de la clase base AmigoImaginarios
        super().__init__()
        # Inicializamos el atributo adicional 'color_personaje'
        self._color_personaje_favorito = ""

    # Método 'get' y 'set' para color_personaje
    def get_color_personaje_favorito(self):
        return self._color_personaje_favorito

    def set_color_personaje_favorito(self, color):
        self._color_personaje_favorito = color

    def descripcion(self):
        # Llamamos al método descripcion() de la clase base AmigoImaginarios
        descripcion_padre = super().descripcion()
        # Añadimos la información sobre el color del personaje
        return f"{descripcion_padre} El personaje que tiene el color favorito en todo el mundo es {self._color_personaje_favorito}."
