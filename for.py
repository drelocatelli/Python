palavras = open("assets/palavras aleatorias.txt", "r")

for palavra in palavras:
    palavra = palavra.rstrip("\n")
    print(palavra + " | palavra")