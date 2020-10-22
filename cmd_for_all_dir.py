import os

input("\033[38;2;255;255;255m\033[1;41mPOSICIONE ESTE SCRIPT UM NÍVEL DE DIRETÓRIO ANTERIOR [ENTER] $ \033[0m")

opt = False
while(opt == "" or bool(opt) == False):
    opt = input("\033[1;32m[COMANDO PRA TODOS DIRETÓRIOS] $ \033[0m")
    continue

for x in os.listdir('.'):
    if os.path.isdir(x):
        cmd = f"cd {x} && {opt}"
        print("\033[1;32m\n$ "+cmd+"\033[0m")
        os.system(f"cd {x} && {opt}")
