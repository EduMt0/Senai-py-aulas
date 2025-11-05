import streamlit as st
import math as mt

#Problema medidas
TITULO = "calculo de area de um Quadrado, Triangulo e Trapezio"
# st.title(TITULO)
st.markdown(f"<h1 style='text-align: center';>{TITULO}</h1>", unsafe_allow_html=True)

#Entrada de Dados
medidaA = st.number_input("Insert a medida A:")
medidaB = st.number_input("Insert a medida B:")
medidaC = st.number_input("Insert a medida C:")

#Processamento de Dados
areaQuadrado = mt.pow (medidaA, 2)
areaTriangulo = (medidaA + medidaB) / 2
areaTrapezio = ((medidaA + medidaC) * medidaB / 2)

#Saida de Dados
st.markdown(f"<h2 style = 'text-aling: left;'> Resultados:</h2>", unsafe_allow_html=True)
st.write(f"A area do Quadrado é: {areaQuadrado:.4f}")
st.write(f"A area do Triangulo é: {areaTriangulo:.4f}")
st.write(f"A area do Trapezio é: {areaTrapezio:.4f}")