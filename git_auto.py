import os

print("COLOQUE git_auto.py UM NIVEL ANTES DO REPO GIT")
print("Você está em: " + os.getcwd())
file = input("[CAMINHO DO REPO GIT] $ ")
if file != "":
    os.chdir(file)
print("\nVocê está em: " + os.getcwd())
print("\n")

print("$ git status")
os.system("git status")

print("\n$ git add *")
os.system("git add *")

print("\n$ git status")
os.system("git status")

input("PROSSEGUIR? [ENTER] $ ")

print("\n$ git commit -m '...' ")
commit_msg = input("Enviar msg no commit? [y] $ ")
if commit_msg == "y":
    commit_msg = input("[MSG] $ ")
    print(f"$ git commit -m '{commit_msg}'")
    os.system(f"git commit -m '{commit_msg}'")
else:
    os.system("git commit -m '...'")
    