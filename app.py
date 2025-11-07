import streamlit as st
import numpy as np
import pandas as pd
import joblib
import requests
import os
import gdown

file_id = '1AxdMNf_CP0j9L3l7tkP4i8a01WlRgczB'
output_file = 'USA_House_Price_Prediction_model.pkl'

download_url = f'https://drive.google.com/uc?id={file_id}'

if not os.path.exists(output_file):
    st.info('Downloading model from Google Drive...')
    gdown.download(download_url, output_file, quiet=False)

model = joblib.load(output_file)

st.title('USA House Price Prediction Model')
st.divider()
st.write('Please enter House details in Numeric Format')
st.divider()
floor=st.number_input('Select floors',min_value=0,value=0)
waterfront=st.number_input('Select waterfront',min_value=0,value=0)
bedrooms=st.number_input('Select Number of bedrooms',min_value=0,value=0)
sqft_basement=st.number_input('Enter Square footage of the basement',min_value=0,value=0)
lat=st.number_input('Select lat',min_value=0,value=0)
view=st.number_input('Select Has been viewed',min_value=0,value=0)
bathrooms=st.number_input('Select Number of bathrooms',min_value=0,value=0)
sqft_living15=st.number_input('Enter Living room area in 2015(implies-- some renovations) This might or might not have affected the lotsize area',min_value=0,value=0)
sqft_above=st.number_input('Enter Square footage of house apart from basement',min_value=0,value=0)
grade=st.number_input('Select overall grade given to the housing unit, based on USA grading system',min_value=0,value=0)
sqft_living=st.number_input('Enter Square footage of the home',min_value=0,value=0)
st.divider()
x=[bedrooms,bathrooms,sqft_living,sqft_above,sqft_basement,lat,waterfront,view,grade,sqft_living15,floor]
predictbutton=st.button('Predict')

if predictbutton:
    x_array = np.array(x).reshape(1, -1)  # Reshape to 2D array
    prediction = model.predict(x_array)
    st.write(f'Predicted House Price: ${prediction[0]:,.2f}')
else:
    st.write('Please click predict button after entering all values')
