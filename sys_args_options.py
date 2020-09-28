import sys, optparse

parser = optparse.OptionParser()
parser.add_option('--title', action="store", dest="title", type="int")
options, remainder = parser.parse_args()

print(options)
print(f"title: {options.title}")
