import os

def sendMsg(bot_token, groupId, msg):
    print('curl -d chat_id=-'+groupId+' -d text="'+msg+'"  https://api.telegram.org/'+bot_token+'/sendMessage')
    os.system('curl -d chat_id=-'+groupId+' -d text="'+msg+'"  https://api.telegram.org/bot'+bot_token+'/sendMessage')

sendMsg(
    bot_token = "", 
    groupId = "",
    msg = ""
)