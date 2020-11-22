import re

lista_pesquisa = [];
texto = str(input('Digite seu texto: '))

def count_busca():
    print('Nenhuma palavra foi adicionada') if len(lista_pesquisa) == 0 else print(str(len(lista_pesquisa))+' palavras foram adicionadas')

def busca():
    print('Buscando por informações: ')
    i = -1
    for item in lista_pesquisa:
        i += 1
        print(lista_pesquisa[i], end=', ') if i == 0 else print(lista_pesquisa[i])

    print('\n')

    for item in lista_pesquisa:
        print('"%s"' % (item))
        print('Palavra encontrada.\n') if re.search(item, texto) else print('Palavra não encontrada\n')


while True:
    print("1 - Adicionar palavra\n2 - Verificar palavras\n3 - Pesquisar")
    opt = int(input("Digite um número: "))

    if opt == 1:
        print('\n')
        add_palavra = input("Atribua uma palavra para pesquisar: ")
        lista_pesquisa.append(add_palavra)
        print('\n')

        continue
    elif opt == 2:
        print('\n')
        count_busca()
        i = -1; msg = ""
        for item in lista_pesquisa:
            i += 1
            if i == len(lista_pesquisa) -1:
                msg = lista_pesquisa[i]
            else:
                msg = (lista_pesquisa[i])+', '

            print(msg, end='')
            
        print('\n')
        continue
    elif opt == 3:
        busca()


