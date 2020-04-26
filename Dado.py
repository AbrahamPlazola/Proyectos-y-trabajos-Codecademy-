import random
win = 0
loss = 0

def dado(lados, pred):
    res = random.randint(1, lados)
    if lados == 2:
        if res == 1:
            res = 'A'
        elif res == 2:
            res = 'S'
    print('El resultado fue {}'.format(res))
    if res == pred:
        return True
    else:
        return False


while 1:
    lados = input('Ingrese el número de lados de su dado, si quiere lanzar una moneda ingrese 2 y si quiere salir ingrese "Y" \n Número de lados = ')    
    if lados == 'Y':
        break

    if lados == 2:
        prediccion = input('Hola, ingrese su predicción de la moneda "A" o "S". \nPredicción = ')
    else:
        prediccion = input('Hola, ingrese su predicción del dado.\nPredicción = ')
    
    if dado(lados, prediccion) == True:
        win += 1
        print("¡Su predicción fue correcta!")
    else:
        loss += 1
        print("Su predicción fue incorrecta...")

    print('Historial actual: \n Ganadas: {} \n Perdidas: {} \n'.format(win, loss))

print('\n Finalizando programa...')