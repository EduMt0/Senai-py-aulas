import streamlit as st

def grafico(datsu1,datsu2,datsu3):
#Apresentação do grafico
    st.area_chart([0, datsu1], use_container_width=True, height=200, color="#0015ff")
    st.area_chart([0, datsu2], use_container_width=True, height=200, color="#ccff00")
    st.area_chart([0, datsu3], use_container_width=True, height=200, color="#ff0022")




st.title("🎯 Simulação de Lançamento de Dardo 🎯")
'''Simulação de lançamento de tres dardos. 
Objetivo do aplicativo é mostrar o dardo com a maior distância'''

#Entrada de Dodos
st.header("Inserir as tres distâncias dos dardos lançados pelo jogador.")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("Distancia do 1° dardo", min_value=0)
with coluna2:
    dardo2 = st.number_input("Distancia do 2° dardo", min_value=0)
with coluna3:
    dardo3 = st.number_input("Distancia do 3° dardo", min_value=0)
maior_distancia = max(dardo1,dardo2,dardo3)

#Estrutura de contole de decisão
if (dardo1 > dardo2) and (dardo1 > dardo3):
    dardo_vencedor = "dardo1"
elif (dardo2 > dardo1) and (dardo2 > dardo3):
    dardo_vencedor = "dardo2"
elif (dardo1 == dardo2) and (dardo1 == dardo3) or (dardo2 == dardo3):
    dardo_vencedor = "Empate entre os dardos"
else:
    dardo_vencedor = "dardo3"

#Saida de Dados
if st.button("Apresentar resultados do Lançamento"):
    if dardo_vencedor == "Empate entre os dardos":
        st.write("Houve um empate entre os dardos")
    else:
        st.write(f"O dardo com a maior distância foi o {dardo_vencedor} com {maior_distancia} metros")
        grafico(dardo1,dardo2,dardo3)