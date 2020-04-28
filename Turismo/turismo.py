destinos = ["Paris, Francia", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egipto"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def obtenerIndiceDestino(destino):
    indiceDestino = destinos.index(destino)    
    return indiceDestino

def locacionViajero(viajero):
    destinoViaje = test_traveler[1]
    indiceDestinoViajero = obtenerIndiceDestino(destinoViaje)
    return indiceDestinoViajero

test_indiceDestino = locacionViajero(test_traveler)
print(test_indiceDestino)