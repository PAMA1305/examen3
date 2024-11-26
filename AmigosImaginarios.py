
from CaricaturaModerna import CaricaturaModerna
from ElMejorP import CaricaturaBase  # Asegúrate de que la ruta del archivo sea correcta


class AmigoImaginarios(CaricaturaModerna, CaricaturaBase):
    def __init__(self):
        CaricaturaModerna().__init__()
        CaricaturaBase().__init__()

        self._pais_mas_visto = ""

    # Método GET para obtener el país más visto
    def get_pais_mas_visto(self):
        return self._pais_mas_visto

    # Método SET para establecer un nuevo país como el más visto
    def set_pais_mas_visto(self, pais):
        self._pais_mas_visto = pais

    def descripcion(self):

        descripcion_modern = super().descripcion()

        descripcion_base = CaricaturaBase.descripcion(self)  # Si 'CaricaturaBase' tiene un método 'descripcion'

        # Combine ambas descripciones y añade información adicional
        return f"{descripcion_modern} {descripcion_base} Fue más vista en el pais {self._pais_mas_visto},"
