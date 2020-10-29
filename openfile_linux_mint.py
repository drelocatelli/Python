import os, sys, optparse

parse = optparse.OptionParser()
parse.add_option('--way', action='store', dest='location', type='string')
parse.add_option('--location', action='store', dest='location', type='string')
parse.add_option('--destination', action='store', dest='location', type='string')
options, remainder = parse.parse_args()

if options.location is not None:
    os.system(f"xdg-open {options.location}")
else:
    # print("\n"+(os.getcwd())+"\n")
    location = input("Caminho: ")
    os.system(f"xdg-open {location}")
