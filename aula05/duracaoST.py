import streamlit as st

#Problema duração de tempo
TITULO = "Calculadora de Duração de Tempo"
st.set_page_config(page_title=TITULO)
st.title (TITULO)

#Entrada de Dados
Tempo = st.number_input("Digite o tempo em segundos:", min_value = 0, step = 1, help = "Insira a duração total em segundos para converter em horas, minutos e segundos.")

#Processamento de Dados
horas = Tempo // 3600
minutos = (Tempo % 3600) // 60
segundos = Tempo % 60

#Saida de Dados
st.write(f"{horas} horas, {minutos} minutos e {segundos} segundos.")

