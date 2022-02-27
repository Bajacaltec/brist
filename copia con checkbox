from email.utils import collapse_rfc2231_value
import streamlit as st
fol1,fol2=st.columns(2)
with fol1:
    st.title("                            BristolApp")

with fol2:
    st.image("WAPP.png",None,350)

st.subheader("Identifica el tipo de evacuaciones que tienes y verémos si necesitas ajustar tu dieta")
col1,col2,col3,col4,col5,col6,col7=st.columns(7)

with col1:
    st.image('B1.png')
    st.markdown("Pedazos duros separados. Como nueces y con excreción difícil")
    bri1=st.checkbox("B1")
with col2:
    st.image("B2.png")
    st.markdown("Con forma de salchicha, pero grumosa (compuesta de fragmentos")
    bri2=st.checkbox('B2')
with col3:
    st.image("B3.png")
    st.markdown("Con forma de salchica, pero con grietas en la superficie")
    bri3=st.checkbox('B3')
with col4:
    st.image("B4.png")
    st.markdown('Con forma de salchica pero lisa y suave')
    bri4=st.checkbox('B4')
with col5:
    st.image('B5.png')
    st.markdown("Trozos de pastosos con bordes bien definidos")
    bri5=st.checkbox('B5')
with col6:
    st.image('B6.png')
    st.markdown("Pedazos blandos y esponjosos con bordes irregulares")
    bri6=st.checkbox('B6')
with col7:
    st.image('B7.png')
    st.markdown('Acuosa, sin pedazos sólidos, totalmente líquida')
    bri7=st.checkbox('B7')
if bri1==True:
    with col1:
        st.subheader("B1")
        st.warning("Característico del estreñimiento, debes aumentar el consumo de fibra, o iniciar el consumo de fibra en suplementos como el Psyllium plantago, 1 cucharada con 1 litro de agua diariamente")
if bri2==True:
    with col2:
        st.subheader("B2")
        st.warning('Característico del estreñimiento, debes aumentar el consumo de fibra, o iniciar el consumo de fibra en suplementos como el Psyllium plantago, 1 cucharada con 1 litro de agua diariamente')
if bri3==True:
    with col3:
        st.subheader('B3')
        st.success('Excelente, tus heces son normales no debes realizar cambios en tu dieta respecto a la forma de tus heces')
    st.balloons()
if bri4==True:
    with col4:
        st.subheader('B4')
        st.success('Excelente, tus heces son normales no debes realizar cambios en tu dieta respecto a la forma de tus heces')
    st.balloons()
if bri5==True:
    with col5:
        st.subheader('B5')
        st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')
if bri6==True:
    with col6:
        st.subheader('B6')
        st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')
if bri7==True:
    with col7:
        st.subheader('B7')
        st.warning('Existe un paso acelerado de las heces, puede deberse a un tránsito intestinal rápido, uso de laxantes o alteraciones en la absorción, amerita investigación médica')
st.select_slider('Elige',['B1','B2','B3','B4','B5','B6','B7'])

      




