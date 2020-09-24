items = [{"Name":"item1", "Value": "valor1"},{"Name":"item2", "Value": "valor2"}]
external = ""

for item in items:
    item = str(item)
    item = item.replace("{", "").replace("'","").replace("}"," ")
    external += item

print(external)
