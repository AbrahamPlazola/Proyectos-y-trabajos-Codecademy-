#Una sola lista
#Trabajar las verticales con delta de 5
#Trabajar horizontales con deltas de 1
#Trabajar diagonales con delta de 6
tablero0 = [
            "", "", "", "", "", #0-4
            "", "", "", "", "", #5-9
            "", "", "", "", "", #10-14
            "", "", "", "", "", #15-19
            "", "", "", "", ""  #20-24
          ]

#Lista de listas, simulando cada lista como un renglón del tablero
#Trabajar verticales con el mismo indice en diferentes listas
#Trabajar horizontales dentro de la misma lista
#Trabajar diagonales con un indice +- 1 en diferentes listas
#Lista1[0] lista2[1] lista3[2]...
tablero1 = [
            ["", "", "", "", ""], #Lista0[0-4]
            ["", "", "", "", ""], #Lista1[0-4]
            ["", "", "", "", ""], #Lista2[0-4]
            ["", "", "", "", ""], #Lista3[0-4]
            ["", "", "", "", ""], #Lista4[0-4]
           ]

#Lista de listas, simulando cada lista como una pila del tablero
#Igual que tablero 2, con la funcionalidad de verticales en horizontales y viceversa
tablero2 = [
            ["", "", "", "", ""], #Lista0[0-4]
            ["", "", "", "", ""], #Lista1[0-4]
            ["", "", "", "", ""], #Lista2[0-4]
            ["", "", "", "", ""], #Lista3[0-4]
            ["", "", "", "", ""], #Lista4[0-4]
           ]