import os
from docx2pdf import convert

print("$ pip3 install docx2pdf")
os.system("pip3 install docx2pdf")

os.chdir('docx')

for docx in os.listdir('.'):
    doc = docx.replace('.docx','')
    convert(docx, doc+".pdf")

# convert("input.docx")
# convert("input.docx", "output.pdf")
# convert("docx/")