import streamlit as st

def celsius_faherenheit(temp):
    return (temp * 1.8) + 32
def celsius_kelvin(temp):
    return temp + 273.15
def F_celsius(temp):
    return (temp - 32) * 5/9
def F_kelvin(temp):
    return F_celsius(temp) + 273.15
def K_celsius(temp):
    return temp - 273.15
def k_fahrenheit(temp):
    return celsius_faherenheit(K_celsius(temp))

#Problema Temperatura
st.sidebar.title("Conversor de Temperatura")
st.title("Conversor de Temperatura °C para °F e K")
st.sidebar.markdown("Converte a temperaturaentre entre Celsius, Fahrenheit e Kelvin")
celsius_selecionar = st.sidebar.checkbox("celsius", key="temp_celsius")
fahrenheit_selecionar = st.sidebar.checkbox("Fahrenheit", key="temp_Fahrenheit")
kelvin_selecionar = st.sidebar.checkbox("Kelvin", key="temp_Kelvin")

opcao_selecionada = st.sidebar.radio(options=[])
#Entrada de Dados
temp = st.number_input("Valor da Temperatura", format="%.2f", step=1.0)

if celsius_selecionar + fahrenheit_selecionar + kelvin_selecionar > 1:
    st.sidebar.error("Por favor, selecione apenas uma unidade de temperatura.")


#Processamento de Dados
if st.button("Converter", icon="🔄"):
    if celsius_selecionar:
        st.write(f"{temp} °C em Fahrenheit é: {celsius_faherenheit(temp):.2f}°F")
        st.write(f"{temp} °C em Kelvin é: {celsius_kelvin(temp):.2f}°K")
    elif fahrenheit_selecionar:
        st.write(f"{temp} °F em Celsius é: {F_celsius(temp):.2f} °C")
        st.write(f"{temp} °F em Kelvin é: {F_kelvin(temp):.2f} °K")
    elif kelvin_selecionar:
        st.white(f"{temp} °K em Celsius é: {K_celsius(temp):.2f} °C")
        st.write(f"{temp} °K em Fahrenheit é: {k_fahrenheit(temp):.2f} °F")
