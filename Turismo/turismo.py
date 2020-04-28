destinos = ["Paris, Francia", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egipto"]

def obtenerIndiceDestino(destino):
    try:
        indiceDestino = destinos.index(destino)
    except ValueError:
        print("Ese destino no existe")
        indiceDestino = None   
    return indiceDestino

def locacionViajero(viajero):
    destinoViaje = test_traveler[1]
    indiceDestinoViajero = obtenerIndiceDestino(destinoViaje)
    return indiceDestinoViajero

def añadirAtraccion(destino, atraccion):
    indiceDestino = obtenerIndiceDestino(destino)
    if indiceDestino == None:
        return
    atracciones[indiceDestino].append(atraccion)
    return

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

atracciones = [[] for i in destinos]

añadirAtraccion("Los Angeles, USA", ['Venice Beach', ['beach']])
añadirAtraccion("Paris, Francia", ["the Louvre", ["art", "museum"]])
añadirAtraccion("Paris, Francia", ["Arc de Triomphe", ["historical site", "monument"]])
añadirAtraccion("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
añadirAtraccion("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
añadirAtraccion("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
añadirAtraccion("Los Angeles, USA", ["LACMA", ["art", "museum"]])
añadirAtraccion("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
añadirAtraccion("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
añadirAtraccion("Cairo, Egipto", ["Pyramids of Giza", ["monument", "historical site"]])
añadirAtraccion("Cairo, Egipto", ["Egyptian Museum", ["museum"]])
