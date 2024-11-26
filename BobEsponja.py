from CaricaturaModerna import CaricaturaModerna


class bob(CaricaturaModerna):
    def __init__(self):
        # Llamada al constructor de la clase base CaricaturaModerna
        super().__init__()

        # Inicialización de atributo propio de la clase bob
        self._lugar_creacion = ""

    # Métodos 'get' y 'set' para lugar_creacion
    def get_lugar_creacion(self):
        return self._lugar_creacion

    def set_lugar_creacion(self, lugar_creacion):
        self._lugar_creacion = lugar_creacion


    # Método que devuelve la descripción
    def descripcion(self):
        descripcion_padre = super().descripcion()
        return f"{descripcion_padre} Fue creada en {self.get_lugar_creacion()}."