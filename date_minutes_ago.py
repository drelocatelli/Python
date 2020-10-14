import os

minutes = str(input("Informe quantos minutos antes: "))
os.system("clear -x")
cmd = f'date -d "now {minutes} minutes ago" --iso-8601=seconds'
print("\033[1;32mComando: $\033[0m "+str(cmd))
os.system(cmd)