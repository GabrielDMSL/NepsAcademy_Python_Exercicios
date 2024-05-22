N = int(input())
Lista = input().split(" ")

for i in range(N):
    Lista[i]=int(Lista[i])

Lista.sort()

for i in range(N):
    print(Lista[i], end = " ")