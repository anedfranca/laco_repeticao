from termcolor import colored


paleta1 = ['paleta de sombra', 150.00, 10, True]
paleta2 = ['paleta de blush', 80.00, 0, False]
paleta3 = ['paleta de contorno', 99.00, 5, False]

paletas = [paleta1, paleta2, paleta3] # matriz 😇

base1 = ['Virginia', 299.00, 0, False]
base2= ['Nina Secrets', 70.00, 10,True]
base3= ['Dior', 300.00, 25,  True]

bases = [base1, base2, base3]

corredor1 = [paletas, bases]


cont = 1
while True:
    print(colored("\nBem vindo a Wepink\n\n", "magenta"))
    opcao = int(input(colored('1. Listar todos os produtos\n'
                   '2. Listar produtos disponiveis e em promocao\n'
                   '3. Buscar um produto\n'
                   '4.\n'
                   '5.sair\n\n'
                   
                   'digite: \n', 'magenta')))
    print ()

    if opcao == 5:
        break

    elif opcao == 1:
        for categoria in corredor1:
            for produto in categoria:
                print(f'{cont}. {produto[0]} | {produto [1]}')
                cont+=1
        
        cont = 1
    elif opcao  == 2:
        for categoria in corredor1:
            for produto in categoria:
                if produto[2] > 0 and produto[3] == True:
                    print(f'{cont}. {produto[0]} | {produto [1]}')
                    cont+=1
        cont = 1
    elif opcao == 3:
        produto_pesquisado = input("Digite o nome do produto a ser procurado: ")

        foi_achado = False

        for categoria in corredor1:
            for produto in categoria:
                if (produto[0] == produto_pesquisado):
                    foi_achado = True
        
        # acabou a pesquisa
        if (foi_achado):
            print("\n achei")
        else:
            print("\n nao achei")










