import re

lista_pesquisa = ['problemas', 'negócios'];

texto = 'Alguns dos problemas enfrentados incluem conhecimento inadequado sobre as tecnologias envolvidas, privacidade dos dados e capacidades analíticas inadequadas das organizações. Muitas empresas também enfrentam a falta de habilidades para lidar com tecnologias de Big Data.'

print('Buscando por informações: ')
i = -1
for item in lista_pesquisa:
    i += 1
    print(lista_pesquisa[i], end=', ') if i == 0 else print(lista_pesquisa[i])

print('\n')

for item in lista_pesquisa:
    print('"%s"' % (item))

    if re.search(item, texto):
        print('Palavra encontrada.')
        print('\n')
    else:
        print('Palavra não encontrada.')
        print('\n')
