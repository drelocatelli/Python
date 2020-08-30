import os

# verificando se existe diretório
print(os.path.exists("assets/creating_file/"))

if os.path.exists("assets/creating_file/") == False:
    # cria diretorio
    os.mkdir("assets/creating_file")
    # cria arquivo no diretorio
    f = open("assets/creating_file/example.txt", "x")
    f.write("Arquivo e texto adicionados!")
else:
    # adiciona texto
    f = open("assets/creating_file/example.txt", "w")
    f.write("Texto adicionado!")
