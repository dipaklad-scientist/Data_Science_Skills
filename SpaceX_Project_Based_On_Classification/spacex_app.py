import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('SpaceX_Project_Based_On_Classification/SpaceX_Classification_Model.pkl')
scaler = joblib.load('SpaceX_Project_Based_On_Classification/scaler.pkl')

# Load original dataset for dropdown options
df = pd.read_csv('SpaceX_Project_Based_On_Classification/spacex_launch_data.csv')  # Replace with your actual file

# Dropdown options
Orbit_key = df['Orbit'].unique().tolist()
LaunchSite_key = df['LaunchSite'].unique().tolist()
Flights_key = sorted(df['Flights'].unique().tolist())
LandingPad_key = df['LandingPad'].unique().tolist()
Block_key = sorted(df['Block'].unique().tolist())

# Streamlit UI
st.title('SpaceX Falcon9 First Stage Landing Prediction')
st.divider()

FlightNumber = st.number_input('Enter Flight Number', min_value=0, value=0)
PayloadMass = st.number_input('Enter Payload Mass in KG', min_value=0, value=0)
Orbit = st.selectbox('Select Orbit', Orbit_key)
LaunchSite = st.selectbox('Select LaunchSite', LaunchSite_key)
Flights = st.selectbox('Select Number of Flights', Flights_key)
GridFins = st.selectbox('Select GridFins (True/False)', ['True', 'False'])
Reused = st.selectbox('Select Reused (True/False)', ['True', 'False'])
Legs = st.selectbox('Select Legs (True/False)', ['True', 'False'])
LandingPad = st.selectbox('Select LandingPad', LandingPad_key)
Block = st.selectbox('Select Block', Block_key)
ReusedCount = st.number_input('Enter Count of Reused', min_value=0, value=0)
Serial = st.text_input('Enter Serial (e.g., B1049)', value='B1049')

st.divider()
predictbutton = st.button('Predict')

if predictbutton:
    # Create raw input DataFrame
    raw_input = pd.DataFrame([{
        'FlightNumber': FlightNumber,
        'PayloadMass': PayloadMass,
        'Orbit': Orbit,
        'LaunchSite': LaunchSite,
        'Flights': Flights,
        'GridFins': GridFins,
        'Reused': Reused,
        'Legs': Legs,
        'LandingPad': LandingPad,
        'Block': Block,
        'ReusedCount': ReusedCount,
        'Serial': Serial
    }])

    # Apply same preprocessing
    categorical_cols = ['Orbit', 'LaunchSite', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Serial']
    input_encoded = pd.get_dummies(raw_input, columns=categorical_cols, dtype=int)

    # Align columns with training set
    training_columns = joblib.load('SpaceX_Project_Based_On_Classification/training_columns.pkl')  # Save this during training
    input_encoded = input_encoded.reindex(columns=training_columns, fill_value=0)

    # Scale numeric features
    input_scaled = scaler.transform(input_encoded)

    # Predict
    prediction = model.predict(input_scaled)
    if prediction==1:
        st.success(f"Landing Outcome {prediction[0]}: ✅ Successful Landing")
    else:
        st.error(f"Landing Outcome {prediction[0]}: ❌ Landing Failure")
else:
    st.info('Please click predict button after entering all values')
