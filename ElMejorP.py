class CaricaturaBase:
    def __init__(self):
        self._personaje_mas_querido = ""

    # Método GET para obtener el personaje más querido
    def get_personaje_mas_querido(self):
        return self._personaje_mas_querido

    # Método SET para establecer un nuevo personaje como el más querido
    def set_personaje_mas_querido(self, personaje):
        self._personaje_mas_querido = personaje

    def descripcion(self):
        return f"El personaje más querido por la audiencia es {self._personaje_mas_querido},"
