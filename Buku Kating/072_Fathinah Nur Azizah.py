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
            "https://drive.google.com/uc?export=view&id=1yMLx11UAxx27_x75XPe4gAibWXdH0794",
            "https://drive.google.com/uc?export=view&id=1yMCQ2fbkKt_zR4XIhACwCexAw6H5rA2i",
            "https://drive.google.com/uc?export=view&id=1yLbraM-Bxij8JsfA7YWS7Fgp7QtGKQO5",
            "https://drive.google.com/uc?export=view&id=1yWZ1qaB16uOCuMOGOYinkm2VnfTsLEQp",
            "https://drive.google.com/uc?export=view&id=1yKoYwdq5mqIz5dAu79uJ-mjefWJAV3vt",
            "https://drive.google.com/uc?export=view&id=1yU4eExgpi5q4Ioa4gC4gwb-8NsorpVfa",
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
                "kesan": "Abangnya inspiratif",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abangnya unik dan ngasih pandangan berbeda buat saya, gokil",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakaknya imut banget?! Makasih snacknya kak :)",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kak Titi adalah definisi cewek kalem",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini padang abis",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "kakak imut banget?!",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12BDuruq1tkSrnzEbd2s8dbCxD0xbFQTA",
            "https://drive.google.com/uc?export=view&id=10xyNNUkNYKAIHXQnQHwYOrGKeI4qFsYj",
            "https://drive.google.com/uc?export=view&id=1pWTVBjk7Inaig08twQCIg_xDG4Qg-zs2",
            "https://drive.google.com/uc?export=view&id=1jkoqot8gpPZ4I2WoL5n-nnfRk_xGJ_DL",
            "https://drive.google.com/uc?export=view&id=1aIi0Flb1TQKMQokz4gvcdpTmorxvHj1b",
            "https://drive.google.com/uc?export=view&id=1j7nxSMJS_g9T8if97b_RbYXeVmUp0taT",
            "https://drive.google.com/uc?export=view&id=1cgwTtmOYlEsQpegKVXmS-nAZC7WVEMmv",
            "https://drive.google.com/uc?export=view&id=14wwuSZ4wMGihPNq8HRAo1wJ2ONdD8zwz",
            "https://drive.google.com/uc?export=view&id=1qD_KPxnKw7lT6iAcNS0CkvUQzF-8XhcU",
            "https://drive.google.com/uc?export=view&id=1fbp2s1xQeUnNWJni14iEQuNAvvHZDuZd",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Searching di perplexity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kak, kakak tuh ramah banget tau gak???",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kak Claud adalah definisi cewek aestehetic pinterest",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak aesthetic bgt vibesnya?",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini asik dan seru diajak ngobrol",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya ramah banget?!",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "bang Mirzan kalem sekali",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kece bgt",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak aesthetic bgt vibesnya?",  
                "pesan":"Kakak aesthetic bgt vibesnya?"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ramah banget sih :D",  
                "pesan":"Kakak aesthetic bgt vibesnya?"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Yeay, ketemu Carat",  
                "pesan":"Kakak aesthetic bgt vibesnya?"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Pmh42DTOiF3Nz89OfGdL6xEGEq0xvvmN",
            "https://drive.google.com/uc?export=view&id=1dQCUf5CDyjjqrFBJBfr_gRRoxRuT0mak",
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi",
                "nim": "121450093",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahyu",
                "hobbi": "Bernyanyi",
                "sosmed": "@anissaluthfia_",
                "kesan": "Abangnya inspiratif",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Ryan Bintang Wijaya ",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "Percaya gak percaya, Bang Bintang super supportif orangnya",  
                "pesan":"Tetep jadi orang baik bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

# Tambahkan menu lainnya sesuai kebutuhan
