matriz = [[0] * 7 for _ in range(7)]
suma_renglones = [0] * 7
suma_columnas = [0] * 7

for i in range(7):
    for j in range(7):
        matriz[i][j] = int(input("Ingrese un número: "))
        suma_renglones[i] += matriz[i][j]
        suma_columnas[j] += matriz[i][j]

print("La suma de cada renglón es:", suma_renglones)
print("La suma de cada columna es:", suma_columnas)
