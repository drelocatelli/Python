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
    
    

