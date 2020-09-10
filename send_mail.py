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

    print('\n')
    print("="*50)
    print(f"DE: {email['from']}")
    print(f"PARA: {email['to']}")
    print(f"ASSUNTO: {email['assunto']}")
    print(f"MENSAGEM: {email['msg']}")
    print("="*50)
    print("E-mail enviado!")
    print('\n')
    
remetente = input("[DE] $ ")
from getpass import getpass
senha = getpass("[SENHA DO E-MAIL] $ ")
print(senha)
destinatario = input("[PARA] $ ")
assunto = input("[ASSUNTO] $ ")
mensagem = input("[MENSAGEM] $ ")

send_gmail(remetente, destinatario, senha, assunto, mensagem)
