import sys

# type example: python append_list_within_dictionary.py  "{'nome': 'Andressa', 'cpf': 100}"

list_dict = [{'nome': 'Ana', 'cpf': '1000'}, {'nome': 'João', 'cpf': '7770'}]
app_item = sys.argv[1].replace("\"", "")
app_item = eval(app_item)

list_dict.append(app_item) 

print(list_dict)
