from streamlit import header, write, text_input, button, warning, success, error
from math import pow, sqrt, z

#Função Python
def calculo(Delta):
   valor = (sqrt(Delta)) / (2 * a)
   return valor

#Cabeçalho
header("Calculadora de Bhaskara")
write("Calculadora de Raízes \n" \
" de uma equação de 2º Grau")
write("ax² + bx + c = 0")

#Entrada e Dados
a = text_input("Digite o valor de a:")
b = text_input("Digite o valor de b:")
c = text_input("Digite o valor de c:")

#Processamento de Dados
if button("Calcular Raízes"):
    try:
      a = float(a)  #convertendo string para float
      b = float(b)  #convertendo string para float
      c = float(c)  #convertendo string para float
      Delta = pow(b,2) - 4 * a * c
      if Delta < 0:
         warning(f"A equação não possui raízes reais:")
      elif Delta == 0:
         raiz = (-b + calculo(Delta))
         success(f"A equação possui uma raiz real: {raiz:.2f}")
      else:
         raiz1 = (-b + calculo(Delta))
         raiz2 = (-b - calculo(Delta))
         success(f"As raizes da equação são: \n Raiz 1:{raiz1:.2f} \n Raiz 2: e {raiz2:.2f}")

    except ValueError:
      error("Por favor, insira valores validos para a, b  e c.")
    except ZeroDivisionError:
       error("O avlor de 'a' não pode ser zero em uma equação de 2º grau.")