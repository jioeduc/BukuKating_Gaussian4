import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#FDFFE2",
            },
            "nav-link-selected": {"background-color": "#83B4FF"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Kelompok kami memilih nama Gaussian yang diambil dari perangkat lunak kimia komputasi yang dibuat oleh Sir John A. Pople, 
            serta dari penggunaan orbital Gaussian sebagai basis perhitungan. Gaussian Distribution, konsep statistik yang penting, menjadi dasar bagi para Data Analyst. 
            Nama ini dipilih untuk memotivasi anggota kelompok agar mendalami distribusi Gaussian, memperkaya keterampilan, dan meningkatkan kualitas sebagai Data Analyst di masa depan.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=10u1MqDbyUUgbYnIB5T82VI_9WbnDA1XG"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Kelompok kami memilih nama Gaussian yang diambil dari perangkat lunak kimia komputasi yang dibuat oleh Sir John A. Pople, 
            serta dari penggunaan orbital Gaussian sebagai basis perhitungan. Gaussian Distribution, konsep statistik yang penting, menjadi dasar bagi para Data Analyst. 
            Nama ini dipilih untuk memotivasi anggota kelompok agar mendalami distribusi Gaussian, memperkaya keterampilan, dan meningkatkan kualitas sebagai Data Analyst di masa depan.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1paZWnSpICzOJGlVPsu19Hi_k_FTHanO5",
            "https://drive.google.com/uc?export=view&id=1oG4GBAQoowRpnY3K2vL_TBDDJbChGdyg",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Fd6MLsRFAEuRldHBeiuhgt3oj85qNh1q",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1mFjQ2PaaTEwTwFQIgfe6mBMoBrOfflbC",
            "https://drive.google.com/uc?export=view&id=1fcnxJJYyNo6TCm07e31kTH0swgoWT1QQ",
            "https://drive.google.com/uc?export=view&id=1VhC_WL_PMJsJ92_HDe0Urlj2UNxSjJoO",
            "https://drive.google.com/uc?export=view&id=1S1_KVbHA1S_dX4t82rwQ2yyxXUoDb0e0",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Arya Muda Siregar",
                "sebagai": "Pak Lurah",
                "nim": "123450063",
                "fun_fact": "cita cita pengen terbang",
                "motto_hidup": "jangan panik",
            },
            {
                "nama": "Fathinah Nur Azizah",
                "sebagai": "Bu Lurah",
                "nim": "123450072",
                "fun_fact": "aku carat",
                "motto_hidup": "Alhamdulillah masih hidup",
            },
            {
                "nama": "Afifah Fauziah",
                "sebagai": "Anggota",
                "nim": "123450002",
                "fun_fact": "suka cowo 2D",
                "motto_hidup": "kalo error tinggal trial lagi aja",
            },
            {
                "nama": "D",
                "sebagai": "Anggota",
                "nim": "122450000",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "jalanin dulu aja",
            },
            {
                "nama": "E",
                "sebagai": "Anggota",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
             {
                "nama": "E",
                "sebagai": "Anggota",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
             {
                "nama": "E",
                "sebagai": "Anggota",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
             {
                "nama": "E",
                "sebagai": "Anggota",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
             {
                "nama": "Giofani Aristyo",
                "sebagai": "Anggota",
                "nim": "123450065",
                "fun_fact": "ga suka manis",
                "motto_hidup": "gali ilmu sebanyak-banyaknya",
            },
             {
                "nama": "iqfina Haula Halika",
                "sebagai": "Anggota",
                "nim": "123450076",
                "fun_fact": "ga suka hewan berbulu",
                "motto_hidup": "seberat apapun hidupmu, tetaplah hidup",
            },
             {
                "nama": "Ali Aristo Muthahhari Parisi",
                "sebagai": "Anggota",
                "nim": "123450088",
                "fun_fact": "tim bubur gk diaduk",
                "motto_hidup": "Kalo rencana A gagal, santai masih ada sisa 25 huruf lagi",
            },
             {
                "nama": "Arienta Khusnul Ananda",
                "sebagai": "Anggota",
                "nim": "123450097",
                "fun_fact": "ga bisa makan telur",
                "motto_hidup": "jalanin aja dulu",
            },
             {
                "nama": "E",
                "sebagai": "Anggota",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
