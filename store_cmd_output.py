import os, subprocess

cmd = "mkdir teste && rm -rfv teste"
output = str(subprocess.getoutput(cmd))

# salva o output do comando num texto
cmd = "echo "+output+" > output.txt"
os.system(cmd)
