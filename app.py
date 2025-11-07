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
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df=pd.read_csv(url)
floors=sorted(df['floors'].unique().tolist())
waterfront=df['waterfront'].unique()
bedrooms=sorted(df['bedrooms'].dropna().unique().tolist())
view=sorted(df['view'].unique().tolist())
bathrooms=sorted(df['bathrooms'].unique().tolist())
grade=sorted(df['grade'].unique().tolist())
st.title('USA House Price Prediction Model')
st.divider()
st.write('Please enter House details in Numeric Format')
st.divider()
floor=st.selectbox('Select Number of floors',[0]+floors)
waterfront=st.selectbox('Select waterfront(if yes then select 1 if No then select 0)',waterfront)
bedrooms=st.selectbox('Select Number of bedrooms',bedrooms)
sqft_basement=st.number_input('Enter Square footage of the basement',min_value=0,value=0)
lat=st.number_input('Enter Latitude of Home Location',min_value=0,value=0)
view=st.selectbox('Select Has been viewed',view)
bathrooms=st.selectbox('Select Number of bathrooms',bathrooms)
sqft_living15=st.number_input('Enter Living room area in 2015(implies-- some renovations) This might or might not have affected the lotsize area',min_value=0,value=0)
sqft_above=st.number_input('Enter Square footage of house apart from basement',min_value=0,value=0)
grade=st.selectbox('Select overall grade given to the housing unit, based on USA grading system',grade)
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
