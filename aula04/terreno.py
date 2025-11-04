#problema terreno

#decalaração variaveis
Largura : float
comprimento : float

#Entrada de dados
Largura = float(input("Digite a largura do terreno em metros: "))
comprimento = float(input("Digite o comprimento do terreno em metros: "))
valor_metro_quadrado = float(input("Digite o valor do metro quadrado do terreno em reais: "))

#processamento de dados
area = Largura * comprimento
preco = area * valor_metro_quadrado

#Saida de dados
print(f"A area do terreno é de {area}")
print(f"O preco do terreno é de R/$ {preco}")
