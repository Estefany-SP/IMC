st.title("Calculadora de Índice de Masa Corporal IMC")
st.header('''
Introduccion: 
El índice de masa corporal (IMC) es un número que se calcula con base en el peso y la estatura de la persona. Para la mayoría de las personas, el IMC es un indicador confiable de la gordura y se usa para identificar las categorías de peso que pueden llevar a problemas de salud.''')
st.image('https://www.lavanguardia.com/files/article_main_microformat/uploads/2017/06/16/5fa3c57bc8fa5.jpeg')
st.latex(r'''IMC = \frac{peso}{estatura^2}''')
peso = st.number_imput('Escriba su peso en Kg',50)
st.write(peso)
estatura = st.number_imput('Escriba su estatura en metros',1.6)
st.write(estatura)
imc = peso/estatura**2
imc = round(imc,3)
cal=st.button('Calcular')
st.write(cal)
if cal==True:
  st.write('# El IMC es:',imc,'kg/m2')