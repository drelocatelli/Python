adc = input("[PALAVRA ADICIONADA] $ ")
adc = adc.capitalize()
adc = adc + "\n"
with open('assets/add_item_to_text.txt', 'a') as palavras:
    palavras.write(adc)
with open('assets/add_item_to_text.txt', 'r') as palavras:
    for palavra in palavras:
        palavra = palavra.strip()
        print(palavra)