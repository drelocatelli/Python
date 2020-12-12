#!/usr/bin/env python3
import os

# verificando se existe diretório
file = str('assets/creating_file/')
print(os.path.exists(file))

if bool(os.path.exists(file)) == False:
    # cria diretorio
    os.system('mkdir -p '+(file))
    # cria arquivo no diretorio
    f = open(file+'example.txt', 'x')
    f.write('Arquivo e texto adicionados!')
else:
    # adiciona texto
    f = open(file+'example.txt', 'w')
    f.write('Texto adicionado!')
