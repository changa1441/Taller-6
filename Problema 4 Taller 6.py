matriz = [[0] * 20 for _ in range(20)]
suma_columnas = [0] * 20
max_suma = float('-inf')
columna_max_suma = 0

for i in range(20):
    for j in range(20):
        matriz[i][j] = int(input("Ingrese un número: "))
        suma_columnas[j] += matriz[i][j]

for j in range(20):
    if suma_columnas[j] > max_suma:
        max_suma = suma_columnas[j]
        columna_max_suma = j

print("La columna con la máxima suma es:", columna_max_suma)
print("La suma de esa columna es:", max_suma)
