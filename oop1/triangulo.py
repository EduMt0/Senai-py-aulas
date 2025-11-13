#Problema triangulo sem oop
#Entrada de dados

#Triangulo X
print("Inserir as Medidas do Triangulo X")
ax = int(input("Digite a medida a:"))
bx = int(input("Digite a medida b:"))
cx = int(input("Digite a medida c:"))

#Triangulo Y
print("Inserir as Medidas do Triangulo Y")
ay= int(input("Digite a medida do a:"))
by= int(input("Digite a medida do b:"))
cy= int(input("Digite a medida do c:"))

#Processamento de dados
p = (ax + bx + cx) / 2
areax = (p * (p - ax) * (p - bx) * (p - cx)) ** 0.5
p = (ay + by + cy) / 2
areay = (p * (p - ay) * (p - by) * (p - cy)) ** 0.5
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