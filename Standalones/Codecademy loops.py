estilos = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

precio = [30, 25, 40, 20, 20, 35, 50, 35]

ultimaSemana = [2, 3, 5, 8, 4, 4, 6, 2]

precioTotal = 0

for i in precio:
    precioTotal += i

precioPromedio = precioTotal / len(precio)
print('Precio de corte promedio: ${}'.format(precioPromedio))

preciosNuevos = [p-5 for p in precio]
print(preciosNuevos)

gananciaTotal = 0
for i in range(len(estilos)):
    gananciaTotal += precio[i] * ultimaSemana[i]
print('Ganancia total: ${}'.format(gananciaTotal))

gananciaPromedioDiaria = gananciaTotal/7
print(gananciaPromedioDiaria)

cortesBajo30 = [i for i in preciosNuevos if i < 30]
print(cortesBajo30)