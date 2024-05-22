N = int(input())
dicionario = {}

for _ in range(N):
    ingles, portugues = input().split()
    dicionario[ingles] = portugues

frase = input().split()
traducao = [dicionario[palavra] for palavra in frase]

print(' '.join(traducao))