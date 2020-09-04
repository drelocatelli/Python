import os

opt = input("[COMANDO PRA TODOS DIRETÓRIOS] $ ")

for x in os.listdir('.'):
    if os.path.isdir(x):
        cmd = f"cd {x} && git pull"
        print("$ "+cmd)
        os.system(f"cd {x} && {opt}")