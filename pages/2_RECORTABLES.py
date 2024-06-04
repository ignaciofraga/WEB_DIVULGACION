# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2023

@author: ifraga
"""

import streamlit as st
from PIL import Image

logo_IEO_reducido    = 'DATOS/IMAGENES/ieo.ico'
logo_IEO_principal   = 'DATOS/IMAGENES/LOGOS.jpg' 

foto_lura            = 'DATOS/IMAGENES/LURA.jpg'    
foto_alvarino        = 'DATOS/IMAGENES/ALVARIÑO.jpg'
foto_margalef        = 'DATOS/IMAGENES/MARGALEF.jpg'
foto_navarro         = 'DATOS/IMAGENES/PNAVARRO.jpg'
foto_mytilus         = 'DATOS/IMAGENES/MYTILUS.jpg'

archivo_recortable_lura      = 'DATOS/RECORTABLES/LURA.pdf'
archivo_recortable_alvarino  = 'DATOS/RECORTABLES/ANGELES_ALVARIÑO.pdf'
archivo_recortable_margalef  = 'DATOS/RECORTABLES/RAMON_MARGALEF.pdf'
archivo_recortable_mytilus  = 'DATOS/RECORTABLES/MYTILUS.pdf'
archivo_recortable_paula_navarro  = 'DATOS/RECORTABLES/FRANCISCO_PAULA_NAVARRO.pdf'



imagen_logo   = Image.open(logo_IEO_reducido)
st.set_page_config(page_title="DIVULGACION IEO-CORUÑA",page_icon=logo_IEO_reducido)  # , layout="wide"


logo_cabecera = Image.open(logo_IEO_principal) 
st.image(logo_cabecera)

# TITULO PRINCIPAL
texto = 'Monta los barcos del Instituto Español de Oceanografía en tu propia casa !!'
titulo_principal = '<p style="text-align:  center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

# DESCARGA RECORTABLES

col1, col2, col3 = st.columns(3,gap="large")

with col1:

    titulo_secundario = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Lura</p>'

    st.markdown(titulo_secundario, unsafe_allow_html=True)    

    imagen_pagina = Image.open(foto_lura)   
    st.image(imagen_pagina)

    with open(archivo_recortable_lura, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="DESCARGAR RECORTABLE",
                    data=PDFbyte,
                    file_name="RECORTABLE_LURA_IEO.pdf",
                    mime='application/octet-stream')

with col2:

    titulo_secundario = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Ángeles Alvariño</p>'
    st.markdown(titulo_secundario, unsafe_allow_html=True)    

    imagen_pagina = Image.open(foto_alvarino)
    st.image(imagen_pagina)     

    with open(archivo_recortable_alvarino, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="DESCARGAR RECORTABLE",
                    data=PDFbyte,
                    file_name="RECORTABLE_ALVARIÑO_IEO.pdf",
                    mime='application/octet-stream')

with col3:

    titulo_secundario = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Ramón de Margalef</p>'
    st.markdown(titulo_secundario, unsafe_allow_html=True)    

    imagen_pagina = Image.open(foto_margalef)
    st.image(imagen_pagina)     

    with open(archivo_recortable_margalef, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="DESCARGAR RECORTABLE",
                    data=PDFbyte,
                    file_name="RECORTABLE_MARGALEF_IEO.pdf",
                    mime='application/octet-stream')







col1, col2 = st.columns(2,gap="large")

with col1:

    titulo_secundario = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Mytilus</p>'

    st.markdown(titulo_secundario, unsafe_allow_html=True)    

    imagen_pagina = Image.open(foto_mytilus)   
    st.image(imagen_pagina)

    with open(archivo_recortable_mytilus, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="DESCARGAR RECORTABLE",
                    data=PDFbyte,
                    file_name="RECORTABLE_MYTILUS_IEO.pdf",
                    mime='application/octet-stream')

with col2:

    titulo_secundario = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Francisco de Paula Navarro</p>'
    st.markdown(titulo_secundario, unsafe_allow_html=True)    

    imagen_pagina = Image.open(foto_navarro)
    st.image(imagen_pagina)     

    with open(archivo_recortable_paula_navarro, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="DESCARGAR RECORTABLE",
                    data=PDFbyte,
                    file_name="RECORTABLE_PAULA_NAVARRO_IEO.pdf",
                    mime='application/octet-stream')



# #titulo_secundario = '<p style="text-align: center;font-family:Gothic Light; font-size: 20px;"> Imprime los planos en un A3, monta el barco y comienza a navegar</p>'
# titulo_secundario = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Imprime los planos, monta el barco y comienza a navegar.</p>'

# st.markdown(titulo_secundario, unsafe_allow_html=True)
    
# with open(archivo_recortable, "rb") as pdf_file:
#     PDFbyte = pdf_file.read()

# col1, col2, col3, col4, col5 = st.columns(5,gap="small")

# with col3:

#     st.download_button(label="DESCARGAR RECORTABLE",
#                     data=PDFbyte,
#                     file_name="RECORTABLE_LURA_IEO.pdf",
#                     mime='application/octet-stream')



# # FOTOS GUIA
# titulo_fotos = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Aquí tienes unas fotos del barco terminado, para que te ayuden en el montaje.</p>'
# st.markdown(titulo_fotos, unsafe_allow_html=True)


# # Despliega la extensión para subir los archivos .btl y .cnv
# col1, col2 = st.columns(2,gap="small")

# with col1:
#     imagen_pagina = Image.open(foto_base) 
#     st.image(imagen_pagina)   
#     st.caption('Piezas 1,2 y 3 montadas')
    
#     imagen_pagina = Image.open(foto_cabina) 
#     st.image(imagen_pagina)   
#     st.caption('Cabina y tejado montados')    
    
# with col2:
#     imagen_pagina = Image.open(foto_laterales) 
#     st.image(imagen_pagina)   
#     st.caption('Añadidos los laterales y la cubierta')
    
#     imagen_pagina = Image.open(foto_final) 
#     st.image(imagen_pagina)   
#     st.caption('Terminado y listo para navegar!')    
 

