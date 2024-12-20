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
                "sosmed": "@gumilangkharisma",
                "kesan": "Abangnya inspiratif",  
                "pesan":"Semangat untuk mewujudkan komunitas SD se-Indonesia bang!"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr27",
                "kesan": "Abangnya unik dan ngasih pandangan berbeda buat saya, gokil",  
                "pesan":"Terus jadi diri sendiri bang"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakaknya imut banget?!",  
                "pesan":"Makasih buat snacknya kak, stay humble and happy :)"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kak Titi adalah definisi cewek kalem",  
                "pesan":"Stay calm and humble kak"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini padang abis!",  
                "pesan":"Tetap jadi orang yang baik"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@nadillaandr26",
                "kesan": "kakak imut banget?!",  
                "pesan":"Kak,foto kita lucu banget?! anw, menurut aku kakak mirip Bu Luluk"
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
                "pesan":"Aku suka duality kakak waktu kerja dan kalaulagi bercanda, profesional banget..."
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kak Claud cantik banget?!",  
                "pesan":"Menurut aku, Kak Claud ada sedikit vibes Nessie Judgenya?"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "kak Dhea super ramah dan positif",  
                "pesan":"Semangat jadi kakak mentor aku kak >-<"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Hobinya gokil",  
                "pesan":"Tetap jadi orang yg iseng bang karena bisa naikin suasana >-<"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Gak tau ya tapi mukanya Bang Ferdi tuh, familiar banget",  
                "pesan":"Semangat jadi abang mentorku bang >-<"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Bang Mirzan well-dressed abiss",  
                "pesan":"spill pin board ya bang"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Bang Fahrul baik banget orangnya",  
                "pesan":"stay positive bang"
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
                "pesan":"mau pin boardnya dong kakak >_<"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di draw.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kak Berlin vibenya kayak mengayomi banget",  
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
                "pesan":"stay hard for SVT kak!"
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
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahyu",
                "hobbi": "Bernyanyi",
                "sosmed": "@anissaluthfi_",
                "kesan": "Kak Lutfi keren abiss",  
                "pesan":"Mau denger suara Kak Lutfi"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Percaya gak percaya, Bang Bintang super supportif orangnya",  
                "pesan":"Tetep jadi orang baik bang >_<"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eIj4YpyzkJMDM6mprDnPVlLOFT0Rn2e-",
            "https://drive.google.com/uc?export=view&id=1f4lGwVQOnjSBdZlAaTmbHBvOwbIis9LS",
            "https://drive.google.com/uc?export=view&id=1O-i8bbjDHu9mBZpfKbxMfKEyZQJPhg6N",
            "https://drive.google.com/uc?export=view&id=1c578n_M7lJ-sVp91CiSC6czNMP9mZPAt",
            "https://drive.google.com/uc?export=view&id=1tipsBFEUqp709_S03xBwyFSK-QIvEPD3",
            "https://drive.google.com/uc?export=view&id=1HB1RnCY7kpswEk3xM1JHxeukqC49m3xx",
            "https://drive.google.com/uc?export=view&id=1ls2WidqO6b4ntvFPIuuraoOXC-eH8Ryd",
            "https://drive.google.com/uc?export=view&id=15nJk0IEw-36yLm8od9D0y05FN74Zr993",
            "https://drive.google.com/uc?export=view&id=1S7he1qaOzFrWCgJaS6Zlzh6GVyHZp3Hj",
            "https://drive.google.com/uc?export=view&id=1EMONicZuXhiztdTAjuzTDGia6KOV8Gbb",
            "https://drive.google.com/uc?export=view&id=1TvgjC7bVoKdlqG8W3GBzJpOGI_oozdE_",
            "https://drive.google.com/uc?export=view&id=1lGHLBi-E_PYr-hcD13INJkyeAl2dktF1",
            "https://drive.google.com/uc?export=view&id=1WS7mPjOkuYGVJls8GZPY_8a-cSQf2TFe",
            "https://drive.google.com/uc?export=view&id=1pVxPj205vZuAa-M6bC9sX1HwYeJR_Q0e",
            "https://drive.google.com/uc?export=view&id=1NXpEx7dNXpuZyr5qG_1plMAunPB4OQ7S",
            "https://drive.google.com/uc?export=view&id=1meT_uMSufHueiKPxAlMjPyRr-iAV-IXs",
            "https://drive.google.com/uc?export=view&id=15VO0QD4NLI4NDEYGeGfB9zs7tAGI2Aqm",
            "https://drive.google.com/uc?export=view&id=1-Zv0eos6jSlUdSoTZqZ9O6O6M-62qDBp",
            "https://drive.google.com/uc?export=view&id=1l44-e1Wyy6VqT3nrduUV8l0xJWrJLHzH",
            "https://drive.google.com/uc?export=view&id=1o327QNKgog1iN_TdVqMqfPVbcq0XEiQt",
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Bang Econ seru banget orangnya",  
                "pesan":"Tetap jadi pemateri dan sosok yang interaktif dan gak judgemental bang >_<"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Abeth ruamah poll",  
                "pesan":"Stay positive kak!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Afifah mirip sama temen aku...",  
                "pesan":"Aku suka kalau lagi ngobrol sama Kak Fifah"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami_",
                "kesan": "Jujur aku terharu sama salah satu kalimat kakak waktu lagi wawancara",  
                "pesan":"Tetap jadi sosok yang mencerminkan nama Allya Nurul Islami kak >_<"
            },
            {
                "nama": "Ekshanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kak Eksanty tinggi banget, diriku harus jinjit dulu walaupun akhirnya gak setinggi Ka Eksanty juga sih",  
                "pesan":"Tetap jadi orang baik dan ramah kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak Hanum vibenya jaksel banget, walaupun asal Padang",  
                "pesan":"Tetap jadi kakak yg peratian ya"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Bang Ferdy kece abis",  
                "pesan":"Maaf bang, kemarin waktu mau foto di rk bikin abang bingung"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "Bang Deri seru banget orangnya!",  
                "pesan":"Gas jadi asprak ADS bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kak Okta perhatian banget",  
                "pesan":"Tetap jadi kakak yang inisiatif dan perhatian kak <3"
            },
            { 
                "nama": " Deyvan Loxefal", 
                "nim": " 121450148 ", 
                "umur":  "21", 
                "asal":"Duri Riau", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanloo", 
                "kesan": "Bang Depan seru banget?!",   
                "pesan":"Semangat ngebasket dan kuliahnya bang" 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamg", 
                "kesan": "Kak Presilia cantik banget?!",   
                "pesan":"Semangat terus kuliahnya kak, jangan stress-stress ya:D" 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "Bang Jo ramah bgt orangnya ",   
                "pesan":"Semangat terus ngebasket, ngasprak, dan akademiknya bang" 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "Bang Kemas super penyabar",   
                "pesan":"Semangat terus ngasprak dan main valorantnya bang" 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Bang Maul ramah banget, serius",   
                "pesan":"Tetap jadi orang yang ramah ya bang..." 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Suka rambut Kak Rafa",   
                "pesan":"Tetap jadi orang ramah dan spreading positivity kak" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Bang Ateng seru banget diajak foto, salfok sama sendal hiunya hihi",  
                "pesan":"Stay humble bang"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "Ini juga, ramah banget abangnya ",  
                "pesan":"Semangat belajar dan ngegamenya bang"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "First impression aku yak, Kak Jaclin imut orangnya",  
                "pesan":"Semangat ngebimbing bocah-bocah Gauss kak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Bang Rafly pendiem kah?",  
                "pesan":"Bang jangan terlalu kaku..."
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakak cantik bgt kalau lagi ketawa",  
                "pesan":"Awalnya aku bingung, ternyata kakak ada kembaran juga di Sains Data 22 "
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YWJWLcOT5cW-fXb9JXOk1HM9Et7pF52M",
            "https://drive.google.com/uc?export=view&id=1Py4TFU49qlwCkbg5iPXgGjmRZv2P1rLm",
            "https://drive.google.com/uc?export=view&id=1R-Dj_ySO9Fa9Do07qCALZzpJto-Feh6h",
            "https://drive.google.com/uc?export=view&id=1kO-1zj9Qa-3cKWALh-3qYCEmQbk6M6yi",
            "https://drive.google.com/uc?export=view&id=1FeNXsiVYrmMFJjQcv1oGz9WUMYJkoubU",
            "https://drive.google.com/uc?export=view&id=170sqDgMgyiiFPgJwRIEGAvaW-uLXJOaj",
            "https://drive.google.com/uc?export=view&id=1bmjqp5hJXjtWqqQZgXn-9psTY3LJMjq-",
            "https://drive.google.com/uc?export=view&id=1pbZIO73Ajx-6HQZ9OxM-9qonXNavZCQ6",
            "https://drive.google.com/uc?export=view&id=14P9JtsIygdxCtv_pPY8zQLBxmt0vo5sR",
            "https://drive.google.com/uc?export=view&id=1tk-w9nhhsqpz5MdctWzSV9cwNpVJLI_m",
            "https://drive.google.com/uc?export=view&id=1_tD9kdrENNwrGKRvdPFm6wBUq8VYWnPV",
            "https://drive.google.com/uc?export=view&id=1OUt2VBDL7ojH2HgHiw5NffgOD4GdSAlR",
            "https://drive.google.com/uc?export=view&id=1zM_T1xeZmd8RUTsvWECycyeNM2AvzBiB",
            "https://drive.google.com/uc?export=view&id=15O8NJ3QK2qnWioO8ge8mnGQnVjpCK42H",
            "https://drive.google.com/uc?export=view&id=1p4RyNuShvQeZ-iMrrH0WC8q3xcyPLjT8",
            "https://drive.google.com/uc?export=view&id=1vgAf7Gty5GNBqP10B87RiLppetIGCWTP",
            "https://drive.google.com/uc?export=view&id=1FShuzzzUh07hDC6Ix-3apmVi2rZySUCw",
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuklinggau",
                "alamat": "Jl. nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhlillahh13",
                "kesan": "Keliatan tegas :D",  
                "pesan":"Difoto ini kayaknya Bang Rafi lagi flu gak sih bang? stay healthy ya bang"
            },
            {
                "nama": "Annisa Novatika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl.Pulau Sebesi, Sukarame",
                "hobbi": "baca novel",
                "sosmed": "@anovavona",
                "kesan": "Suka sama namanya, gak deng orangnya juga :D",  
                "pesan":"Semangat terus kak jangan lupa istirahat"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Jawanya kentel banget",  
                "pesan":"Semangat merawat bocah-bocah Gauss bang"
            },

            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Bang Fadhli vibesnya kayak mahasiswa DKV :D",  
                "pesan": "Aku suka sama pose abang difoto ini tau bang, makasih ya "
            },

            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "Aura bintangnya ada banget",  
                "pesan":"Spill MBTI bang, soalnya penasaran"
            },

            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Baca novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak kalem trs cantik juga kalau lagi ketawa",  
                "pesan":"Banyak-banyakin ketawa ya kak >_<"
            },

            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@here.am.ai",
                "kesan": "Gak expect sama hobinya Bang Anwar TT",  
                "pesan":"Maaf ya bang kalau dari kami waktu materi abang ada yg kurang merhatiin :("
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "Aku suka Kak Deva",  
                "pesan":"Tetap terus jadi orang baik yang memberikan kehangatan kak"
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kak Dinda mirip sama Velma di Scooby-Doo ",  
                "pesan":"Tetap jadi orang yang menyebarkan kehangatan kak"
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Marleta positive vibe banget plus, kakak mirip sama teman sebangku SMA aku",  
                "pesan":"Makasih ya kak, sudah jadi orang baik"
            },

            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Suka sama Kak Rut...",  
                "pesan":"Mau spill-an gendre buku yang kakak suka dong >_<"
            },

            {
                "nama": "Syahdza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Senangnya bertemu kakak NIM :D",  
                "pesan":"Kakak cantik dan baik banget, makasih sudah antusias waktu aku ngasih tahu kalau kakak itu kakak NIM aku"
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhmn_adityaa",
                "kesan": "Aku bertemu salah satu idola anak 23",  
                "pesan":"Bang, abang punya banyak fans tau"
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "Bang Eggi keliatan banget jago ngodingnya",  
                "pesan":"Semangat terus ngodingnya bang"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Muka kakak imut banget?!",  
                "pesan":"Mau rekomendasi k-drama yang gendrenya chicklit dong kak"
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Bang Syahrul ucul",  
                "pesan":"Semangat akademiknya bang"
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa keren poll",  
                "pesan":"Semangat membantu bocah-bocah Gauss"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oz66-5o4ePhNwMpI0Ij0miLkizedalkz",
            "https://drive.google.com/uc?export=view&id=1ST6LHXj_yOBkO5zfecDqubmmuK78tzKG",  
            "https://drive.google.com/uc?export=view&id=1NnZ4CUpbgttdM81RI-zMzOPOD7yi3RK9",
            "https://drive.google.com/uc?export=view&id=1UCT0Y3KY0Z4ELW8emMAXzIVodLX5up_M",
            "https://drive.google.com/uc?export=view&id=1o9yi9REaxhjxUj_Nq2hWncRBFKPJslwI",
            "https://drive.google.com/uc?export=view&id=1MMME1N5OpK9o4XtXFgMGzrxymiM3BC9I",
            "https://drive.google.com/uc?export=view&id=1fnSMQYiohk1pW6gGf5OrQd_9L0VBoPU8",
            "https://drive.google.com/uc?export=view&id=1HhL0f8A0Gukfd9bMVI3JoJNyp_iIp04W",
            "https://drive.google.com/uc?export=view&id=1VMxRAv1OJfYSWFGmsQv9s0r9X5AJZ2U6",
            "https://drive.google.com/uc?export=view&id=1XZWzzseJ1t9Ur3cgRki8XpwMRt8btrUS",
            "https://drive.google.com/uc?export=view&id=1eintoOUot6xQf4S9bLIJLZ6xLQ6Jz7_p",
            "https://drive.google.com/uc?export=view&id=1DP7BL8DO7HBmFulH9szObfHPuY_-xbb5",
            "https://drive.google.com/uc?export=view&id=1npfRK9cB_VD5eUEbqBhB2wdiPFpFC-TG",
            "https://drive.google.com/uc?export=view&id=13m7z6ZhQTGMjwXHKWtN0BcotBiy_rkgz",
            "https://drive.google.com/uc?export=view&id=1ZD_JNirb9y0FAQvEMyvMu1UxMJawgqI2",
            "https://drive.google.com/uc?export=view&id=1RkG1PnzrtC7425G9fwpnhGxLYSSYt3Os",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@yogyyyyyyy",
                "kesan": "Bang Yogy humble banget orangnya",  
                "pesan":"Kenapa muka abang cemberut gitu?!"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kak Dhita perhatian banget, riil",  
                "pesan":"Tetap jadi orang perhatian kak :D"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana cantik banget?!",  
                "pesan":"Kak, love kita mleyot gitu..."
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "Somehow, Kak Dea ada vibes sumbarnya",  
                "pesan":"Kak Dea plis banget jadi orang baik terus :)"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kak Novelia mirip Cindy gak sih...",  
                "pesan":"Jadi orang baik terus kak <3"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Menyala atlet basket Sains Data!",  
                "pesan":"Semangat ngebasket dan kuliahnya bang"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Muka Bang Irvan gak asing...",  
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "Bang Rizki ramah banget orangnya",  
                "pesan":"Abang kurang 1 jempol lagi :D"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@arafiramadhanmaulan",
                "kesan": "Abangnya agamais bener",  
                "pesan":"Semoga terus istiqamah"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfaw",
                "kesan": "Kak Chalifiaaa, makasih sudah mau berpose spiderman",  
                "pesan":"Kakak... aku suka kakak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "Bang Raid mukanya kayak gak asing...",  
                "pesan":"Semoga aku bisa punya hobi yang mirip-mirip sama abangnya"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "17",
                "asal":"Bogor",
                "alamat": "Pemda",
                "hobbi": "Bersholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kak Yuna cantik banget?!",  
                "pesan":"Makasih sudah inget aku kak <3"
            },
            {
                "nama": "Khalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kak Khalisa imut banget",  
                "pesan":"Semoga istiqomah untuk tillawah kak"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Ening",
                "alamat": "Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kak Asa imut dan baik banget",  
                "pesan":"Semangat ngerjain donor darahnya kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Planning Content",
                "sosmed": "@jasminednva",
                "kesan": "Kak Mine humble dan ramah banget",  
                "pesan":"Semangat kerjanya kak :D"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Main Volly",
                "sosmed": "@@izzalutfiaa",
                "kesan": "Kak Izza ramah poll",  
                "pesan":"Tetap jadi orang baik kak :D"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CEbEknD57Qn-i6jkA0f6_KwJw86YyVNk",#1
            "https://drive.google.com/uc?export=view&id=1J3003BIOsCA6FG5PLBoDTEh50bq2XQFM",#2
            "https://drive.google.com/uc?export=view&id=16CyrcL1411WMZ23O5K7xYMauFt-jlWFw",#3
            "https://drive.google.com/uc?export=view&id=1XGruZv_jPhw60LrADO6Js-3Yf7ZA0os7",#5
            "https://drive.google.com/uc?export=view&id=1mGuls3rlIoBy1bZYMgcz10lwk0H0vvIu",#6
            "https://drive.google.com/uc?export=view&id=1TLG0JjTaaynaj5c2vXSuwbv3GVbcJFRl",#7
            "https://drive.google.com/uc?export=view&id=1wG5c3q1lRAr41Pi0S7QWoue-nmDpH3Xo",#8
            "https://drive.google.com/uc?export=view&id=1DvkKpYXNDHV1Xvjb-N8Rq7Ajp7AOskjt",#9
            "https://drive.google.com/uc?export=view&id=1JtB2jTS0NCx-wUmEhibbzcej4xFLB-_9",#10
            "https://drive.google.com/uc?export=view&id=1hNWWVElTYY52H5oi4CHCZfSgWxArZQ6x",#11
            "https://drive.google.com/uc?export=view&id=1a2S1C2yzHmc2GXoTC6Zafgh6398on2Ss",#12
            "https://drive.google.com/uc?export=view&id=1vjl3a-p9Sv7PiUkNFJm9lALhUOnGh4ii",#13
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":"Pamulang, Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "Manjat tower sutet",
                "sosmed": "@dimzrky_",
                "kesan": "Bang Dimas sangat supportif",  
                "pesan":"Makasih bang sudah terus support 23 :D"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@catherine.sinaga",
                "kesan": "yeay, senang ketemu kakak nim",  
                "pesan":"Aku suka kakak dan foto kita di sini"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "Bang Ari Sigit mukanya mewakili divisinya",  
                "pesan":"Terus semangat dan jaga kesehatan kak"
            },
        
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kak Meira mirip temen aku...",  
                "pesan":"suka banget sama vibenya Kak Meira, tetap jadi orang baik kak"# 5
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Bang Rendi baik banget, serius",  
                "pesan":"makasih bang sudah jadi salah satu orang baik di dunia ini, eak"
            },
            {
                "nama": "Josua Alfa Viando Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Ini abang yang sering disangkut pauting sama mahasiswa Unila ><",  
                "pesan":"Semangat kulianya bang"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "Lucu bgt hobinya",  
                "pesan":"Semangat mengoleksi dino, bang"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "It is our third times ketemuan hihi",  
                "pesan":"seneng banget bisa ketemu Kak Renta lagi :D semangat terus kak"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Lihat cogan",
                "sosmed": "@slwafhn_694",
                "kesan": "Kak Salwa ramah, cantik, baik, lope pokoknya",  
                "pesan":"Semangat terus jadi orang yang ramah dan baik kak"
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@ranipuu",
                "kesan": "Kakak suka seni gitu kah?",  
                "pesan":"Semoga aliran outfit kakak gak ganti"
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Bang Yosia auranya ramah gitu",  
                "pesan":"Makasih sudah senyum lebar bang tapi kenapa aku yang gak senyum lebar ya..."
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abang ini ada di mana-mana",  
                "pesan":"Semangat jadi ketuplak riuh bulau ini bang!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1v9a0to0ppM-6k9qpHK8Nlmbib3DXqHwW",
            "https://drive.google.com/uc?export=view&id=1Ryr5yQ1-nl7_QP7ZoWoBITHJAm0Fn3Ui",
            "https://drive.google.com/uc?export=view&id=1EHyzVH_MvfmiYS59ZXcAMHC0FDFpfJIm",
            "https://drive.google.com/uc?export=view&id=1AdHgyCzzSyqLC7EcLWfh3DLYclN6cDt4",
            "https://drive.google.com/uc?export=view&id=17P2sX4ebK5DKLJdeMKgyAeuX_FVfriiN",
            "https://drive.google.com/uc?export=view&id=1usYxnZFUWrvqtu4dQTTi7l9jmRTLffq6",
            "https://drive.google.com/uc?export=view&id=1hcT69RzRPoWtxAq69VX40npoBJnSvCP3",
            "https://drive.google.com/uc?export=view&id=1uXxDX84uYnH-EmMMPOdEPM4hgLcqNuj6",
            "https://drive.google.com/uc?export=view&id=1Wh4QYMieNlm4RPePCQDmBvpRN3YtND91",
            "https://drive.google.com/uc?export=view&id=1CVHzDPT-jrnCW-J_PxS_5Q5rWX3q1CJU",
            "https://drive.google.com/uc?export=view&id=1OrOeiDcO7jsIhdpNgLHCeVLqGo_N3CUq",
            "https://drive.google.com/uc?export=view&id=1pB1aXpluYdEVW7OQNaGQ0ITXe4rBkiiX",
            "https://drive.google.com/uc?export=view&id=1ovugRMrzPiWlIyFv_jb-A3WHGBC0KM09",
            "https://drive.google.com/uc?export=view&id=1e4yISaSnTM250B3UYrOHbk07EoIS4izA",
            "https://drive.google.com/uc?export=view&id=1PQCCi95qZQeT-mC3wUv7DotBikZr6iv6",
            "https://drive.google.com/uc?export=view&id=1QJDpAHVy9vjQoA3fDEyVvMEo4OsYPb5o"
        ]
        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@wayuraja",
                "kesan": "pasti Bang Wahyu PDD abadi",  
                "pesan":"semangat terus bikin branding sosmed HMSD bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "121450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@Elokviola",
                "kesan": "Kak Elok cantik banget?!",  
                "pesan":"Makasih sudah mau pose anjing bareng aku kak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kak Cybel cantik banget...",  
                "pesan":"semangat ngegymnya kak, spill tempat gym yang muslimah friendly"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak Cia sangat positive vibe",  
                "pesan":"Tetap jadi orang yang ceria ya kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Neli imut banget, aku sukak",  
                "pesan":"Makasih sudah inget sama aku kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakaknya imut banget, aku sebel sama diriku difoto itu hiks",  
                "pesan":"semangat terus kak, maaf aku kayak beda konsep di foto ini huhuu"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Bang Kaisar humble banget orangnya",  
                "pesan":"Makasih sudah mau berpose fox bersama saya bang :D"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@dwiratnn_",
                "kesan": "Kak Ratna kalem banget...",  
                "pesan":"semangat kuliahnya kak, anw love kita kurang melengkung"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@gymnn.as",
                "kesan": "ini yang kata Kak Izza sepuh laprak ADS",  
                "pesan":"semangat ngasprakin RC bang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kak Nasywa positive vibe banget?!",  
                "pesan":"semangat terus bersih-bersihnya kak <3"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakak manis bgt siiih",  
                "pesan":"Stay happy and stay healthy kak"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan": "Abangnya ramah poll",  
                "pesan":"makasih sudah mau berpose seperti itu bang :D"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Bang 'Abit ramah banget, serius",  
                "pesan":"semangat terus ngemedkraf Bang Abit"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "Ini juga, Bang Akmal ramah banget orangnya",  
                "pesan":"dari Bang Akmal aku belajar bahwa, setelah TPB tidur akan menjadi hobi bukan kewajiban"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Wiih abang asprak alpro RC",  
                "pesan":"Semangat ngasprakin RC bang, jangan capek-capek kalau kami ngeluh ya bang"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Ini kakak yg dibilang mirip Nisa 23 kah?",  
                "pesan":"imutan kakak daripada Nisa hahahaha jk nis,"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11MtiATNchwxBU0WSJ8wJNeBZhtzoGLKM",
            "https://drive.google.com/uc?export=view&id=1JIwp8GMIr7LO-R-TyQVio0NtWGL3zW8e",
            "https://drive.google.com/uc?export=view&id=1moUdXZ3vP33dmvWvmE6aGcdPuoZx3inw",
            "https://drive.google.com/uc?export=view&id=1YVaBOIkMyCBAlrn9CvjxUqCBp_vUwINu",
            "https://drive.google.com/uc?export=view&id=1umoBJIAACu7kzUyvbm8B2ogRbZYuPfhs",
            "https://drive.google.com/uc?export=view&id=1AkApFjzAkCi3P6wW8yvFdZp_cJpdbhaL",
            "https://drive.google.com/uc?export=view&id=1y-XUUurdBiAYQcyZRci37mTd3usd58QR",
            "https://drive.google.com/uc?export=view&id=1pP3C6qx4rI1pqr-BhuJpPX8rdT0upP_c",
            "https://drive.google.com/uc?export=view&id=1CxirOpyoaJbmHK4jxiuzJddFWCca8Rg8",
            "https://drive.google.com/uc?export=view&id=1VAeHQL_A8sRpcWANhuc5UT3Sq1Vi6BWT",
            "https://drive.google.com/uc?export=view&id=1zELUXwETRnGxrMJmUc1oye6_jQKW51yV",
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "20",
                "asal":"Cirikalang",
                "alamat": "Dekat penjara",
                "hobbi": "Nyari hobi",
                "sosmed": "@andrianlgaol",
                "kesan": "Bang Adrian keren banget, serius",  
                "pesan":"Semangat terus bang ngembangin bisnisnya"
            },
            {
                "nama": "Adisty Syawalda Arianto ",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@adhistysa_",
                "kesan": "Kak Adisty cantik banget?!",  
                "pesan":"mau rekomendari film yang horror tapi gak bikin jantungan dong kak"
            },        
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "Kak Nabila ramah banget, seneng ketemu sama kakak",  
                "pesan":"Pasti tingkat fokus kakak tinggi karena suka ngitung uang"
            },  
            {
                "nama": "Ahmad Rizqi ",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "Ooh ini abang yang banyak fansnya",  
                "pesan":"Semangat jadi idola 23 bang :D"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Makasih bang sudah mau berfose seperti itu :D",  
                "pesan":"Semangat terus ngembangin It's Clean"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "menyala capo Sains Data!",  
                "pesan":"semangat terus bang jadi capo"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakaniaa",
                "kesan": "Sumpah yaa, Kak Tessa positive vibe banget :)",  
                "pesan":"Tetap jadi orang baik ya kak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kak Nabilah imut banget, baik juga",  
                "pesan":"Stay imut kak hihi"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@alviagnting",
                "kesan": "Kak Alvia imut banget siih",  
                "pesan":"Semangat terus kuliahnya kak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "Bang Dhafin pendiem banget...",  
                "pesan":"Semangat terus bang, semoga KWU SSD lancar terus"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "122450076",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@meylaniellia",
                "kesan": "Kak Elia ramah banget?!",  
                "pesan":"Mau lihat Kak Elia nyanyi"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()