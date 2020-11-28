import sys, optparse

parser = optparse.OptionParser()
parser.add_option('--opcao1', action="store", dest="opcao1", type="string")
parser.add_option('--opcao2', action="store", dest="opcao2", type="string")
options, args = parser.parse_args()

# printa todos os argumentos
print(options)
# printa opção
print(options.opcao1)


print('------------------------------------')

# printa quantidade de argumentos
argumentos = []

for i in sys.argv[1:]:
    if not i.startswith('--'):
        argumentos.append(i)

print(argumentos)
print(len(argumentos))
