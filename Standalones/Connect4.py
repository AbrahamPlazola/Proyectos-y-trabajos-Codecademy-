import os
#Lista de listas, simulando cada lista como un renglón del tablero
#Trabajar verticales con el mismo indice en diferentes listas
#Trabajar horizontales dentro de la misma lista
#Trabajar diagonales con un indice +- 1 en diferentes listas
#Lista1[0] lista2[1] lista3[2]...
#Jugador 1 = O
#Jugador 2 = X
tablero =  [
            [" ", " ", " ", " ", " "], #lista0[0-4]
            [" ", " ", " ", " ", " "], #lista1[0-4]
            [" ", " ", " ", " ", " "], #lista2[0-4]
            [" ", " ", " ", " ", " "], #lista3[0-4]
            [" ", " ", " ", " ", " "]  #lista4[0-4]
           ]

#Coloca la ficha en la lista correspondiente
#Regresa Falso si el movimiento no fue valido
def colocarFicha(jugador, pila):
    #Itera por el tablero en reversa
    for i in range(len(tablero) - 1, -1, -1):
        if tablero[i][pila] is " ":
            tablero[i][pila] = jugador
            return True

    print("Movimiento invalido, esta columna ya está llena")
    return False

def imprimirTablero():
    print("  1   2   3   4   5")
    for i in tablero:
        print("| ", end="")
        for j in i:
            print(j + " | ", end="")
        print("\n|---|---|---|---|---|")

def checarVictoria(jugador):
    #Horizontales
    for i in tablero:
        if i[2] is not " ":
            if i[1] is i[2] is i[3]:
                if i[0] is i[1] or i[4] is i[1]:
                    return jugador
    #Verticales
    for i in range(len(tablero)):
        if tablero[2][i] is not " ":
            if tablero[1][i] is tablero[2][i] is tablero[3][i]:
                if tablero[0][i] is tablero[1][i] or tablero[4][i] is tablero[1][i]:
                    return jugador
    #Diagonales hacia arriba
    if tablero[3][0] is not " ":
        if tablero[3][0] is tablero[2][1] is tablero[1][2] is tablero[0][3]:
            return jugador

    if tablero[2][2] is not " ":
        if tablero[3][1] is tablero[2][2] is tablero[1][3]:
            if tablero[4][0] is tablero[2][2] or tablero [0][4] is tablero[2][2]:
                return jugador

    if tablero[4][1] is not " ":
        if tablero[4][1] is tablero[3][2] is tablero[2][3] is tablero[1][4]:
            return jugador
        
    #Diagonales hacia abajo
    if tablero[1][0] is not " ":
        if tablero[1][0] is tablero[2][1] is tablero[3][2] is tablero[4][3]:
            return jugador
    
    if tablero[2][2] is not " ":
        if tablero[1][1] is tablero[2][2] is tablero[3][3]:
            if tablero[0][0] is tablero[1][1] or tablero[4][4] is tablero[1][1]:
                return jugador
    
    if tablero[0][1] is not " ":
        if tablero[0][1] is tablero[1][2] is tablero[2][3] is tablero[3][4]:
            return jugador

    return " "

jugador = "X"
ganador = " "
turno = 0
empate = False
while ganador is " ":
    if jugador is "O":
        jugador = "X"
    else:
        jugador = "O"
    turno += 1
    #Variables para iniciar validación
    columna = -1
    valido = False

    print("Turno de '{0}'".format(jugador))
    imprimirTablero()
    while valido is False:
        columna = int(input("En que columna desea colocar su ficha? "))
        columna -= 1
        if columna < 0 or columna > 4:
            print("Columna invalida, seleccione de nuevo")
            valido = False
        else:
            valido = True
        
        if valido is True:
            valido = colocarFicha(jugador, columna)

    if turno > 6:
        ganador = checarVictoria(jugador)
    if turno == 25:
        empate = True
        break

imprimirTablero()
if empate is True:
    print("Empate")
else:
    print("Ganó " + ganador + " en {0} turnos".format(turno))

os.system("pause")