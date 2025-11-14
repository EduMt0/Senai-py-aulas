import produtoOOP as p 
p1 = p.produto()

#entrada de dados
print("Digite as dados do produto")
p1.nome = input("\tnome: ")
p1.preco = float(input("\tpreco: R$"))
p1.saldo = int(input("\tquantidade"))

#Saida de dados 1
print("Dados do produto")
print(f"\tNome do produto: {p1.nome}")
print(f"\tValor da compra: R$ {p1.preco}")
print(f"\tvalor total em estoque: R$ {p1.valor_total_estoque()}")