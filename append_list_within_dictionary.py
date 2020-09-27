list_dict = [{'nome': 'Ana', 'cpf': '1000'}, {'nome': 'João', 'cpf': '7770'}]

app_nome, app_cpf = 'Maria', '2020'

list_dict.append({'nome': app_nome, 'cpf': app_cpf})

print(str(list_dict) + "\n")

for dict in list_dict:
    print(dict)