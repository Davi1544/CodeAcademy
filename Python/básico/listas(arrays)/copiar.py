lista1 = [1,2,3,5,6,4,6,9,7,2,1]
lista2 = lista1 #isso não funciona, pois a lista2 passar a imitar tudo o que ocorrer com a lista1
# a lista2 funciona em referência à lista1

lista2 = lista1.copy() # isso funciona, pois a lista2 só será uma cópia da 1, sem usá-la como referência
lista2 = list(lista1) # funciona da mesma forma