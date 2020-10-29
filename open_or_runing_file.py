import os, sys, subprocess
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
arquivo = input("[CAMINHO DO ARQUIVO] $ ")
open_file(arquivo)
