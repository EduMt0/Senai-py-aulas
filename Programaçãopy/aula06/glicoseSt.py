import streamlit as st

TITULO = "Classificação de níveis de Glicose no Sangue"
st.set_page_config("Classificação de níveis")
st.title (TITULO)

st.markdown("""
     | Nível de glicose| Classificação |
     |-----------------|---------------|
     | 0 - 70        | Hipoglicemia    |
     | 71 - 100      | Normal          |
     | 101 - 140     | Pré-Diabetico   |
     | 141 ou mais   | Diabetico       |
"""
)
#Entrada de Dados
glicose = st.number_input("Digite o valor da glicose no Sangue (mg/dL):", min_value =0)

#Processamento e Saída de Dados
if st.button("Classificar"):
    if glicose <= 70:
        st.write("Nivel de Glicose classificado como: Hipoglicemia")
    elif glicose <= 100:
        st.write("Nivel de Glicose classificado como: Normal")
        st.balloons()
    elif glicose <= 140:
        st.write("Nivel de Glicose classificado como: Pré-Diabetico")
    else:
        st.write("Nivel de Glicose classificado como: Diabetico")