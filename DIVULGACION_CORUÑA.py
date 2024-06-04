# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2023

@author: ifraga
"""

import streamlit as st
from PIL import Image

logo_IEO_principal   = 'DATOS/IMAGENES/LOGOS.jpg' 
logo_centro_coruna   = 'DATOS/IMAGENES/logo_IEO_Coru.jpg' 

foto_Lura_1          = 'DATOS/IMAGENES/LURA.jpg'
foto_roseta          = 'DATOS/IMAGENES/roseta.jpg'
foto_red_plancton    = 'DATOS/IMAGENES/red_plancton.PNG'

logo_IEO_reducido    = 'DATOS/IMAGENES/ieo.ico'
foto_1               = 'DATOS/IMAGENES/ieo.jpg'    




imagen_logo   = Image.open(logo_IEO_reducido)
st.set_page_config(page_title="DIVULGACION IEO-CORUÑA",page_icon=logo_IEO_reducido)  # , layout="wide"

logo_cabecera = Image.open(logo_IEO_principal) 
st.image(logo_cabecera)


# Texto
texto = 'Bienvenid@ a la web de divulgación del Centro Oceanográfico de A Coruña'
titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

# Texto
texto = 'En esta web encontrarás material de divulgación que elaboramos los científicos del Centro Oceanográfico de A Coruña. Explora las pestañas laterales para encontrar diferentes actividades a través de las cuales conocer la labor que hace el Instituto Español de Oceanografía.'
titulo_principal = '<p style="text-align:  justify;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)




