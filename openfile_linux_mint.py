import os, sys, optparse

parse = optparse.OptionParser()
parse.add_option('--way', action='store', dest='location', type='string')
parse.add_option('--location', action='store', dest='location', type='string')
parse.add_option('--destination', action='store', dest='location', type='string')

if bool(parse.parse_args()):
    options, remainder = parse.parse_args()
    os.system(f"xdg-open {options.location}")
    sys.exit()

print("\n"+os.getcwd()+"\n")
location = input("Caminho: ")

os.system(f"xdg-open {location}")
