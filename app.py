from cProfile import label
from math import pi
import streamlit as st
import requests
import datetime
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

''')

form = st.form(key='yeah')

date = form.text_input("Insert date")
time = form.text_input("Insert time")

pickup_longitude = form.text_input('Insert pickup_longitude')
pickup_latitude = form.text_input('Insert pickup_latitude')
dropoff_longitude = form.text_input('Insert dropoff_longitude')
dropoff_latitude = form.text_input('Insert dropoff_latitude')
passenger_count = form.text_input('Insert passenger_count')

combine = date + ' ' + time

params = {
    "pickup_datetime": combine,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

url = 'https://taxifare.lewagon.ai/predict'

submitted = form.form_submit_button(label="Submit")



df = pd.DataFrame([[float(pickup_latitude), float(pickup_longitude), float(dropoff_latitude), float(dropoff_longitude)]], columns=["lat", "lon", "lat_2", "lon_2"])

if submitted:
    request = requests.get(url, params=params).json()
    fare = request['fare']
    st.success(f"This is your fare amount: {fare}")
    st.map(df)




'''

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
