matriz = [[0] * 10 for _ in range(10)]
mayor = float('-inf')
fila_mayor = 0
columna_mayor = 0

for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input("Ingrese un número: "))
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            fila_mayor = i
            columna_mayor = j

print("La posición del número mayor es:", [fila_mayor, columna_mayor])
