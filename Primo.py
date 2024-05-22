x = int(input())

def eh_primo(x):
	divisores = 0
	
    for i in range(1, x+1):
        if (x % i == 0):
            divisores += 1
			
    if (divisores == 2):
        return True
    else:
        return False
			

if eh_primo(x):
	print('S')
else:
	print('N')