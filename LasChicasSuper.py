from CaricaturaModerna import CaricaturaModerna

class ChicasSuper(CaricaturaModerna):
    def __init__(self):
        # Llamada al constructor de la clase base CaricaturaModerna
        super().__init__()

        # Inicialización de atributo propio de la clase ChicasSuper
        self._creador = ""

    # Métodos 'get' y 'set' para creador
    def get_creador(self):
        return self._creador

    def set_creador(self, creador):
        self._creador = creador



    # Método que devuelve la descripción
    def descripcion(self):
        descripcion_padre = super().descripcion()
        return f"{descripcion_padre} Fue creada por {self.get_creador()}."