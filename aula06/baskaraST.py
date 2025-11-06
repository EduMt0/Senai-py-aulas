import streamlit as st
import math as mt 

st.header("Calculadora de Bhaskara")
st.write("Calculadora de Raízes \n" \
" de uma equação de 2º Grau")
st.write("ax² + bx + c = 0")

#Entrada e Dados
a = st.text_input("Digite o valor de a:")
b = st.text_input("Digite o valor de b:")
c = st.text_input("Digite o valor de c:")

#Processamento de Dados
if st.button("Calcular Raízes"):
    try:
      a = float(a)  #convertendo string para float
      b = float(b)  #convertendo string para float
      c = float(c)  #convertendo string para float
      Delta = mt.pow(b,2) - 4 * a * c
      if Delta < 0:
         st.warning(f"A equação não possui raízes reais:")
      elif Delta == 0:
         raiz = (-b + mt.sqrt(Delta)) / (2 * a)
         st.success(f"A equação possui uma raiz real: {raiz:.2f}")
      else:
         raiz1 = (-b + mt.sqrt(Delta)) / (2 * a)
         raiz2 = (-b - mt.sqrt(Delta)) / (2 * a)
         st.success(f"As raizes da equação são: \n Raiz 1:{raiz1:.2f} \n Raiz 2: e {raiz2:.2f}")




    except:
      st.error("Por favor, insira valores validos para a, b e c.")
