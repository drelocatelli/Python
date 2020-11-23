import math

produtos = ['Celular', 'Computador', 'Notebook', 'Bicicleta', 'Cofre', 'Volvo', 'BMW', 'Ford', 'Mazda']
itens_por_pagina = 3
num_paginas = math.ceil(len(produtos)/itens_por_pagina)
total_itens = str(len(produtos))

paginacao = ''

# mensagem
print(total_itens + ' itens foram cadastrados | exibindo ' + str(itens_por_pagina) + ' itens por página.\n')


# itens
for i in range(itens_por_pagina):
    print(produtos[i])
    
# paginacao
for item in range(1,num_paginas+1):
    paginacao += str(item) + ' '

print()
print(paginacao)
