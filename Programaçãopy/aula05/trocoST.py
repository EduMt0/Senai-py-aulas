import streamlit as st
import math as mt

TITULO = "Calculadorar Troco"
st.set_page_config(page_title=TITULO)
st.title (TITULO)

#Entrada de Dados
Preco_Unitario = st.number_input("Digite o valor do Produto:", min_value = 1)
Quantidade = st.number_input("Digite a quantidade de itens:", min_value = 1)
Valor = st.number_input("Digite o valor que da/das notas:", min_value = 0.1)

#Processamento de Dados
Valor_a_Pagar = Quantidade * Preco_Unitario
troco_cliente = Valor - Valor_a_Pagar

#Saida de Dados
st.write (f"O troco será igual á: R$ {troco_cliente:.2f}")