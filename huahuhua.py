A = input()

new_frase = ""

vogais = ['a', 'e', 'i', 'o', 'u']

for i in A:
    if i in vogais:
        new_frase += i

if new_frase == new_frase[::-1]:
    print('S')
else:
    print('N')