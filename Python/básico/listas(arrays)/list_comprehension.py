fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x: # se um element da lista contém a letra "a", ele é selecionado
    newlist.append(x)
    
newlist = [x for x in fruits if "a" in x] # versao resumida

# [expression for item in iterable if condition == True]