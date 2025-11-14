import produtoOOP as p 
p1 = p.produto()

#entrada de dados
print("Digite as dados do produto")
p1.nome = input("\tnome: ")
p1.preco = float(input("\tpreco: R$"))
p1.saldo = int(input("\tquantidade:"))

#Saida de dados 1
print(p1.dados_produto())

#Adicionar produtos
q = int(input("Digite o número de produtos a ser adicionado ao  estoque: "))
p1.adicionar_produtos(q)

#Saida de dados 2
print("--Dados Atualizado--")
print(p1.dados_produto())

#remover produtos
q = int(input("Digite o número de produtos a ser adicionado ao  estoque: "))
p1.remover_produtos(q)

#Saida de dados 3
print("--Dados Atualizado--")
print(p1.dados_produto())

