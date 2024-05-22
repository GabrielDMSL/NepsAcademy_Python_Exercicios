N = int(input())

lista_tuplas = []

for _ in range(N):
    linha = input()
    string1, string2 = linha.split()

    lista_tuplas.append((string1, string2))

print(lista_tuplas)