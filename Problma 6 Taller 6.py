matriz = [[0] * 5 for _ in range(5)]
diagonal_principal = []

for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input("Ingrese un número: "))
        if i == j:
            diagonal_principal.append(matriz[i][j])

print("El vector resultante de la diagonal principal es:", diagonal_principal)
