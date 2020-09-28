import sys

print("\033[38;2;255;255;255m\033[1;41mNão se esqueça de passar os parâmetros\033[0m\n\n")
# python append_list_within_dictionary.py  "{'nome': 'Ana', 'cpf': '1000'}, {'nome': 'João', 'cpf': '7770'}, {'nome': 'Andressa', 'cpf': 100},{'nome': 'Dory', 'cpf': 100}"

list_dict = []
app_item = sys.argv[1]

list_dict.append(app_item)
list_dict = str(list_dict)
list_dict = list_dict.replace("\"","")

# eval sempre por ultimo!!!!!!!!!!!!!!!!
list_dict = eval(list_dict)

print(list_dict)

