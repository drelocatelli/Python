names = ["Andressa", "Marcus", "Adriano", "Maria", "Fulano", "Ciclano"]
values = 0

    
while True:
    add_item = input("ADICIONAR ITEM? [y] $ ")

    if add_item == "y":
        add_item = input("[Nome do item] $ ")
        if add_item == "":
            add_item = input("[Nome do item] $ ")
            continue
        names.append(add_item)   
        print("\n")
        for name in names:
            values += 1
            print(f"{values} | {name}")
        print("\n")
        continue