n = int(input())
tabuleiro = []

tabuleiro.append(0)

for i in range(1, n+1):
    tabuleiro.append(int(input()))

tabuleiro.append(0)

for i in range(1, n+1):
    quantidade = tabuleiro[i-1] + tabuleiro[i] + tabuleiro[i+1]
    print(quantidade)
