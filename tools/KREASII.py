# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and Introduction
st.title("Analisis Data Gender dan Divisi Magang CEO HMSD 2024")
st.write("""
Artikel dalam kreasi ini menyajikan analisis data peserta magang CEO HMSD 2024, khususnya mengenai distribusi gender dan keterlibatan
dalam divisi-divisi yang ada. Melalui analisis ini, kita akan melihat bagaimana proporsi laki-laki dan perempuan di setiap divisi,
serta menganalisis beberapa statistik deskriptif terkait distribusi ini.
""")

# Load Data
@st.cache
def load_data():
    # Replace this path with the path to your data file
    data_path = r"dataset/Pendataan_Peserta_Magang_CEO_HMSD_2024.xlsx"
    data = pd.read_excel(data_path)
    data.columns = data.columns.str.strip()  # Clean column names
    return data

data = load_data()

# Display Data Preview
st.subheader("Data Peserta Magang")
st.write("Berikut adalah sekilas data yang digunakan untuk analisis:")
st.dataframe(data[['Divisi', 'Gender']].head())

# Gender Distribution and Descriptive Statistics
st.subheader("Statistik Deskriptif Gender dan Divisi Magang")
st.write("""
Berikut ini adalah tabel yang menunjukkan jumlah peserta laki-laki dan perempuan di setiap divisi, 
beserta beberapa statistik deskriptif seperti rata-rata dan deviasi standar.
""")

# Descriptive Statistics for Gender and Divisi
data_divisi_gender = data[['Divisi', 'Gender']].value_counts().unstack().fillna(0)
gender_stats = data_divisi_gender.describe()

# Displaying descriptive statistics table
st.write("Tabel Statistik Deskriptif:")
st.table(gender_stats)

# Explanation for Descriptive Statistics
st.write("""
Tabel statistik deskriptif di atas memberikan gambaran umum mengenai distribusi gender di setiap divisi. 
Rata-rata jumlah peserta per gender di setiap divisi membantu kita memahami bagaimana persebaran gender.
""")

# Plotting the Divisi and Gender distribution
st.subheader("Distribusi Gender Berdasarkan Divisi")
st.write("""
Grafik berikut menampilkan distribusi jumlah peserta laki-laki dan perempuan pada masing-masing divisi. Grafik ini 
membantu kita memahami keterlibatan gender di tiap divisi dan melihat apakah ada dominasi tertentu dari sisi gender.
""")

fig, ax = plt.subplots(figsize=(8, 6))
data_divisi_gender.plot(kind='bar', stacked=True, ax=ax, color=["#3498db", "#e74c3c"])
plt.title("Distribusi Peserta Berdasarkan Divisi dan Gender")
plt.xlabel("Divisi")
plt.ylabel("Jumlah Peserta")
plt.legend(["Laki-laki", "Perempuan"], title="Gender")
st.pyplot(fig)

# Insight: Gender Percentage in Each Division
st.subheader("Persentase Gender di Setiap Divisi")
st.write("""
Selain melihat jumlah absolut, kita juga dapat menganalisis persentase peserta laki-laki dan perempuan di setiap divisi.
Grafik ini menunjukkan perbandingan proporsi gender dalam setiap divisi, memberikan gambaran yang lebih jelas mengenai keterwakilan gender.
""")

gender_percentage = data_divisi_gender.div(data_divisi_gender.sum(axis=1), axis=0) * 100

# Plotting Gender Percentage in Each Division
fig, ax = plt.subplots(figsize=(8, 6))
gender_percentage.plot(kind='bar', stacked=True, ax=ax, color=["#3498db", "#e74c3c"])
plt.title("Persentase Gender Berdasarkan Divisi")
plt.xlabel("Divisi")
plt.ylabel("Persentase (%)")
plt.legend(["Laki-laki", "Perempuan"], title="Gender")
st.pyplot(fig)

# Explanation for Percentage Plot
st.write("""
Grafik persentase di atas membantu kita melihat proporsi gender dalam setiap divisi. Kita bisa melihat apakah ada divisi tertentu yang 
memiliki keseimbangan gender atau lebih didominasi oleh salah satu gender.
""")

# Kesimpulan
st.subheader("Kesimpulan")
st.write("""
Distribusi gender di setiap divisi cukup beragam. Dengan analisis ini, kita dapat lebih memahami keterlibatan gender 
dan melakukan evaluasi untuk mencapai keikutsertaan yang lebih merata di masa mendatang.
""")
