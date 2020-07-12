from os import system
import random

refresh = 0
opc = 0
mano = []
deckActual = []
descartados = []

def switchCase(opc):
    func = switch.get(opc, "F")
    try:
        return func()
    except:
        print("Input no reconocido mi joven\n")

def robar():
    global mano
    system("cls")
    if len(mano) == refresh:
        print("No puedes tener mas cartas en tu mano") 
        input("Presione enter para continuar...")
        return
    
    cantidad = refresh + 1
    while (len(mano) + cantidad) > refresh:
        system("cls")
        print("Puedes robar hasta " + str(refresh - len(mano)) + " cartas")
        cantidad = int(input("Cuantas cartas desea robar: "))

        if len(mano) + cantidad > refresh:
            print("No puedes robar esa cantidad de cartas")
            input("Presione enter para continuar...")

        else:
            for i in range(cantidad):
                mano.append(deckActual.pop())
            return

def verDeck():
    system("cls")
    print("Tu deck es:")
    for carta in deckActual:
        print(carta)
    barajear()

def barajear():
    system("cls")
    print("Barajeando deck...")
    random.shuffle(deckActual)
    input("Presione enter para continuar...")

def usar():
    print("Tu mano es:")
    i = 0
    for card in mano:
        print("[{}] ".format(i) + card)
        i += 1
        
    opc = int(input("Que carta desea usar? "))
    print("Descartando {} de la mano".format(mano[opc]))
    descartados.append(mano.pop(opc))

def verDescartados():
    print("Pila de descartados: ")
    for card in descartados:
        print(card)
    input("Presione enter para continuar...")

def reiniciar():
    pass

with open("deck.txt", "r") as deck:
    readDeck = deck.read().splitlines()

for carta in readDeck:
    copias = int(carta[-1])
    for i in range(copias):
        deckActual.append(carta[:-3])

switch = {
    1: robar,
    2: verDeck,
    3: barajear,
    4: usar,
    5: verDescartados,
    6: reiniciar
}

barajear()
refresh = int(input("Ingrese el valor de refresh del persona: "))
robar()

while True:
    system("cls")
    print("Tu mano es:")
    i = 0
    for card in mano:
        print("[{}] ".format(i) + card)
        i += 1

    opc = int(input("1.- Robar\n2.- Ver deck\n3.- Barajear deck\n4.- Usar carta\n5.- Ver descartadas\n6.- Reiniciar\n7.- Salir\n"))
    system("cls")
    if opc == 7:
        break
    switchCase(opc)

print("bye bye")