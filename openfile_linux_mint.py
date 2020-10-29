import os, sys, optparse

parse = optparse.OptionParser()
parse.add_option('--way', action='store', dest='location', type='string')
parse.add_option('--location', action='store', dest='location', type='string')
parse.add_option('--destination', action='store', dest='location', type='string')
options, remainder = parse.parse_args()

if options.location is not None:
    os.system(f"xdg-open {options.location}")
else:
    print("\033[1;32m$ pwd\033[0m ", end='')
    print(os.getcwd())
    location = input("Caminho: ")
    os.system(f"xdg-open {location}")
