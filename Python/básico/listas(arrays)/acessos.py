frutas = ['banana', 'maça', 'caju', 'morango', 'abacaxi']
print(frutas)
print(frutas[0]) # primeiro
print(frutas[-1]) # último

print(frutas[1:3]) # do segundo ao terceiro
# é importante reparar que o primeiro item é incluido e o último não é, ou seja, para acessar do 
# segundo (1) ao quarto (3), deve-se utilizar 1:4

print(frutas[:2]) # do primeiro ao segundo
# seguindo a mesma lógica, o terceiro elemento (2) não é incluido

print(frutas[1:]) # do segundo ao último
# como o segundo (1) é o elemento inicial da separação, ele é incluido

# TODOS OS EXEMPLOS DE ARRAY[X:Y] RETORNAM UM OUTRO ARRAY, OU SEJA, PODE SER INTERESSANTE DE USAR

if "banana" in frutas: # essa estrutura é muito interessante
    print("Tem banana")