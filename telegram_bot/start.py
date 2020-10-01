import os,subprocess

def sendMsg(token, groupId, msg):
    print('curl -d chat_id=-'+groupId+' -d text="'+msg+'"  https://api.telegram.org/'+token+'/sendMessage')
    os.system('curl -d chat_id=-'+groupId+' -d text="'+msg+'"  https://api.telegram.org/bot'+token+'/sendMessage')

token = ""
groupId = ""
msg = ""

config = open("config","r")
for line in config:
    line = line.rstrip('\n').replace("=","")
    if line.startswith("token"):
        token += line.replace("token","")
    if line.startswith("groupId"):
        groupId += line.replace("groupId","")
    if line.startswith("msg"):
        msg += line.replace("msg","")
        
sendMsg(token=token,groupId=groupId,msg=msg)