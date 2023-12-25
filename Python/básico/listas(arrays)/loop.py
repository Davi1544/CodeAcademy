frutas = ['banana', 'maça', 'caju', 'morango', 'abacaxi']

# loop por todos os elementos
for x in frutas: # for fruta in frutas
    # x = frutas[x]
    print(x)

for i in range(len(frutas)): # for(i = 0; i < len(frutas); i++)
    print(i) # 0 - 4

i = 0
while i < len(frutas): # mesma ideia
    print(i)
    i += 1

# LIST COMPREHENSION
[print(x) for x in frutas] # loop por todos os elementos (versão resumida)
[print(x) for x in frutas if x == "banana"] # loop por todos os elementos (versão resumida) com if