import os
from pathlib import Path

# verificando se existe diretório
print(Path("assets/creating_file/").exists())

if Path("assets/creating_file/").exists() == False:
    # cria diretorio
    os.mkdir("assets/creating_file")
    # cria arquivo no diretorio
    f = open("assets/creating_file/example.txt", "x")
    f.write("Arquivo e texto adicionados!")
else:
    # adiciona texto
    f = open("assets/creating_file/example.txt", "w")
    f.write("Texto adicionado!")
