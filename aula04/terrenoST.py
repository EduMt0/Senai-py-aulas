import streamlit as st 

st.title("Analise de terreno")

#Entrade de dados
st.write("Digite a largura do terreno em motros:")
largura = st.number_input("largura (m):")
st.write("Digite o comprimento do terreno em metros:")
comprimento = st.number_input("comprimento (m):")
valor_m2 = st.number_input("Valor do m2 (R$):")

#Processamento de Dados
area = largura * comprimento
preco = area * valor_m2

#Saida de Dados
st.write(f"A area do terreno é de {area} metros quadrados")
