import trianguloOOp as tl 

#Instanciar a classe
triangulox = tl.triangulo()
trianguloy = tl.triangulo()

#Entrada de dados
print("Digite as medidas do Triangulo X")
triangulox.a = int(input("Digite a medida a:"))
triangulox.b = int(input("Digite a medida b:"))
triangulox.c = int(input("Digite a medida c:"))
print("Digite as medidas do Triangulo Y")
trianguloy.a = int(input("Digite a medida a:"))
trianguloy.b = int(input("Digite a medida b:"))
trianguloy.c = int(input("Digite a medida c:"))

#Processamento de dados
p = (triangulox.a + triangulox.b + triangulox.c) / 2
areax = (p * (p - triangulox.a) * (p - triangulox.b) * (p - triangulox.c)) ** 0.5
p = (trianguloy.a + trianguloy.b + trianguloy.c) / 2
areay = (p * (p - trianguloy.a) * (p - trianguloy.b) * (p - trianguloy.c)) ** 0.5

#Condicional para a verificação dos dados
if areax > areay:
    saida = "A area do Triangulo X é maior q do Triangulo Y"
elif areay > areax:
    saida = "A area do Triangulo Y é maior q do Triangulo X"
else: 
    saida = "As areas do Triangulo são iguais"

#Saida de dados
print(f"A area do Triangulo X=:{areax:.1f}")
print(f"A area do Triangulo Y=:{areay:.1f}")
print(saida)