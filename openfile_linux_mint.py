import os

print(os.getcwd())
location = input("Caminho: ")

os.system(f"xdg-open {location}")
