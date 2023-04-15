import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
import pickle
import plotly.express as px


# Load Model 
with open('model_arima.pkl', 'rb') as file_1:
  model_arima = pickle.load(file_1)



def run():
    with st.form(key='Customer Data Input'):
        # define the user inputs
        week = st.number_input('No of Week to Predict', min_value=1, max_value=100, step=1)

        submitted = st.form_submit_button('Predict')

    if submitted:
        result = model_arima.forecast(12+week).tail(week)
        data = {'date': result.index,
                'predicted_product_sold': result
        }

        # Convert 'date' column to Pandas DatetimeIndex
        data['predicted_product_sold'] = data['predicted_product_sold'].round(2)
        data_inf = pd.DataFrame(data).reset_index()
        st.dataframe(data_inf)

        fig = px.line(data_inf, x='date', y='predicted_product_sold')
        fig.update_layout(title='Predicted Sold Products', xaxis_title='Date', yaxis_title='Sales Difference', 
                          hovermode='x unified', hoverlabel=dict(bgcolor="white", font_size=16, font_family="Courier New"))
        st.plotly_chart(fig)       


# calling function
if __name__ == '__main__':
   run()
