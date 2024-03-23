base1 = ['Virginia' , 299]
base2 = ['Rhianna', 400]
base3 = ['Dior', 450]
base4 = ['Jequiti', 12]

loja = [base1, base2, base3, base4]

qual_base = input('\n BASES: Virginia \n Rhianna \n Dior\n Digite qual base voce deseja comprar: \n')
qtde_base = int(input('Digite quantas bases voce deseja: \n'))


for i in loja:
    if (i[0] == qual_base):
        print (f'{i[1] * qtde_base}.00 R$')
        

