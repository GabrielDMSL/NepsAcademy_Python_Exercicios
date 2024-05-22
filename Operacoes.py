N = input()
A, B = input().split(" ")
A = float (A)
B = float (B)

if (N == "M"):
    mult = A*B
    print('{:.2f}'.format(mult))
if (N == "D"):
    div = A/B
    print('{:.2f}'.format(div))