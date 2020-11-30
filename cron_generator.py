import os
while 1:
    print("Para gerar o cron digite os valores numéricos.\n- Nulos serão considerados como Zero.")

    minuto = input("Digite um minuto: ")

    hora = input("Digite um horário: ")
    
    fuso = input("Digite a diferença de fuso horário: ")

    dia = input("Digite um dia: ")

    mes = input("Digite um mês: ")

    ano = input("Digite um ano: ")

    
    # Replace se há zeros menor do que 10
           
    if(int(fuso) < 10 and int(fuso) != 0):
        fuso = fuso.replace('0','')
    
    if(hora.isnumeric()):
        if (int(hora) < 10 and int(hora) != 0):
            hora = str(hora).replace('0','')
        hora = int(fuso) + int(hora)
        
    if(minuto.isnumeric()):    
        if(int(minuto) < 10 and int(minuto) != 0):
            minuto = minuto.replace('0','')
            
    if(dia.isnumeric()):    
        if(int(dia) < 10 and int(dia) != 0):
            dia = dia.replace('0','')
            
    if(mes.isnumeric()):    
        if(int(mes) < 10 and int(mes) != 0):
            mes = mes.replace('0','')


    print(f"\n\nExpressão CRON:\n{minuto} {hora} {dia} {mes} ? {ano}\n\n")

    input("Continuar? $ ")
    
    os.system("clear -x")
    
    continue