from termcolor import colored

carrinho = []
valor_total = 0
itens_comprados = 0

paleta1 = ['paleta de sombra', 150.00, 10, True]
paleta2 = ['paleta de blush', 80.00, 0, False]
paleta3 = ['paleta de contorno', 99.00, 5, False]

paletas = [paleta1, paleta2, paleta3] # matriz 😇

base1 = ['Virginia', 299.00, 0, False]
base2= ['Nina Secrets', 70.00, 10,True]
base3= ['Dior', 300.00, 25,  False]

bases = [base1, base2, base3]

batom1 = ['Mac', 300.00, 5, False]
batom2 = ['Frann', 50.00, 10, True]
batom3 = ['Nix', 200.00, 25,  False]
batom4 = ['Boca rosa', 40.00, 0,  True]

batons = [batom1, batom2, batom3, batom4]

corredor1 = [paletas, bases, batons]


cont = 1
while True:
    print(colored("\nBem vindo a Wepink\n\n", "magenta"))
    opcao = int(input(colored('1. Listar todos os produtos\n'
                   '2. Listar produtos disponiveis e em promocao\n'
                   '3. Buscar um produto\n'
                   '4. Comprar um produto\n'
                   '0. Sair\n\n'
                   
                   'digite: ', 'magenta')))
    print ()

    if opcao == 0:
        print(colored('Carrinho de compras \U0001f6cd\uFE0F \n', "magenta"))
        for i in carrinho:
            print(i[0].title())
            print(f'{i[1]} - {i[2]}')
            print()

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
        if (foi_achado and produto [3]):
            print(f"\n Produto encontrado. Esta na promocao \n {produto_pesquisado} | {produto [1]}")
        elif foi_achado:
            print(f"\n Produto encontrado. Nao esta na promocao \n {produto_pesquisado} | {produto [1]}")
            
    elif opcao == 4:
        for categoria in corredor1:
            for produto in categoria:
                if (produto[2] > 0): # Disponível / Em estoque
                    print(f'{cont}. {produto[0]} | {produto [1]}')
                    cont+=1
        
        cont = 1

        qual_produto = input("Digite o nome do produto desejado: ")
        
        for categoria in corredor1:
            for produto in categoria:
                if produto[0] == qual_produto:
                    qtde_produto = int(input('Digite a quantidade: '))

                    while True: 
                        if qtde_produto <= produto[2]: # se é valido
                            valor_por_produto = qtde_produto * produto[1]
                            valor_total += valor_por_produto
                            
                            break
                        else:
                            print("\nA qtde inserida não é valida")
                            print(f"Tem {produto[2]} unidades\n")

                            qtde_produto = int(input('Digite a quantidade: '))

                    produto[2] -= qtde_produto

                    print(f'Uma unidade custa {produto[1]}, Portanto o total deu: ')
                    print(f'R${produto[1] * qtde_produto :.2f}')
                    print(f'O valor total deu {valor_total}')

                    produto = [qual_produto.title(), qtde_produto, valor_por_produto]

                    carrinho.append(produto)
                    
                    
                    #######


'''
Corrigir os prints do valores ( R$ 300.00 )
Criar um valor_total pra saber quanto o usuario gastou no programa

Desafio: Ao finalizar o programa, exibir um carrinho de compras
        Mostrando os itens que o usuario comprou, a qtde, preco unitario, valor por item
'''







