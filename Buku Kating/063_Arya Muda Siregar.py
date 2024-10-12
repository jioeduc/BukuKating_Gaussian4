import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GpC18GIU8uPvK9U2yW_BLyi4QnANeFKW",
            "https://drive.google.com/uc?export=view&id=1Gml4TQwChcrSQl62ZBdnPu9qGKzy1UL4",
            "https://drive.google.com/uc?export=view&id=1Gkr0FL2xGV4lIbWVllQoTZGC7syJDGvw",
            "https://drive.google.com/uc?export=view&id=1GqRDrLoSDrnMxUwNRDVN6fQZ_V57pl8j",
            "https://drive.google.com/uc?export=view&id=1GgnJ3Ok8nxRjaSoOJ4pOuRjf6JrEQHYR",
            "https://drive.google.com/uc?export=view&id=1GiWBNX-NFSZ9BEC4p05PkL_i3ObA4grL",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Dengerin musik",
                "sosmed": "@amsirahk",
                "kesan": "Kakak ini asik dan santai",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Kakak ini asik dan seru",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kaka ini memotivasi",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Hartiti Fadhilaj",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kaka ini ramah",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini menginspirasi",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "kakak ini ramah dan inspiratif",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HJ-Qh2nevxnHrW1dix-FC5xxDsmYahVQ",
            "https://drive.google.com/uc?export=view&id=1HsTBX2rXmbxTh5i8SrpC_VlYngeBYNKo",
            "https://drive.google.com/uc?export=view&id=1IZpWkd3zLa0PPUINg9E1FGe5uSqq4Gog",
            "https://drive.google.com/uc?export=view&id=1I6H1gYP5mvHQTmF4p39aoDoXY5YVVDwO",
            "https://drive.google.com/uc?export=view&id=1I4Bl1jtFFq_3uNL7nXin2DDN_PK5Y-Cd",
            "https://drive.google.com/uc?export=view&id=1Gz8wNyEnR5tjfxvDtouZj7ARIpnqhptc",
            "https://drive.google.com/uc?export=view&id=1HkNDNH_ynQiLIcsAYg-s0GpFQtdAldVP",
            "https://drive.google.com/uc?export=view&id=1IgBDSi7z2-NSRtuGK5XPE0F7Stc2vg9d",
            "https://drive.google.com/uc?export=view&id=1HzJIHinsazeEhEBEdyDtiBdwc6kMDxy7",
            "https://drive.google.com/uc?export=view&id=1HmQu9aSDsw-MU7RkFmnBPIBV6D4C0Oxm",
        ]
        data_list = [
            {
                "nama": "Tri Murnia Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Searching di perplexity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak ini baik dan asik",  
                "pesan":"Terima kasih atas segala saran dan arahannya."
            },
            {
                "nama": "Claudea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini ramah dan baik",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "Jeremia Susanto",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini penuh inspiratif",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak ini asik dan santai",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Ferdiadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini penuh inspiratif dan santai",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini santai dan asik",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Muhammad Farul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak ini inspiratif",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini ramah",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Berliana Inda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini penuh motivasi",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini penuh inspirasi",  
                "pesan":"Terima kasih atas segala saran dan arahannya."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
