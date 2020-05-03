letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
"R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letraAPunto = {key: value for key, value in zip(letters, points)}
letraAPunto[" "] = 0

def puntuar(palabra):
    puntuacion = 0
    palabra = palabra.upper()
    for i in palabra:
        puntuacion += letraAPunto.get(i, 0)
    return puntuacion

def jugarPalabra(jugador, palabra):
    jugadorPalabra[jugador].append(palabra)    

jugadorPalabra = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
"Lexi Con": ["ERASER", "COMA", "PERIOD"]}
jugadorPuntos = {}

def actualizarpuntuacion():
    for key, value in jugadorPalabra.items():
        puntuacion = 0
        for i in value:
            puntuacion += puntuar(i)
        jugadorPuntos[key] = puntuacion

