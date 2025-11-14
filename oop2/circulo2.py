from calculadora import calculadora1

#Entrada de dados
raio = float(input("Digite o valor do raio: "))

#Processamento de dados
circuferencia = calculadora1.circuferencia(raio)
area = calculadora1.area(raio)

#Saida de dados
print(f''' Circunferencia: {circuferencia:.2f}
    area = {area:.2f}
    PI = {calculadora1.PI}
''')
