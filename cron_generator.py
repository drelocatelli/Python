import os, subprocess
while 1:
    print("Para gerar o cron digite os valores numéricos.\n- Nulos serão considerados como Zero.")

    cron = {
        'minuto': input('Digite um minuto: '),

        'hora': input('Digite um hora: '),
    
        'fuso': input('Digite a diferença de fuso horário: '),

        'dia': input('Digite um dia: '),

        'mes': input('Digite um mês: '),

        'semana': input('Dia da semana: '),

        'ano': input('Digite um ano: ')
    }

    for k in cron.keys():
        # Semana nulo = ?
        if ( k == 'semana' ):
            if( cron[k] == '' ):
                cron[k] = '?'
        # Se nulo = 0
        elif( cron[k] == '' ):
            cron[k] = '0'
        
    
    # Replace se há zeros menor do que 10
    for i in cron:
        if( cron[i].isnumeric() and int(cron[i]) != 0 ):
            cron[i] = cron[i].replace('0','')


    # Fuso não pode ter asterisco
    if( cron['fuso'] == "*" ):
        cron['fuso'] = 0

    
    # Soma da hora com o fuso
    cron['hora'] = int(cron['fuso']) + int(cron['hora'])


    print(f"\n\nExpressão CRON:\n{cron['minuto']} {cron['hora']} {cron['dia']} {cron['mes']} {cron['semana']} {cron['ano']}\n\n")
 
    input("Continuar? $ ")
    
    os.system("clear -x")
    
    continue
