def send_gmail(remetente, destinatario, senha, mensagem):
    import smtplib
    email_from = remetente
    email_to = destinatario
    email_pass = senha
    smtp = "smtp.gmail.com"
    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email_from, email_pass)
    msg = mensagem
    server.sendmail(email_from, email_to, msg)
    server.quit()
    print("Sucesso ao enviar o email")
    
remetente = input("[E-MAIL QUE ENVIARÁ A MSG] $ ")
senha = input("[SENHA DO E-MAIL] $ ")
destinatario = input("[E-MAIL QUE RECEBERÀ A MSG] $ ")
mensagem = input("[MENSAGEM] $ ")

send_gmail(remetente, destinatario, senha, mensagem)
