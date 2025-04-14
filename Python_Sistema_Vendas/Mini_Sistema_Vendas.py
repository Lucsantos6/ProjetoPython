def venda_de_produto():
 print(" ******** VENDA DE PRODUTO*****")

 while True:
    try:
        n = input("Digite o nome do produto : ")
        if not n.isalpha():
            raise ValueError("O nome do produto pode conter apenas letras")
        break
    except ValueError as erro:
       print(erro)

 while True:
    try:
     p = input("Digite o preço do produto:")
     p1 = float(p)
     break
    except ValueError as erro2:
        print(" Apenas números são aceitos no valor do produto")

 while True:
    try:
     q = input("Digite a quantidade do produto:")
     q1 = float(q)
     break
    except ValueError as erro2:
        print(" Apenas números são aceitos na quantidade do produto")
 print( 'Apenas números são permitidos nos campos quantidade e preço')


 vt = p1 *q1

 print(F"O Valor total da venda selecionado será de R${vt:.2f}")
 
 while True:
     mp = input("Qual sera o metodo de pagamento : 1.dinheiro 2.pix 3.cartão(credito/debito) ? ")
     if mp ==  '1':
      print(" -> Você escolheu Dinheiro. O pagamento foi realizado em Dinheiro")
      break       
     elif mp == '2':
      print(" -> Você escolheu Pix. O pagamento foi realizado via Pix")        
      break
     elif mp == '3':
      print(" -> Você escolheu Cartão. O pagamento foi realizado no Cartão(crédito/débito)")
      break
     else:
      print(" -> Método de pagamento inválido, por favor,selecione um método válido")
 print("Volte logo, esperamos por você ! ")
         

venda_de_produto()


            
