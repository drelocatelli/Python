import os, sys, optparse

parse = optparse.OptionParser()
parse.add_option('--way', action='store', dest='way', type='string')

if '--way' in sys.argv:
    options, remainder = parse.parse_args()
    os.system(f"xdg-open {options.way}")
    sys.exit()

print(os.getcwd())
location = input("Caminho: ")

os.system(f"xdg-open {location}")
