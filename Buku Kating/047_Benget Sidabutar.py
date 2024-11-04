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
            "https://drive.google.com/uc?export=view&id=1KTygLuZPXmS_SiDPbjLFu5JGQ9KH9Zj1",
            "https://drive.google.com/uc?export=view&id=1KYoN3B1_WoFcNXGyaoSv2ZBpt3hrVDcF",
            "https://drive.google.com/uc?export=view&id=1KhBPaoNJbT789Zx01UBverrxY494kVJ2",
            "https://drive.google.com/uc?export=view&id=1KN4kpD5_AEYz4bEbstxRpj54luX8T3F5",
            "https://drive.google.com/uc?export=view&id=1KjII7ZvV4RhLk8SuxtpIWO1kNejibd8W",
            "https://drive.google.com/uc?export=view&id=1KP8tneE6x8Sp1-qgI7Gjfom2edjIsGqu",
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
                "kesan": "Abangnya asik sekali",  
                "pesan":"Semoga sukses terus bang."
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abang nya Menyenangkan dan hangat:",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakak nya Pendengar yang baik",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak nya Ramah dan bersahabat",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakak nya kelihatan nya Pekerja keras:",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "kakak nya Rendah hati:",  
                "pesan":"semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Q-bBl6vk3LvZ2epy39d-SBgKrPstihPX",
            "https://drive.google.com/uc?export=view&id=1PpFPQo-TTZ9ovs9aXRQxLej4_vnNceq3",
            "https://drive.google.com/uc?export=view&id=1Pp8TjF6U0GNfE83bqevJBY5GnKSIUaSV",
            "https://drive.google.com/uc?export=view&id=1PqV-qA4pKAjSF0iDarKBHNR4Oiel0XR4",
            "https://drive.google.com/uc?export=view&id=1Rhh2tyVqDK0zomESAGtvb_W5qi9Xso_W",
            "https://drive.google.com/uc?export=view&id=1Q2o0dN36HfDQrnRzuNlcmG6se2mxH5vj",
            "https://drive.google.com/uc?export=view&id=1Px71SbEofvjcGUpuq-UdgwqkcnbzLuDs",
            "https://drive.google.com/uc?export=view&id=1PvchlIPI3zu3qj2S-Kx7-2-bT3js-cfc",
            "https://drive.google.com/uc?export=view&id=1PtOXKGkmJoOHvwbtpxDkWU3uHmjOT48o",
            "https://drive.google.com/uc?export=view&id=1Q-EzJHH3VQJ6PckrIlTbWQf__8pirawF",
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
                "kesan": "Kakak ini asik sekali dan membuat suasana menjadi enak",  
                "pesan":"semangat terus kuliah nya kak semoga cepat lulus"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "kakaknya asik dan baik sekali",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "kakaknya asik sekali dan informatif sekali",  
                "pesan":"semangat terus kak kuliah nya"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "abangnya seru diajak ngobrol",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya seru dan asik",  
                "pesan":"semangat terus bang kuliah nya"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang nya pendiam",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "abangnya asik sekali dan informatif sekali",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak nya kelihatan nya pendiam dan cantik",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "kakak nya pembawaan nya asik dan menyenangkan",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini asik dan ramah",  
                "pesan":"semangat kakak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Vvinc-dV0mR2e6_DWiSvL-BZs_pNM1Ne",
            "https://drive.google.com/uc?export=view&id=1W8KkBnMdSvPg6HA-NXWCda2pL6JQRl5g",
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahyu",
                "hobbi": "Bernyanyi",
                "sosmed": "@anissaluthfia_",
                "kesan": "Kakak nya Menginspirasi",  
                "pesan":"Semoga kakak nya Lulus Tepat Waktu"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "Bang bintang inspiratif dan asik di ajak ngobrol ",  
                "pesan":"Tetep jadi orang baik bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Lx9X7cd5lFyhdC0t-AhyV_rX_kW60zFg",
            "https://drive.google.com/uc?export=view&id=1MJYnqz1O8NhWYYxkCUWc_fmiqUfxOycW",
            "https://drive.google.com/uc?export=view&id=1M58p6vlxfsu-R3i5sh9EZB15rjqCeOdC",
            "https://drive.google.com/uc?export=view&id=1M4FVhOhwYjOXKiQ_Czp3Xv_1MC51tg3g",
            "https://drive.google.com/uc?export=view&id=1MCvCEhgYeH32z_6wxGxZWK6i-fhHIHQ4",
            "https://drive.google.com/uc?export=view&id=1M5Rn2WXLuVRp1wNMurVCVkorvMW1JZbB",
            "https://drive.google.com/uc?export=view&id=1MITQNt4_O9DmG06xD5YHiDb2mJwRHLVt",
            "https://drive.google.com/uc?export=view&id=1M6eIPG1URfqNddPE-VQcOb-yUcdG0_vG",
            "https://drive.google.com/uc?export=view&id=1MGjBvNJwbhCuxOdB65NKwG-Zz0oBjdxv",
            "https://drive.google.com/uc?export=view&id=1LbXK2xUyGXpWO6CjyWPAzOSdC6ozarup",
            "https://drive.google.com/uc?export=view&id=1LoqY5n614tUBHKcaGP0PxpxHIHGOdB4t",
            "https://drive.google.com/uc?export=view&id=1wFtOh_E6No3NgFesNBAzHFWMZg_w4vp0",
            "https://drive.google.com/uc?export=view&id=1LlcZbSlNYPnZq0sN34myCRTWIORfZNbF",
            "https://drive.google.com/uc?export=view&id=1Lffup2qOGIYMQDADs3kmOTiIPIpV0zyl",
            "https://drive.google.com/uc?export=view&id=1LnXnKOlK9ceyWxVjCQVS_c1lDCUT-nzk",
            "https://drive.google.com/uc?export=view&id=1M3CRVj-GCIfJS8V7JJGcOctj6Ql_wbmc",
            "https://drive.google.com/uc?export=view&id=1LpwCePkIxHDl5Ysp1cZ7LhCWTHKs6GqH",
            "https://drive.google.com/uc?export=view&id=1M2c3VS0D0wq7vlxbxnyosE_XqkESy1UR",
            "https://drive.google.com/uc?export=view&id=1LudxDa0QO3TpiEw9mm0VDNZ6RYyvHOuw",
            "https://drive.google.com/uc?export=view&id=1LpWZDRaS-uD-Fn_S3SGF5wlky8zM6pZp",
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
                "kesan": "Bang Econ Ramah dan Kelihatan nya Tegas sekali",  
                "pesan":"Semangat terus kuliahnya Bang dan semoga bisa lulus tepat waktu dan sukses dalam kariernya nanti."
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakak nya ramah, seru, dan asik.",  
                "pesan":"semangat Terus kuliahnya Kak "
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Afifah orangnya seru dan asik.",  
                "pesan":"Semangat Terus Kak kuliah nya"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami",
                "kesan": "kakak Allya asik dan seru diajak ngobrol.",  
                "pesan":"semangat terus kak kuliah nya"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakak Eksanty menyenangkan dan asik.",  
                "pesan":"Semangat terus kuliahnya Kak, dan Jangan Menyerah"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakanyanya seru dan asik",  
                "pesan":"Semangat terus kuliahnya Kak"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya seru diajak ngobrol",  
                "pesan":"Semangat Bang kuliahnya dan sukses mengejar impian."
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "abangnya asik dan menyenangkan",  
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya menyenangkan dan asik pembawaannya",  
                "pesan":"Semangat terus Kak kuliahnya dan jangan menyerah"
            },
            { 
                "nama": " Deyvan Loxefal", 
                "nim": " 121450148 ", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanlo", 
                "kesan": "Bang Deyvan Ramah, asik dan seru.",   
                "pesan":"Semangat terus Bang kuliahnya dan semoga semua cita-citanya tercapai." 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamy", 
                "kesan": "Kakaknya Cantik dan Lucu.",   
                "pesan":"Semangat terus Kak kuliahnya" 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "Bang joh sangat Ramah dan Kalo diajak ngobrol asik sekali",   
                "pesan":"Semangat terus bang kuliahnya dan semoga semua cita-citanya tercapai." 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "bang kemas Ramah, Keren dan asik",   
                "pesan":"Semangat terus bang kuliahnya" 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Bang Sahit enak di ajak ngobrol seru dan asik",   
                "pesan":"Semangat bang kuliahnya " 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya Kelihatan nya Pendiam",   
                "pesan":"Semangat terus Kak kuliahnya" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Bang Farhan sangat menyenang kan dan seru di ajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya dan semoga Lulus tepat Waktu"
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": " bang gede asik dan seru.",  
                "pesan":"Semangat terus bang kuliahnya "
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "kakak yang paling cantik, ramah dan juga baik",  
                "pesan":"Semangat terus kuliahnya kak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abang nya asik di ajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakak nya Kelihatan nya Pendiam",  
                "pesan":"Semangat terus Kak kuliahnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZsEXLdj5fKdNuTp1MO6CRnKzGK6wWZGA",
            "https://drive.google.com/uc?export=view&id=1_-kJTztWLN7-ae1WDgOqN86-RvK4qLAD",
            "https://drive.google.com/uc?export=view&id=1ZzGBcXh5kd5aEeuHddVJRWNJlAbRU0SJ",
            "https://drive.google.com/uc?export=view&id=1_D8bMrqNnMufD5Dq9SC41pxisPnZqVzb",
            "https://drive.google.com/uc?export=view&id=1_3lUPl5W-CQ6IAPOkuyK_9IzwGwshtba",
            "https://drive.google.com/uc?export=view&id=1Ztj8E1AUmvzobbUEs1uigO7Lu2yRAR8b",
            "https://drive.google.com/uc?export=view&id=1_7rigHsn25liKqhhUipZda_GMymLmLs3",
            "https://drive.google.com/uc?export=view&id=1_9BKpUw_OF-3xPDH5F_h4FXDFS9YEbdR",
            "https://drive.google.com/uc?export=view&id=1fpKGiU7Oac_9lC2B0tNzHNVk1voQGhYY",
            "https://drive.google.com/uc?export=view&id=1_6oOY0rNMnKPxwOcLUBA3e-MckhGikr5",
            "https://drive.google.com/uc?export=view&id=1_4wvbDWYj9qGN3Dr8Wo8wAQ1OlvLADll",
            "https://drive.google.com/uc?export=view&id=1_9CszgmqsNdAfgz4wkS8z67_-Mcjn-Z8",
            "https://drive.google.com/uc?export=view&id=1_BuBe6Hdaa8XzmThCau7fR3O2jGAXanS",
            "https://drive.google.com/uc?export=view&id=1ZzycOgMOX7boR6Akqxadb0uitHddpouF",
            "https://drive.google.com/uc?export=view&id=1Zt76vyNINxplg1i64c9PJXfey3yS94jW",
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
                "kesan": "Bang Rafi Keliatan tegas",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Annisa Novatika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl.Pulau Sebesi, Sukarame",
                "hobbi": "baca novel",
                "sosmed": "@annovavona",
                "kesan": "Kakak nya canti, baik, dan ramah",  
                "pesan":"Semangat kak kuliah nya"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Bang Sahid asik orang nya, suka buat becanda",  
                "pesan":"Semangat bang kuliah nya, dan juga Semangat merawat bocah-bocah Gauss bang"
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
                "pesan":"Semangat terus bang"
            },

            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Baca novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak nya Pendiam bangat",  
                "pesan":"Semangat terus kak"
            },

            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@rhmn_adityaa",
                "kesan": "Abangnya keren dan asik banget",  
                "pesan":"Semangat terus bang"
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "121450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "kakaknya asik dan menyenangkan",  
                "pesan":"Semangat terus kak"
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya Kelihatan nya Baik!",  
                "pesan":"Semangat terus kak"
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Marleta positive vibe banget",  
                "pesan":"Semangat terus kak"
            },

            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak Ruth Pendiam, tapi kakak nya baik dan ramah",  
                "pesan":"Semangat terus kak"
            },

            {
                "nama": "Syahdza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kakak nya asik banget orang nya",  
                "pesan":"Semangat terus kak"
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhmn_adityaa",
                "kesan": "Abangnya seru dan enak di ajak ngobrol",  
                "pesan":"Semangat terus bang"
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "Gokil dan asik banget",  
                "pesan":"Semangat terus bang"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Hobinya relate banget",  
                "pesan":"Semangat terus kak"
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "Abangnya pendiem tapi kelihatan nya ceria",  
                "pesan":"Semangat terus bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1H2iTFZQZD7zUdGt95d4wOH3wI0AhrvEd",
            "https://drive.google.com/uc?export=view&id=1H3pXUNBlAhexBBClsKeoT8yGLcah0QOS",  
            "https://drive.google.com/uc?export=view&id=1HCrrtmZNe5L8ZOTsYT3r_U2yRfDg6rIX",
            "https://drive.google.com/uc?export=view&id=1HaNy-bmvS8r9dD8URFAiu002K_U-_4oz",
            "https://drive.google.com/uc?export=view&id=1H4h8RWmfgOGTuhgESouDwmzYWv8ldJ1f",
            "https://drive.google.com/uc?export=view&id=1H45EhQJ-0oFK_n-28OckTtkANIgxcfih",
            "https://drive.google.com/uc?export=view&id=1HKaeISNyV85DAwvE0KDNd73hn0Uzz6eF",
            "https://drive.google.com/uc?export=view&id=1H_Qh6ptMZ7s6RB3-RI_sLiI1QwbQmfso",
            "https://drive.google.com/uc?export=view&id=1HY2WgWKsaffAAxe2n2IPPm8QcHebV69u",
            "https://drive.google.com/uc?export=view&id=1HMZZ9zDz8SeT_k9_t6h0NygH-dZWt2qu",
            "https://drive.google.com/uc?export=view&id=1HXSc-SOPs9-SFbDNRMCRz_uKAHw6UnDg",
            "https://drive.google.com/uc?export=view&id=1HUyhtEDbk76D5H50ZNvWBRL-deYnNffa",
            "https://drive.google.com/uc?export=view&id=1HMbtldaF-hAD5a1XTvnBnP_RIU_SBm8U",
            "https://drive.google.com/uc?export=view&id=1HK2fifIBu5t5hJu8-iJ0zBNY5uc3NXtM",
            "https://drive.google.com/uc?export=view&id=1HFfB990s6qbKhuuyoBzqKsBwttlcTgHa",
            "https://drive.google.com/uc?export=view&id=1aJtNHgOrHfbpdncGFBNzY46o4PlyMrL_",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@Yogyyyyyyyyy_",
                "kesan": "Bang Yogi keren banget publik speaking nya",  
                "pesan":"Semangat Kuliahnya bang, semoga lulus tepat waktu"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121400131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya Sangat seru",  
                "pesan":"Semangat Kuliahnya Kakak"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya kalem dan ramah",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kak dea sangat asik sekali dan ceria",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya keren dan Cantik",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Bang Tobias orang nya asik dan enak ketika di ajak ngobrol",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya keren dan asik,",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Rizki Adrian Bennofry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abang nya Laki banget",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@rafiramadhanmaulan",
                "kesan": "abang nya asik dan menyenangkan",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfawwwww",
                "kesan": "Kakak ini baik dan asik",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "abang nya cool banget dan juga abang nya kelihatan nya pendiam",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "17",
                "asal":"Bogor",
                "alamat": "Pemda",
                "hobbi": "Bersholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kakak ini unik dan asik",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Ening",
                "alamat": "Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini lucu dan kalem",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Planning Content",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik, dan sangat menyenangkan",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Main Volly",
                "sosmed": "@@izzalutfiaa",
                "kesan": "Kakak asik dan menyenangkan",  
                "pesan":"semangat kuliahnya kakak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16Vmq7gIRAp32Y-PSmXoPKUnVAu6ylcvK",#1
            "https://drive.google.com/uc?export=view&id=1MkAcA5KTFhZPc-GM-JHAhmRI_nCGuQuM",#2
            "https://drive.google.com/uc?export=view&id=10ITUqzcDPWvz4XqwLCtpNM6TOXJy-beP",#3
            "https://drive.google.com/uc?export=view&id=1JvVYeIEDulCuJnrCkdIYWPGPGuc90pZA",#4
            "https://drive.google.com/uc?export=view&id=1qLQ3AqDkL3UPb_U-8__wZ2wEMa3cEtxj",#5
            "https://drive.google.com/uc?export=view&id=1vJi0E2OYGeMG0ckzkRg_XoVxdRWYhNYc",#6
            "https://drive.google.com/uc?export=view&id=1Sppb4INS1pGBVwt7X1WLQ3ajyj2YvbyC",#7
            "https://drive.google.com/uc?export=view&id=1VF08RZ5b4yRFu_Q_K6j30oFsbxr53KNw",#8
            "https://drive.google.com/uc?export=view&id=1Y0g8V2zer4KEnZZzkG6L5mB_7QNWckGO",#9
            "https://drive.google.com/uc?export=view&id=1img9CUfcDd17JDf3AfGHcrBpBlCO_Qrn",#10
            "https://drive.google.com/uc?export=view&id=1dAjVboPkduhUkpb9oJ-muBoR91VXrdQO",#11
            "https://drive.google.com/uc?export=view&id=18HaXqLDs-ZbIWpwjnzOde2Qd1jz7BJ12",#12
            "https://drive.google.com/uc?export=view&id=1XxA12enISjSC1P0rFVuJZi5oqb0QYzRq",#13
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
                "kesan": "Abang sangat menginspirasi",  
                "pesan":"semangat terus kuliahnya bang, semoga lulus tepat waktu"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@catherine.sinaga",
                "kesan": "Kakaknya baik,, positive vibes",  
                "pesan":"semangat terus kuliahnya kak, semoga semua urusannya diperlancar"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "Bang Sigit sangat membantu dan mudah diajak bicara.",  
                "pesan":"Semoga Abang nya lulus tepat waktu"
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakak nya sangat ramah",  
                "pesan":"Semoga Kakak sukses dalam setiap langkah ke depan"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakak nya pendiam tapi kakak nya luar biasa dalam membimbing",  
                "pesan":"Semoga kebahagiaan selalu menyertai Kakak"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@lexanderr",
                "kesan": "Bang Rendy memiliki kepribadian yang ramah dan menyenangkan.",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Abangnya sangat sabar dan baik",  
                "pesan":"Semoga Kakak lulus tetap waktu"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar.resdika",
                "kesan": "Abang nya selalu berusaha menciptakan suasana yang menyenangkan.",  
                "pesan":"Semangat terus bang kuliah nya, semoga lulus tepat waktu"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak sangat bersahabat dan menyenangkan!",  
                "pesan":"Semoga Kakak lulus tepat waktu "
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Lihat cogan",
                "sosmed": "@slafhn_",
                "kesan": "Kakak sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semangat terus kak kuliah nya"
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@ranipuu",
                "kesan": "Kakak sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semangat yh kak kuliah nya"
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "bang yos sangat baik, dan enak di ajak ngobrol dan penuh pengalaman.",  
                "pesan":"Semangat yh bang kuliah nya, semoga lulus tepat waktu"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abang nya sangat bijaksana dan penuh pengalaman",  
                "pesan":"Semangat terus bang bang kuliah nya semoga, lulus tepat waktu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Msyp6ge_JoiaTky-l6803gwqrP-YWAyI",
            "https://drive.google.com/uc?export=view&id=1N4GBj6rHA6cCLwryYVLOeSydwQ4z1KYn",
            "https://drive.google.com/uc?export=view&id=1N8QrsuSGXsaHkRZs4BZj-mmxPnk1NbSm",
            "https://drive.google.com/uc?export=view&id=1N79U96-FL4VGel90EETSuHGz7D4lfKw0",
            "https://drive.google.com/uc?export=view&id=1My2gHVBfYuco28Tnw9DbRJlmgIN7NJDM",
            "https://drive.google.com/uc?export=view&id=1My4ca7p7p8V9cry2YLgmQxGRDzHMoDIK",
            "https://drive.google.com/uc?export=view&id=1MzSdpMVh4wZAOlzcRVRgIlvAsLWwdBx5",
            "https://drive.google.com/uc?export=view&id=1N-0MdM_Zc_IJp_vw-lVDeZPne2IWf3Qc",
            "https://drive.google.com/uc?export=view&id=1N2_2t-8LIdwWUn2NrMx4J48phRee7Lwl",
            "https://drive.google.com/uc?export=view&id=1N0mjNftA5hDbyQTAAP2_PaBuw0QBF9Kb",
            "https://drive.google.com/uc?export=view&id=1MsBOP0r-bAmTPp4VxAHgmHy-anrif5Ha",
            "https://drive.google.com/uc?export=view&id=1NJ6QxLZv1w5PXwN4MXA9xBiZhet-69nI",
            "https://drive.google.com/uc?export=view&id=1NGgv1Xcs-43EPwgLqXCLREnchdYLCbii",
            "https://drive.google.com/uc?export=view&id=1NJ01NUSfjx7SqaRCRDB6ud9BmAgNiuOU",
            "https://drive.google.com/uc?export=view&id=1NAcGjhI1YOez-Fo3BFw_MnmP1V5c5q3s",
            "https://drive.google.com/uc?export=view&id=1N8hHhPwWDsrjCC_DUuwrtoA12dQkwEjH",

        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": " @wayyulaja",
                "kesan": "Abang nya  asik sekali",  
                "pesan":"semangat terus bang kuliah nya, semoga lulus tepat waktu"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@Elokviola",
                "kesan": "kakak ini cantik sekali, dan super lembut",  
                "pesan":"semangat kak kuliah nya"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Kakak nya asik dan seru ketika di ajak ngobrol",  
                "pesan":"semangat kak belajarnya"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "Kakak nya cantik dan suka bercanda",  
                "pesan":"semangat kak terus kak kuliah nya"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "Kakak nya asik dan ramah",  
                "pesan":"semangat terus kak kuliah nya"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "akaknya asik dan menyenangkan",  
                "pesan":"semangat terus kak kuliah nya"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Abangnya asik dan menyenangkan",  
                "pesan":"semangat bang kuliah nya"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kakak nya baik dan ramah",  
                "pesan":"semangat terus kak, untuk menjalani kuliah nya"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@aimnn.as",
                "kesan": "Abang nya Asik dan suka bercanda",  
                "pesan":"semangat terus bang kuliah nya"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kak Naswa sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kak anisa dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "-",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@Arsalutama",
                "kesan": "Abang nya seru dan asik ketika di ajak ngobrol",  
                "pesan":"semangat terus bang belajarnya"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Bang Abit sangat keren dan lucu",  
                "pesan":"semangat terus bang belajarnya"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@akmal.faiz",
                "kesan": "Kak akmal sangat sopan dan asik sekali",  
                "pesan":"semangat terus bang belajarnya"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "Bang Hermawan orang nya kelihatan tegas banget",  
                "pesan":"semangat terus bang belajarnya"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kak anisa dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1I2CekjPMaCNQ9t3AL_3VEQIUN9ZeGCdG",
            "https://drive.google.com/uc?export=view&id=1HxSEgKadFUX7ay2XDlGHmwOhnM6Eo5ns",
            "https://drive.google.com/uc?export=view&id=1I1o2MPH0qFde73J3nN_OnaW0F89YhZL3",
            "https://drive.google.com/uc?export=view&id=1HtnEGbSM6ohZ73iDzRYpRn2U5jAnahxz",
            "https://drive.google.com/uc?export=view&id=1Hp-oRcxSDvFePAWlqGSCPGl2Si-b9_mX",
            "https://drive.google.com/uc?export=view&id=1Htfx_nBdHAeqOIJVa3LGMYzxTSY0TnwG",
            "https://drive.google.com/uc?export=view&id=1HxvA9Ze-4-Uc0UaxGIalAvaZ3qPqUgSV",
            "https://drive.google.com/uc?export=view&id=1I9PT8wdRcumtgEqSNDg4C0pm27nU5drS",
            "https://drive.google.com/uc?export=view&id=1I4jqMNdRyirSaNyqBg3x758ywTmmXhTr",
            "https://drive.google.com/uc?export=view&id=1I26MgOh2GszQmZE647WKTE_rPMdsBQuc",
            "https://drive.google.com/uc?export=view&id=1I9OvV7KanWtYqdqHA5E-Uk3BaDw9hG8I",
        ] 
        
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol ",
                "nim": "121450090",
                "umur": "20",
                "asal":"Cirikalang",
                "alamat": "Dekat penjara",
                "hobbi": "Nyari hobi",
                "sosmed": "@Andrianelgaol",
                "kesan": "Abang nya Tegas dan pintar",  
                "pesan":"semangat terus bang kuliah nya, semoga lulus tepat waktu"
            },
            {
                "nama": "Adisty Syawaida Ariyanto ",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@Adhistysa_",
                "kesan": "Kakak nya kelihatan nya pendiam",  
                "pesan":"Semangat terus kak kuliah nya, semoga lulus tepat waktu"
            },        
            {
                "nama": "Nabila azhari ",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "Kakak nya Ramah dan baik",  
                "pesan":"Semangat kak kuliah nya, semoga lulus tepat waktu"
            },  
            {
                "nama": "Ahmad Rizqi ",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@Ahmda.riz45",
                "kesan": "Cara berpikir Abang nya selalu logis dan rasional",  
                "pesan":"Semangat terus bang, kuliah nya"
            },
            {
                "nama": "Danang hilal kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Abang nya punya cara unik untuk membuat orang lain tertawa.",  
                "pesan":"Semangat terus bang kuliah"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "Abang nya orang yang sangat bisa diandalkan.",  
                "pesan":"Semangat terus bang kuliah nya"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakaniaa",
                "kesan": "Kakak nya selalu bisa membuat semua orang di sekitarnya merasa nyaman.",  
                "pesan":"Semangat terus kak kuliah nya"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanfir",
                "kesan": "Kakak nya selalu punya energi positif yang bikin orang di sekitarnya bahagia.",  
                "pesan":"Semangat terus kak kuliah nya, semoga lulus tepat waktu"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alfiagntng",
                "kesan": "Cara berpikirnya kakak benar-benar menginspirasiku.",  
                "pesan":"Semangat terus kak kuliah nya"
            },
            {
                "nama": "Dhafin Rezaqa Luthhfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "Kakak nya adalah sosok yang penuh integritas.",  
                "pesan":"semangat terus kuliah nya kak"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "12145002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "Kak Mey selalu bisa membuat semua orang di sekitarnya merasa nyaman.",  
                "pesan":"Semangat terus kak kuliah nya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()