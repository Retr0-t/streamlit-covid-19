import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("COVID-19 Data Analysis and Visualization")

# Path ke file dataset
file_path = r"C:\Users\hrand\Downloads\sem7\Visdat\covid_19_clean_complete.csv"

# Membaca dataset dari file yang ada di direktori lokal
try:
    data = pd.read_csv(file_path)
    st.write("Dataset COVID-19:")
    st.write(data.head())
    
    # Mengambil beberapa kolom untuk analisis lebih lanjut
    if 'date' in data.columns and 'total_cases' in data.columns and 'total_deaths' in data.columns:
        st.write("Menampilkan Grafik Kasus dan Kematian Total:")
        
        # Mengubah kolom 'date' ke tipe datetime
        data['date'] = pd.to_datetime(data['date'])
        
        # Membuat grafik total kasus dan total kematian
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(data['date'], data['total_cases'], label="Total Kasus")
        ax.plot(data['date'], data['total_deaths'], label="Total Kematian", linestyle='--')
        ax.set_title('Tren Kasus dan Kematian COVID-19')
        ax.set_xlabel('Tanggal')
        ax.set_ylabel('Jumlah')
        ax.legend()
        
        st.pyplot(fig)
        
    else:
        st.warning("Data tidak lengkap. Pastikan dataset memiliki kolom 'date', 'total_cases', dan 'total_deaths'.")
except FileNotFoundError:
    st.error(f"File tidak ditemukan di path: {file_path}")
