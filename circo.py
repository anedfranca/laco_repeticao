
bilheteria = 0
lanchonete = 0
votos_grupo = 0
votos_bamboleiras = 0
votos_trapezistas = 0

for i in range (5):
    tipo_ingresso = str(input('\ntipos de ingresso:' + '\n'
                        'meia: 25,00' + '\n'
                        'inteira: 50,00' + '\n'
                        'ingresso social: 30,00' + '\n\n'))
    
    if (tipo_ingresso == 'meia'):
        custo_ingresso = 25
    elif (tipo_ingresso == 'inteira'):
        custo_ingresso = 50
    elif (tipo_ingresso == 'ingresso social'):
        custo_ingresso = 30
    print (f'{custo_ingresso},00 reais\n')

    bilheteria = bilheteria + custo_ingresso

    #################################################################

    comida = str(input('\nqual comida voce deseja? cachorro quente (10,00) ou '
                        'algodao doce(15,00)?\n'))
    if (comida == 'cachorro quente'):
        custo_alimentacao = 10
    else:
        custo_alimentacao = 15



    bebida = input('\nvoce deseja bebida? Y\n')
    if (bebida == 'y'):
        custo_alimentacao += 10
    print (f'\n{custo_alimentacao},00 reais')

    lanchonete += custo_alimentacao 

####################################################################
    atracao_desejada = input('\nqual atracao voce mais gostou?\n'
                               'grupo de palhacos = g\n'
                               'bamboleiras = b\n'
                               'trapezistas = t\n') 
    if (atracao_desejada == 'g'):
        votos_grupo +=1
    elif (atracao_desejada == 'b'):
        votos_bamboleiras +=1
    elif (atracao_desejada == 't'):
        votos_trapezistas +=1


lista_votos = [votos_grupo, votos_bamboleiras, votos_trapezistas]
maior = max(lista_votos)
if (votos_grupo == maior):
    print(f'a atracao mais votado foi grupo de palhacos')

if (votos_bamboleiras == maior):
    print(f'a atracao mais votado foi as bamboleiras')

if (votos_trapezistas == maior):
    print(f'a atracao mais votado foi os trapezistas')
    


valor_apurado = bilheteria + lanchonete
print (f'\no valor apurado da noite foi R$ {valor_apurado},00 reais')
