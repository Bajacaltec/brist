from email.utils import collapse_rfc2231_value
from enum import auto
import streamlit as st

#Con esto puedes utilizar toda la pantalla para las columnas, en telefono no hay cambios
st.set_page_config(layout="wide")
#En st.columns si les pones en el parentesis ((2,1)) la primera columna es el doble de grande que la segunda
fol1,fol2=st.columns(2)
with fol1:
    st.title("BristolApp")

with fol2:
    st.image("WAPP.png",None)

st.subheader("Identifica el tipo de evacuaciones que tienes y verémos si necesitas ajustar tu dieta")
st.info("Desplazate por las imagenes hasta que encuentres el tipo de evacuación que tienes comunmente y posteriormente moviliza  la barra inferior para elegir la escala de Bristol que corresponda(B)")
col1,col2,col3,col4,col5,col6,col7=st.columns(7)

with col1:
    st.subheader('B1')
    st.image('B1.png',None,100)
    st.markdown("Pedazos duros separados. Como nueces y con excreción difícil")
with col2:
    st.subheader('B2')
    st.image("B2.png",None,100)
    st.markdown("Con forma de salchicha, pero grumosa (compuesta de fragmentos")
with col3:
    st.subheader("B3")
    st.image("B3.png",None,100)
    st.markdown("Con forma de salchica, pero con grietas en la superficie")
with col4:
    st.subheader('B4')
    st.image("B4.png",None,100)
    st.markdown('Con forma de salchica pero lisa y suave')
with col5:
    st.subheader("B5")
    st.image('B5.png',None,100)
    st.markdown("Trozos pastosos con bordes bien definidos")
with col6:
    st.subheader("B6")
    st.image('B6.png',None,100)
    st.markdown("Pedazos blandos y esponjosos con bordes irregulares")
with col7:
    st.subheader("B7")
    st.image('B7.png',None,100)
    st.markdown('Acuosa, sin pedazos sólidos, totalmente líquida')
st.info("Selecciona desplazando la barra inferior de izquierda a derecha")
selecccion=st.select_slider('Elige',['Bristol','B1','B2','B3','B4','B5','B6','B7'],None)

yol1,yol2=st.columns(2)
if selecccion=='B1':
    with yol1:
        st.warning("Característico del estreñimiento, debes aumentar el consumo  de agua a 2-3 litros al día y de fibra o iniciar el consumo de fibra en suplementos como el Psyllium plantago tomando 1 cucharada con 1 litro de agua diariamente")
    with yol2:
        st.error("Recuerda que el estreñimiento crónico puede llevar al desarrollo de múltiples enfermedad")

elif selecccion=='B2':
    with yol1:
        st.warning('Característico del estreñimiento, debes aumentar el consumo de agua a 2-3 litros diario y el consumo de fibra o iniciar el consumo de fibra en suplementos como el Psyllium plantago tomando 1 cucharada con 1 litro de agua diariamente')
    with yol2:
        st.error("Recuerda que el estreñimiento crónico puede llevar al desarrollo de múltiples enfermedad")
elif selecccion=='B3':
    st.success('Excelente, tus heces son normales no debes realizar cambios en tu dieta respecto a la forma de tus heces')
    st.balloons()
elif selecccion=='B4':
    st.success('Excelente, tus heces son normales no debes realizar cambios en tu dieta respecto a la forma de tus heces')
    st.balloons()
if selecccion=='B5':
    st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')
if selecccion=='B6':
    st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')
if selecccion==True:
    st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')

#Un expansor para esconder cosas
# with st.expander("Abre para ver mas"):
#     st.image("bristol.png")
#     if selecccion=='B1':
#         st.warning('Ph')


