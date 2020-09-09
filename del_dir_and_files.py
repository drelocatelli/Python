import os

# rm -rf force recursivy
def rm(item):
    item = f"rm -rfv {item}"
    os.system(item)
    
item = input("[CAMINHO A SER REMOVIDO] $ ")
rm(item)