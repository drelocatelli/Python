import sys, optparse

parser = optparse.OptionParser()
parser.add_option('--title', action="store", dest="title", type="string")
parser.add_option('--teste', action="store", dest="teste", type="string")
options, args = parser.parse_args()

# printa todos os argumentos
print(options)
# printa opção
print(options.title)


print('------------------------------------')

# printa quantidade de argumentos
argumentos = []

for i in sys.argv[1:]:
    if not i.startswith('--'):
        argumentos.append(i)

print(argumentos)
print(len(argumentos))
