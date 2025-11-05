import streamlit as st #Framework Streamlit
import math as mt      #Biblioteca 

#Problema RetângulO
TITULO ="Problema Retângulo"
st.title(TITULO)

#Entrada de Dados
base = st.number_input("Digite a base do retângulo:", min_value = 0.0, format = "%.1f")
altura = st.number_input("Digite a altura do retângulo:", min_value = 0.0, format = "%.1f")

#Processamento de Dados
area = base * altura
perimetro = 2 * base + altura * 2
# diagonal = (base  ** 2 + altura ** 2) ** 0.5
x = mt.pow(base, 2) + mt.pow(altura, 2)
diagonal = mt.sqrt(x)

#Saida de Dados
st.write(f"A àrea do retângulo é: {area}")
st.write(f"O perímetro do retângulo é: {perimetro}")
st.write(f"A diagonal do retângulo é: {diagonal:.2}")