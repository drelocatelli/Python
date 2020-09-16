from PySimpleGUI import PySimpleGUI as sg

# Preview themes
# sg.preview_all_look_and_feel_themes()

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('DE'), sg.Input(key='de', size=(30,1))],
    [sg.Text('SENHA',text_color='red'), sg.Input(key='senha',password_char='*', size=(30,1))],
    [sg.Text('PARA'),sg.Input(key='para', size=(30,1))],
    [sg.Text('ASSUNTO'),sg.Input(key='subject', size=(30,1))],
    [sg.Text('MENSAGEM'),sg.Multiline(key='msg', size=(30,5))],
    [sg.Text("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")],
    [sg.Button('CANCELAR'), sg.Button('ENVIAR')]
]

# Janela
janela = sg.Window('G-mail Sender', layout)

# Ler os eventos
while True:
    #valores['de']
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "CANCELAR":
        break
    if eventos == "ENVIAR":
        if valores['de'] == "" or valores['senha'] == "" or valores['para'] == "" or valores['subject'] == "" or valores['msg'] == "":
            sg.popup("Preencha todos os campos!",title="Erro")
        else:
            import assets.config as send
            send.send_gmail(valores['de'], valores['para'], valores['senha'], valores['subject'], valores['msg'])
            
            sg.popup("E-mail enviado!\n\n\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n"+"DE: "+valores['de']+"\nPARA: "+valores['para']+"\nASSUNTO: "+valores['subject']+"\nMENSAGEM:\n"+valores['msg'],title="status")