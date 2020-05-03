alfabeto = "abcdefghijklmnopqrstuvwxyz"

def vigenere(oracion, clave):
    newClave = ""
    indexClave = 0
    for i in oracion:
        if i in alfabeto:
            newClave += clave[indexClave]
            indexClave += 1
            if indexClave >= len(clave):
                indexClave -= len(clave)
        else:
            newClave += i

    indexOracionEnAlfabeto = 0
    indexClave = 0
    indexClaveEnAlfabeto = 0
    indexCodificado = 0
    decodificado = ""
    for i in oracion:
        if i in alfabeto:
            indexOracionEnAlfabeto = alfabeto.find(i)
            indexClaveEnAlfabeto = alfabeto.find(newClave[indexClave])
            indexCodificado = indexOracionEnAlfabeto - indexClaveEnAlfabeto
            decodificado += alfabeto[indexCodificado]
#             print(newClave[indexClave] + " " +str(indexOracionEnAlfabeto) + " " + str(indexClaveEnAlfabeto) + " " + str(indexCodificado) + " " + alfabeto[indexCodificado])
        else:
            decodificado += i
        indexClave += 1
            
    return decodificado

def vigenereEncode(oracion, clave):
    newClave = ""
    indexClave = 0
    for i in oracion:
        if i in alfabeto:
            newClave += clave[indexClave]
            indexClave += 1
            if indexClave >= len(clave):
                indexClave -= len(clave)
        else:
            newClave += i
    print(newClave)
            
    indexOracionEnAlfabeto = 0
    indexClave = 0
    indexClaveEnAlfabeto = 0
    indexCodificado = 0
    decodificado = ""
    for i in oracion:
        if i in alfabeto:
            indexOracionEnAlfabeto = alfabeto.find(i)
            indexClaveEnAlfabeto = alfabeto.find(newClave[indexClave])
            indexCodificado = indexOracionEnAlfabeto + indexClaveEnAlfabeto
            if indexCodificado >= len(alfabeto):
                indexCodificado -= len(alfabeto)
            decodificado += alfabeto[indexCodificado]
    #             print(newClave[indexClave] + " " +str(indexOracionEnAlfabeto) + " " + str(indexClaveEnAlfabeto) + " " + str(indexCodificado) + " " + alfabeto[indexCodificado])
        else:
            decodificado += i
            
        indexClave += 1

    return decodificado

print(vigenereEncode("oye rogelio quieres ", "owo"))
print(vigenere("lm eyd isfwpzs ewwlpdm rc zw piowf c raidtds dn hmzk, hm wzie tc elgv ui yw nhdm", "owo"))