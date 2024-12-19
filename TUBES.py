import streamlit as st
import pandas as pd

# URL raw dataset di GitHub
url = "https://raw.githubusercontent.com/Retr0-t/streamlit-covid-19/main/covid_19_clean_complete.csv"

# Membaca dataset dari URL
data = pd.read_csv(url)

# Menampilkan dataset
st.write("Dataset COVID-19:")
st.write(data.head())
