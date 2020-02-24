from fastkml import kml
from .utils import haversine


class GraphFromKmlDoc:

    def __init__(self, filename='pracas'):
        self._filename = filename

    def _get_document(self):
        doc = open("pracas.kml", "r").read().encode('utf-8')

        self._document = kml.KML()        

        self._document.from_string(doc)
        return self._document

    def get_pracas(self):
        self._pracas = dict()

        for locais in self._get_document().features():
            for idx, marcadores in enumerate(locais.features()):
                lng, lat, *args = marcadores.geometry._coordinates

                self._pracas[marcadores.name] = {
                    'id': idx,
                    'lat': lat,
                    'lng': lng,
                }

        return self._pracas

    def get_matriz_adjacencias(self):
        self._distancias=dict()

        pracas = self.get_pracas()

        for praca, coordenadas in pracas.items():
            self._distancias[praca] = {}
            for _praca, _coordenadas in pracas.items():
                self._distancias[praca][_praca] = haversine(
                    lat1=coordenadas['lat'],
                    lon1=coordenadas['lng'],
                    lat2=_coordenadas['lat'],
                    lon2=_coordenadas['lng'],
                )

        return self._distancias
