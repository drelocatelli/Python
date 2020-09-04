import os

input("POSICIONE ESTE SCRIPT UM NÍVEL DE DIRETÓRIO ANTERIOR [ENTER] $ ")

opt = False
while(opt == "" or bool(opt) == False):
    opt = input("[COMANDO PRA TODOS DIRETÓRIOS] $ ")
    continue

for x in os.listdir('.'):
    if os.path.isdir(x):
        cmd = f"cd {x} && {opt}"
        print("------------------------------------------------")
        print("$ "+cmd)
        print("------------------------------------------------")
        os.system(f"cd {x} && {opt}")
        
