N = int(input())
arr = input().split()
P = int(arr[0])
C = (arr[1])
Q = int(arr[2])

if C == "+":
    if (P+Q<= N):
        print('OK')
    else:
        print('OVERFLOW')

if C == '*':
    if (P*Q<=N):
        print('OK')
    else:
        print('OVERFLOW')