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
            "https://drive.google.com/uc?export=view&id=1OhO3J-9LHBsCiQlKgoyJxdpAuPXjRZo4",
            "https://drive.google.com/uc?export=view&id=1OeH3v1Uu3ou8zvGV-SmWQfScKBsnT7Xf",
            "https://drive.google.com/uc?export=view&id=1OjjvP3ifZuOdAl8H9ERlhLW0qHsYnkWl",
            "https://drive.google.com/uc?export=view&id=1OxoLjwT7znlimme11v3zb_X-n89bQVh_",
            "https://drive.google.com/uc?export=view&id=1OjA9sKz2K1Ix8hCvOuyemenUtCeD2R4sP",
            "https://drive.google.com/uc?export=view&id=1Oztv6IbrUZaA5QXGuqhHvNtd0Lm2LErD",
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
                "kesan": "abang ini sangat memotivasi saya!",  
                "pesan":"Tetap semangat menjalani hidup"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abang ini sangat tau trend tik tok",  
                "pesan":"Tetap ceria dan seru bang, jangan berubah"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakak sangat lucu kiyowo dan baik",  
                "pesan":"Semangat urus surat - suratnya kak, dan semangat belajar nya"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak hartiti agak pendiam tapi best",  
                "pesan":"Jangan menyerah untuk menagih uang kas"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak putri lumayan pendiam dan lucu",  
                "pesan":"Tetap semangat menjalani hidup"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "Kakak nadilla lucu dan seru banget",  
                "pesan":"Tetap semangat untuk hidup lebih baik"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VLEUP3SNpLStSxZGLuoI1RvPzmH80W1k",
            "https://drive.google.com/uc?export=view&id=1UeXmcBIg-nL938IFIw20B20UxZAA0Wfz",
            "https://drive.google.com/uc?export=view&id=1UnDi2sFYQibbkpMZDHUHCZAP8wviZpc9",
            "https://drive.google.com/uc?export=view&id=1UeXmcBIg-nL938IFIw20B20UxZAA0Wfz",
            "https://drive.google.com/uc?export=view&id=1UZkZyw88BrE7nNovaWG4e19_6nNQAHK0",
            "https://drive.google.com/uc?export=view&id=1VJAI1GQeEuwMDXagns6uoY6ic7ETEtSd",
            "https://drive.google.com/uc?export=view&id=1UdMO3bzCSxzObCELbjXoNegG6449UwRY",
            "https://drive.google.com/uc?export=view&id=1Us4VBWB1nf9glpXVbmRu2rL35At6aIhj",
            "https://drive.google.com/uc?export=view&id=1UdMO3bzCSxzObCELbjXoNegG6449UwRY",
            "https://drive.google.com/uc?export=view&id=1VXAkQfuQSrx3a0luWVHoZeRuNViowbuh",
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
                "kesan": "Kakak ini cantik sekali, lucu dan mood banget",  
                "pesan":"semangat kak, jangan luntur ceria nya"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "kakak ini cantik sekali, dan super lembut",  
                "pesan":"semangat ngejar cita - citanya kak"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak dhea kelihatan aura anak pinter nya",  
                "pesan":"semangat kak buat belajarnya"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jeremy asik dan suka bercanda",  
                "pesan":"semangat bang ngejar cita - cita nya"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya sangat responsif dan lucu",  
                "pesan":"semangat bang untuk ngejalanin hidup"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini sangat kalem dan sepertinya menyukai anime",  
                "pesan":"semangat bang ngejar cita - citanya"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Bang fahrul agak pendiem cuma keliatannya asik",  
                "pesan":"semangat bang untuk ngejalanin kehidupan"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kak annisa cahyani ini super asik dan lucu",  
                "pesan":"semangat jangan menyerah dan terus berjuang!"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "kakak berlin sangat cantik dan responsif",  
                "pesan":"semangat kak ngejar cita - cita nya"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kak anisa dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
