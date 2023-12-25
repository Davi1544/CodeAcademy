frutas = ['banana', 'maça', 'caju', 'morango', 'abacaxi']
frutas2 = ['manga', 'melão']
frutas3 = ('manga', 'melão') # tupla

# inserir sem trocar
frutas.insert(2, "melancia") # inserindo, na posição 2, 'melancia'

frutas.append("goma") # inserindo, no final da lista, 'goma'

frutas.extend(frutas2) # inserindo um novo array no final do primeiro
frutas.extend(frutas3) # inserindo uma tupla