import streamlit as st
import pandas as pd
import joblib


# Load model
prophet_model = joblib.load('prophet_model.joblib')

# Prediction Function
def predict_future_month(prophet_model, input_month):
    future_month_df = pd.DataFrame({'ds': [input_month]})
    future_month_forecast = prophet_model.predict(future_month_df)
    predicted_value = future_month_forecast['yhat'].values[0]
    return predicted_value

month_map = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

st.title('Future Total Receipt Prediction')

# Inputs

input_year = st.selectbox("Select a year", options=[2021,2022,2023], index=1)  
input_month_name = st.selectbox("Select a month", options=["January", "February", "March", "April", "May", "June",
                                                           "July", "August", "September", "October", "November", "December"],
                                                           index=0)  

if st.button("Submit"):
    if input_month_name in month_map:  
        input_month = month_map[input_month_name]  
        
        # Use the Prophet model to make predictions for the input month
        future_month_df = pd.DataFrame({'ds': [pd.to_datetime(f"{input_year}-{input_month:02}")]})
        future_month_forecast = prophet_model.predict(future_month_df)
        
        # Extract predicted value, upper, and lower confidence intervals 
        predicted_value = future_month_forecast['yhat'].values[0]
        upper_confidence = future_month_forecast['yhat_upper'].values[0]
        lower_confidence = future_month_forecast['yhat_lower'].values[0]
        
        # Round the values to the nearest tenths
        rounded_predicted_value = round(predicted_value, 0)
        rounded_upper_confidence = round(upper_confidence, 0)
        rounded_lower_confidence = round(lower_confidence, 0)
        
        # Display the prediction in a table
        result_data = {
            "Month": input_month_name,
            "Year": str(input_year),
            "Predicted Values": [rounded_predicted_value],
            "Upper Confidence Interval": [rounded_upper_confidence],
            "Lower Confidence Interval": [rounded_lower_confidence]
        }
        result_df = pd.DataFrame(result_data)
        st.write(result_df)
        
        
    else:
        st.error("Invalid selection. Please choose a valid month.")


