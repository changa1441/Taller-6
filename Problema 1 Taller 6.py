matriz = [[0] * 6 for _ in range(5)]
suma = 0

for i in range(5):
    for j in range(6):
        matriz[i][j] = int(input("Ingrese un número: "))
        suma += matriz[i][j]

print("La suma de los números almacenados en la matriz es:", suma)
