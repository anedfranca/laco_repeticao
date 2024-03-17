import math
'''passo 1: criacao das constantes 
passo 2: receber as entradas
passo 3: fazer as contas necessarias
passo 4: exibir a saida formatada
'''
CAIXA_PREGOS = 12
PRECO_CAIXA = 7.89
total_prego = 0

while True:
    qtde_pregos = int(input('quantos pregos voce usou?\n'))
    if (qtde_pregos % 2 == 0):
        total_prego += qtde_pregos
    else: 
        break

n_caixas = math.ceil(total_prego/CAIXA_PREGOS)
print (f'{(n_caixas * PRECO_CAIXA):.2f}')

sobrou = (CAIXA_PREGOS * n_caixas) - total_prego
print (f'sobraram {sobrou} pregos')