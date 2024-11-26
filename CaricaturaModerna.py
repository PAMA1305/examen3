from Caricaturas import Caricatura


class CaricaturaModerna(Caricatura):
    def __init__(self):
        # Llamada al constructor de la clase base
        super().__init__()

        # Inicialización de nuevos atributos
        self._concepto = ""
        self._genero = ""

    # Métodos 'get' y 'set' para el concepto
    def get_concepto(self):
        return self._concepto

    def set_concepto(self, concepto):
        self._concepto = concepto

    # Métodos 'get' y 'set' para el género
    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero


    def descripcion(self):
        # Llamamos al método de la clase padre para obtener la descripción básica
        descripcion_padre = super().descripcion()
        # Añadimos las nuevas propiedades (concepto y género)
        return f"{descripcion_padre} Es una caricatura con el concepto de {self.get_concepto()}, El género es {self.get_genero()},"

