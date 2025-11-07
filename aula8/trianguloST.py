import streamlit as st

def triangulo_perimetro(a,b,c):
    return a + b + c

def trapezio_area(a,b,c):
    return ((a + b) * c) /2

st.sidebar.title("Calculadora de Perimetro e Trapezio do Triângulo")
st.sidebar.markdown("Calcular 0 Perimetro e o Trapezio do Triângulo apartir dos dados a, b, c")

#Entrada de dados
a = st.number_input("Valor do lado a", format="%.2f", step=1.0)
b = st.number_input("Valor do lado b", format="%.2f", step=1.0)
c = st.number_input("Valor do lado c", format="%.2f", step=1.0)

#Estrutura de controle de decisão
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    area_trapezio = st.write("os valores formam um trapezio")
elif (a + b > c) or (a + c > b) or (b + c > a):
   perimetro_triangulo = st.write("os valores formam um triangulo")
else:
    st.write()


#Saida de dados
if st.button("Calcular", icon="📐"):
    if (a + b > c) or (a + c > b) or (b + c > a):
        triangulo_perimetro = a + b + c
        st.write(f"O Perimetro do Triângulo é: {triangulo_perimetro:.1f} metros")
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        trapezio_area = ((a + b) * c) /2
        st.write(f"A area do trapezio é: {trapezio_area:.1f} metros quadrados")
    else:
        st.write()


