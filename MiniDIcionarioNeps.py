N = int(input())

# Inicialize um dicionário vazio
dictionary = {}

# Para cada tradução, leia a palavra em inglês e sua tradução em português
# e adicione-as ao dicionário
for _ in range(N):
    english, portuguese = input().split()
    dictionary[english] = portuguese

# Leia a frase em inglês da entrada e divida-a em palavras
sentence = input().split()

# Traduza cada palavra na frase procurando sua tradução em português no dicionário
translation = [dictionary[word] for word in sentence]

# Junte as palavras traduzidas em uma frase e imprima-a
print(' '.join(translation))