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
            "https://drive.google.com/uc?export=view&id=1kz-DrVSKJyUJyY64Obi_y2oENNMmdHH9",
            "https://drive.google.com/uc?export=view&id=1yLmRp0jXB0wRTko826XopADkaejnPX9W",
            "https://drive.google.com/uc?export=view&id=186iG-T-ckyJ4XJc7BwLEYuEtbOSd9bH_",
            "https://drive.google.com/uc?export=view&id=1cv--fLgVgls9unJc78WmP_HgjIO7KOYM",
            "https://drive.google.com/uc?export=view&id=19CUgiUg3jt0PQ8NYNDF1R-UNWWipHZo1",
            "https://drive.google.com/uc?export=view&id=1ynkGmRpSDKXQuA75eDzOoQtDHuIZAlu8",
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
                "kesan": "Baik, Keren banget",  
                "pesan":"semangat menjalani hari-hari sebagai kahim bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Asik banget abangnya",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "kakaknya imut banget",  
                "pesan":"semangat menjalani hari-hari sebagai sekretaris umum himpuanan kak"# 1
            },
            {
                "nama": "Hartiti Fadhilaj",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kaaknya baik dan asik ",  
                "pesan":"semangat menjalani hari-hari sebagai bendahara umum himpuanan kak"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakaknya baik banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "kakaknya keren bangett",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1r5Pr5MOWBl1QGbT0FI1_dffZlPB9jb8-",
            "https://drive.google.com/uc?export=view&id=1575tz9JYOkLufxhSVgXh6RhdyKO7hLXL",
            "https://drive.google.com/uc?export=view&id=1WPQDP2x9Id-Ozxrwgf_YV2_0NeNt4Qf4",
            "https://drive.google.com/uc?export=view&id=1RKwOsD6v21cd5qxnQaQ4asCZAzXWU9Ah",
            "https://drive.google.com/uc?export=view&id=1wH5Urtfro4JWx4CMEEcpXHtPTnegSlzw",
            "https://drive.google.com/uc?export=view&id=1zHLSAsph8eOMXdbyp04kQDv--GUUcgR5",
            "https://drive.google.com/uc?export=view&id=1R-EdjpohuRstWF0xERHBQjJAXQy_8gJu",
            "https://drive.google.com/uc?export=view&id=1jY3oVcLc1UKZlHoSq7mBhn7prZ35IIyT",
            "https://drive.google.com/uc?export=view&id=1YAyY9VeA236ggGcAZI7wEi3ofOAXG6YW",
            "https://drive.google.com/uc?export=view&id=1y119uDgqm4banVxnuBs1BZT4Jl6TZU5l",
            "https://drive.google.com/uc?export=view&id=1CWfLDK9i9P4nTcBciUh5rTRiA79E5_8n",
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
                "kesan": "suka banget sama public speaking kakaknya",  
                "pesan":"sukses terus kak!!"
            },
            {
                "nama": "Claudea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "cntikk banget kakaknya",  
                "pesan":"semangat kak"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "baik banget",  
                "pesan":"sukses terus kak"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "suka bercanda",  
                "pesan":"stay humble bang"# 1
            },
            {
                "nama": "Ferdiadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya baik terus friendly abis",  
                "pesan":"semangat terus bang"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "keren tapi keliatannya kaya introvert",  
                "pesan":"semangat terus kuliahnya bang!!"# 1
            },
            {
                "nama": "Muhammad Faru Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "keren banget",  
                "pesan":"ssukses terus bang"# 1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "cantik",  
                "pesan":"semangat terus kuliahnya kakak!!"# 1
            },
            {
                "nama": "Berliana Inda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "lucu dan seru",  
                "pesan":"semangat kak"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "baik banget",  
                "pesan":"semangat kak kuliahnya"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Belajar, nonton film, tidur",
                "sosmed": "@wlsbn0",
                "kesan": "keren banget bisa msib di telkom",  
                "pesan":"sukses terus kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
