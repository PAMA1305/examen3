class Caricatura:
    def __init__(self):
        self._nombre = ""
        self._ano_estreno = 0

    # Métodos 'get' y 'set' para el nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    # Métodos 'get' y 'set' para el año de estreno
    def get_ano_estreno(self):
        return self._ano_estreno

    def set_ano_estreno(self, ano_estreno):
        self._ano_estreno = ano_estreno


    def descripcion(self):
        return f"Nombre: {self._nombre}, Año de estreno: {self._ano_estreno}, "