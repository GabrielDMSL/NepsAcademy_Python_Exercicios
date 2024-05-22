A = int(input())
B = input()
C= input()

acertos = 0

for i in range(A):
    if(B[i] == C[i]):
        acertos += 1

print(acertos)