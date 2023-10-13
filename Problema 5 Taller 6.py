matriz = [[0] * 6 for _ in range(5)]
ceros = 0
positivos = 0
negativos = 0

for i in range(5):
    for j in range(6):
        matriz[i][j] = int(input("Ingrese un número: "))
        if matriz[i][j] == 0:
            ceros += 1
        elif matriz[i][j] > 0:
            positivos += 1
        else:
            negativos += 1

print("Cantidad de ceros:", ceros)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
