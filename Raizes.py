import math

n = int(input())
numeros = input().split(" ")

for i in range(n):
    numero = float(numeros[i])
    print("{:.4f}".format(math.sqrt(numero)))