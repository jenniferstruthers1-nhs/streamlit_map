# This is a very very simple map - it shows dots of varying sizes of a map.
# They are placed using a lat and lon. You can't hover to get more info.
# To do that we will need a better package
import streamlit as st
import pandas as pd

st.set_page_config(page_title="England City Map", layout="centered")

st.title("📍 England City Map")

# 1. Our Data
data = {
    'city': ['London', 'Manchester', 'Birmingham', 'Leeds', 'Newcastle', 'Bristol'],
    'lat': [51.5074, 53.4808, 52.4862, 53.8008, 54.9783, 51.4545],
    'lon': [-0.1278, -2.2426, -1.8904, -1.5491, -1.6178, -2.5879],
    'population_size': [10000, 600, 550, 400, 300, 350]
}
df = pd.DataFrame(data)

# 2. The Updated Streamlit Map
# Using width='stretch' to fill the container 
st.map(
    df,
    latitude='lat',
    longitude='lon',
    size='population_size',
    color='#FF4B4B',
    width='stretch' 
)