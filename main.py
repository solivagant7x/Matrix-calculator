print("Bienvenue sur la première version de ma calculatrice matricielle !")

print("Saisissez les dimensions de la première matrice")
row1 = int(input("ligne(s) : "))
col1 = int(input("colonne(s) : "))

matrix = [[0 for _ in range(col1)] for _ in range(row1)]

for i in range(row1) :
    for j in range(col1) :
        case = int(input("Valeur : "))
        matrix[i][j] = case

print("---------------------")
print("Matrice 1 : ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
print("---------------------")

print("Saisissez les dimensions de la deuxième matrice :")
row2 = int(input("ligne(s) : "))
col2 = int(input("colonne(s) : "))

matrix2 = [[0 for _ in range(col2)] for _ in range(row2)]

for i in range(row2) :
    for j in range(col2) :
        case = int(input("Valeur : "))
        matrix2[i][j] = case

print("---------------------")
print("Matrice 2 :")
for i in range(len(matrix2)) :
    for j in range(len(matrix2[i])) :
        print(matrix2[i][j], end=' ')
    print()
print("---------------------")

total = [[0 for _ in range(col2)] for _ in range(row1)]

operation = input("Opérateur : ").strip()
if operation == "+" :
    if row1 != row2 or col1 != col2 :
        print("Vous ne pouvez additionner 2 matrices de dimensions différentes")
    else :
        for i in range(row1):
            for j in range(col1):
                total[i][j] = matrix[i][j] + matrix2[i][j]
elif operation == "-" :
    if row1 != row2 or col1 != col2 :
        print("Vous ne pouvez soustraire 2 matrices de tailles différentes")
    else :
        for i in range(row1):
            for j in range(col1):
                total[i][j] = matrix[i][j] - matrix2[i][j]
elif operation == "*" :
    if col1 != row2 :
        print("Vous ne pouvez multiplier 2 matrices incompatibles")
    else :
        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    total[i][j] += (matrix[i][k] * matrix2[k][j])

print("---------------------")
print("Résultat de la matrice :")
for i in range(len(total)) :
    for j in range(len(total[i])) :
        print(total[i][j], end=' ')
    print()
print("---------------------")