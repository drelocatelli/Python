import easygui as gui

title = "GMAIL SENDER"
msg = "Envie gmails rapidamente!"

fieldNames = ["DE:","SENHA:","PARA:","ASSUNTO:","MENSAGEM:"]
fieldValues = []
fieldValues = gui.multenterbox(msg, title, fieldNames)

while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" não pode ser um campo vazio.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = gui.multenterbox(errmsg, title, fieldNames, fieldValues)

FROM = fieldValues[0]
PASS = fieldValues[1]
TO = fieldValues[2]
SUBJECT = fieldValues[3]
MSG = fieldValues[4]

import os
os.system('pip3 install yagmail')

import yagmail

def send_gmail(remetente, destinatario, senha, assunto, mensagem):

    email = {}
    email['from'] = remetente
    email['to'] = destinatario
    email['pass'] = senha
    email['assunto'] = assunto
    email['msg'] = mensagem
    smtp = "smtp.gmail.com"
    
    yag = yagmail.SMTP(email['from'], email['pass'])
    yag.send(to = email['to'], subject = email['assunto'], contents = email['msg'])

    status = f"E-mail enviado com sucesso!\n\nDE: {FROM}\nPARA: {TO}\nASSUNTO: {SUBJECT}\nMENSAGEM: {MSG}"
    gui.msgbox(status, title="GMAIL SENDER")
    
remetente = FROM
senha = PASS
destinatario = TO
assunto = SUBJECT
mensagem = MSG

send_gmail(remetente, destinatario, senha, assunto, mensagem)