import os

def sendMsg(token, groupId, msg):
    print('curl -d chat_id=-'+groupId+' -d text="'+msg+'"  https://api.telegram.org/'+token+'/sendMessage')
    os.system('curl -d chat_id=-'+groupId+' -d text="'+msg+'"  https://api.telegram.org/bot'+token+'/sendMessage')
    

token = input("[BOT TOKEN] $ ")
groupId = input("[GROUP ID NUMBER] $ ")
msg = input("[MSG] $ ")

sendMsg(token=token, groupId=groupId, msg=msg)