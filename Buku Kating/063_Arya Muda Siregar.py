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
                "sosmed": "@gumilangkharisma",
                "kesan": "Kakak ini asik dan chill",  
                "pesan":"Semangat kuliahnya bang."# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "1214500137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Kakak ini asik banget",  
                "pesan":"Semangat kuliahnya bang."# 1
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
                "nama": "Hartiti Fadhilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kaka ini ramah banget",  
                "pesan":"Semangat kuliahnya kak Hartiti."# 1
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
                "pesan":"Semangat kuliahnya kak Putri."# 1
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
                "pesan":"Semangat kuliahnya kak Nadilla."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HJ-Qh2nevxnHrW1dix-FC5xxDsmYahVQ",
            "https://drive.google.com/uc?export=view&id=1IZpWkd3zLa0PPUINg9E1FGe5uSqq4Gog",
            "https://drive.google.com/uc?export=view&id=1IgBDSi7z2-NSRtuGK5XPE0F7Stc2vg9d",
            "https://drive.google.com/uc?export=view&id=1I6H1gYP5mvHQTmF4p39aoDoXY5YVVDwO",
            "https://drive.google.com/uc?export=view&id=1I4Bl1jtFFq_3uNL7nXin2DDN_PK5Y-Cd",
            "https://drive.google.com/uc?export=view&id=1Gz8wNyEnR5tjfxvDtouZj7ARIpnqhptc",
            "https://drive.google.com/uc?export=view&id=1HkNDNH_ynQiLIcsAYg-s0GpFQtdAldVP",
            "https://drive.google.com/uc?export=view&id=1HsTBX2rXmbxTh5i8SrpC_VlYngeBYNKo",
            "https://drive.google.com/uc?export=view&id=1HzJIHinsazeEhEBEdyDtiBdwc6kMDxy7",
            "https://drive.google.com/uc?export=view&id=1HmQu9aSDsw-MU7RkFmnBPIBV6D4C0Oxm",
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
                "kesan": "Kakak ini baik bangettt",  
                "pesan":"Semangat kuliahnya kak Tri."
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"Semangat kuliahnya kak Claudhea."# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini penuh inspiratif",  
                "pesan":"Semangat kuliahnya kak Dhea."# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak ini santai banget",  
                "pesan":"Semangat kuliahnya bang jer."# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini santai banget",  
                "pesan":"Semangat kuliahnya bang Feryadi."# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini santai banget",  
                "pesan":"Semangat kuliahnya bang Mirzan."# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak ini inspiratif banget",  
                "pesan":"Semangat kuliahnya bang Fahrul."# 1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini ramah sekali",  
                "pesan":"Semangat kuliahnya kak Annisa."# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini penuh motivasi",  
                "pesan":"Semangat kuliahnya kak Berliana."# 1
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
                "pesan":"Semangat kuliahnya kak ANnisa Dini."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()


elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xHc3zuz5LOXZls5ZX8z1zNRXYvEdfX-r",
            "https://drive.google.com/uc?export=view&id=1xNxGeCMDadnrFX__gVCFUjHsScquJzGR",
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
                "kesan": "Kakak ini inspiratif sekali",  
                "pesan":"Semangat kuliahnya kak Luthfi"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "Bang bintang ini inspiratif sekali",  
                "pesan":"Semangat kuliahnya bang Bintang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wd71z5eK27pyOPjYYufO-1MrVqlFOFl9",
            "https://drive.google.com/uc?export=view&id=1wMFJhxD8fcdjnATmGmrZMZZKxBivtuRN",
            "https://drive.google.com/uc?export=view&id=1x529iogooR67FpXUI1GroP3jX12xFnq8",
            "https://drive.google.com/uc?export=view&id=1wigsyNC6xuAcJN-12bg-EeHkpJx_Rp6v",
            "https://drive.google.com/uc?export=view&id=1wRRlBJiwh8xbpTfYJK9DEFNter-oHsWd",
            "https://drive.google.com/uc?export=view&id=1wv1t7L_VZncRlyhirl5YkAH5C6OIjXLK",
            "https://drive.google.com/uc?export=view&id=1wONgogRGCld-dNgGyXDRU1P7o2wwL15G",
            "https://drive.google.com/uc?export=view&id=1wwj0Pu_zBTwBREpLWtC7d_e1dBFb8Iaw",
            "https://drive.google.com/uc?export=view&id=1wOPKRIXm617qGYA_aQpesmn-NL3QCFIO",
            "https://drive.google.com/uc?export=view&id=1weYfeHq72_c667kR-XPQPKV6l2R5LQxJ",
            "https://drive.google.com/uc?export=view&id=1wajjnwlDkS2tIT9OtpzXKUgZ7aqDACVB",
            "https://drive.google.com/uc?export=view&id=1wbmia9ogxJ1e5N3sQB9WVxSOQFORXh52",
            "https://drive.google.com/uc?export=view&id=1wZQ3pOeMbHoKs2dmprX-rueNj3DwzDal",
            "https://drive.google.com/uc?export=view&id=1waNZXB1_BPewURbopqWV7_LTu1w7uRhl",
            "https://drive.google.com/uc?export=view&id=1wgU_5mbUGMwMCcSOckRoCCkXbGiro75B",
            "https://drive.google.com/uc?export=view&id=1wOdwNLTMW-Lyft579EbChQkCBaFnFT-r",
            "https://drive.google.com/uc?export=view&id=1wVlQeCpjxQXu3_jMBelAT5Z8niItT0uH",
            "https://drive.google.com/uc?export=view&id=1wYO4tYaThjcEBDCnh4N50JMaGzTPe6j7",
            "https://drive.google.com/uc?export=view&id=1wVmG5y-IK8URycH-VYqtv0BcPn7mPPTT",
            "https://drive.google.com/uc?export=view&id=1wS9lZxpQEBunL4pqdpGOQqaZSDvEl7Px",
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
                "kesan": "Kakaknya sering berbagi ilmu.",  
                "pesan":"Semangat kuliahnya bang Econ."
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya asik banget.",  
                "pesan":"Semangat kuliahnya kak abet."
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya asik banget.",  
                "pesan":"Semangat kuliahnya kak Fifah."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami",
                "kesan": "kakak ini tegas sekali.",  
                "pesan":"Semangat terus kuliahnya kak Allya."# 1
            },
            {
                "nama": "Ekshanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakanya asik dan suka bercanda.",  
                "pesan":"Semangat kuliahnya kak Eksanty."
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakanyanya asik banget",  
                "pesan":"Semangat terus kuliahnya Kak Hanum."
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya seru banget ",  
                "pesan":"Semangat kuliahnya Bang Ferdy."
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "abangnya asik parah",  
                "pesan":"Semangat kuliahnya bang Der."
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya asik sekali",  
                "pesan":"Semangat kuliahnya Kak Oktavia."
            },
            { 
                "nama": " Deyvan Loxefal", 
                "nim": " 121450148 ", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanloo", 
                "kesan": "Kakaknya asik dan seru banget.",   
                "pesan":"Semangat terus kuliahnya bang de." 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamg", 
                "kesan": "Kakaknya asik banget.",   
                "pesan":"Semangat kuliahnya kak Presilia." 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "Kakaknya asik dan baik.",   
                "pesan":"Semangat terus kuliahnya bang jo." 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "Kakaknya inspiratif.",   
                "pesan":"Semangat kuliahnya bang Kemas." 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Kakaknya asik banget.",   
                "pesan":"Semangat kuliahnya Bang Sahid." 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya asik banget.",   
                "pesan":"Semangat kuliahnya kak Rafa." 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya asik banget.",  
                "pesan":"Semangat kuliahnya bang Farhan."
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya asik dan seru.",  
                "pesan":"Semangat kuliahnya Bang ."
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakak ini baik banget.",  
                "pesan":"Semangat terus kuliahnya daplok Gausss."
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya asik banget.",  
                "pesan":"Semangat terus kuliahnya bang Rafly."
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakaknya baik banget.",  
                "pesan":"Semangat kuliahnya kaka."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vzW6Fs-CkNK965OOVbKqMrfmIj_kef5d",
            "https://drive.google.com/uc?export=view&id=1w3TvejTNKKxBKlAT_lZTjKYTXDFykJMg",
            "https://drive.google.com/uc?export=view&id=1wFB36rQzu_sr1g26JLE9csMJfAlgvJmS",
            "https://drive.google.com/uc?export=view&id=1vpFQ7GonrXVga8G1_QvW-A57XlBUmpFj",
            "https://drive.google.com/uc?export=view&id=1w334UA6XWZYi1nmcGfxiQYwcamN1wf9-",
            "https://drive.google.com/uc?export=view&id=1yUbuAjBC_ORVQwrKSSKds4F6j5Vy202N",
            "https://drive.google.com/uc?export=view&id=1vz45QUQIqpEv2XvSHf2mI0n9V1vPuJZi",
            "https://drive.google.com/uc?export=view&id=1vsBgVQVCS3BR41y5_95Im32ihFt5CeVQ",
            "https://drive.google.com/uc?export=view&id=1w3r0QmrREeGmOZxlOnWhKoAwohMG9F_Z",
            "https://drive.google.com/uc?export=view&id=1w9pvxFWzZcy2wFwdDIoyO7blvrFMzT0k",
            "https://drive.google.com/uc?export=view&id=1wGW35mbUZ54r-3OY3sCH_UsTLZ11M2bO",
            "https://drive.google.com/uc?export=view&id=1w5S5nDPqLxG9bK3NMSL2OnNEYOCGwgFX",
            "https://drive.google.com/uc?export=view&id=1vuepxemHMylAKj8jiQm3rTNNJF6sKoy4",
            "https://drive.google.com/uc?export=view&id=1wIut0luT6_mnCHoCg1f0ZF4dbp3v1f-0",
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
                "kesan": "Abangnya santai dan asik banget",  
                "pesan":"Semangat kuliahnya bang Rafi"
            },
            {
                "nama": "Annisa Novatika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl.Pulau Sebesi, Sukarame",
                "hobbi": "baca novel",
                "sosmed": "@annovavona",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Semangat kuliahnya kak Anova"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang ini baik dan asik parah",  
                "pesan":"Semangat kuliahnya daplok Gauss akuuu"
            },

            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "Abang ini asik banget",  
                "pesan":"Semangat kuliahnya bang Regi"
            },


            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnya asik banget",  
                "pesan":"Semangat terus kuliahnya bang Anwar"
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakaknya baik dan asik banget",  
                "pesan":"Semangat terus kuliahnya kak Deva"
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya ramah banget",  
                "pesan":"Semangat terus kuliahnya kak Dinda"
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini murah senyum banget",  
                "pesan":"Semangat terus kuliahnya kak Eta"
            },

            {
                "nama": "Syahdza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"Semangat kuliahnya kak Puspa"
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhm_adityaa",
                "kesan": "Abangnya seru abis",  
                "pesan":"Semangat terus kuliahnya bang Adit"
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "Abang ini asik banget",  
                "pesan":"Semangat terus kuliahnya bang Eggi"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"Semangat terus kuliahnya kak"
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abangnya chill banget",  
                "pesan":"Semangat terus kuliahnya bang "
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa kerenn banget",  
                "pesan":"Semangat kuliahnya bangg Randa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uXSECXAUTGpqFQxxmkZ1DYI9TG33n0wk",
            "https://drive.google.com/uc?export=view&id=1uH-2GILCY5fgeIP7j5zcbmO8FsUjpMkg",  
            "https://drive.google.com/uc?export=view&id=1tuBhcB_NqaMVgyH94pa8L56ehlf6MLEK",
            "https://drive.google.com/uc?export=view&id=1tqlouvRoNeHUz957CA6vhxJB5FKQzRfo",
            "https://drive.google.com/uc?export=view&id=1u5RunpLjnDLYshBsVvMDmmW1NOdRxEHn",
            "https://drive.google.com/uc?export=view&id=1uD_QRZ-alP1rtAY4UgOuyKJy0cyROL8B",
            "https://drive.google.com/uc?export=view&id=1tnJdabYU8Rz3DFMD0VDPW6WxFIihzePV",
            "https://drive.google.com/uc?export=view&id=1tVBlNCChDUthx0Sc6R7cfRTw1omm4-Bs",
            "https://drive.google.com/uc?export=view&id=1tWXQjtczUhPUb3NpO7T6r5HBzIgIP4Ot",
            "https://drive.google.com/uc?export=view&id=1tjddBTEcPYzVrd0poQYXevuDoka8x9e-",
            "https://drive.google.com/uc?export=view&id=1tWvRHba5KxiPZSNEk1K0wpNktitgx76i",
            "https://drive.google.com/uc?export=view&id=1taN3qz1bpC9P2eYFEVbw258SbepxY99K",
            "https://drive.google.com/uc?export=view&id=1tcAi4RIHQMcAOFlG6RBM3pV-PKxMTBnR",
            "https://drive.google.com/uc?export=view&id=1toSqMFqF8I3fad3ZeYDf7uVclBZjnv-Q",
            "https://drive.google.com/uc?export=view&id=1ttT6N-Uwr_-zn4CIAH2Jqf-gMc55hlQr",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@Yogyyyyyy",
                "kesan": "Bang Yogy asik dan chill parah",  
                "pesan":"Semangat kuliahnya Bang Yogy"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121400131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya ramah banget",  
                "pesan":"Semangat Kuliahnya kakk"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya asik banget diajak ngobrol",  
                "pesan":"semangat kuliahnya kakkk"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kakak ini ramah banget",  
                "pesan":"semangat kuliahnya kakk "
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya murah senyum",  
                "pesan":"semangat kuliahnya kakk"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Bang Tob asik banget diajak ngobrol dan ditanya tanya",  
                "pesan":"semangat kuliahnya bangvTob, sering sering berbagi ilmu "
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya keren parah",  
                "pesan":"semangat kuliahnya bang vIrvan, sering sering berbagi ilmu "

            },
            {
                "nama": "Rizki Andrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abang ini seru banget",  
                "pesan":"semangat kuliahnya bang Rizki"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "abang ini asik banget",  
                "pesan":"semangat kuliahnya bang Arafi"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfaw",
                "kesan": "Kakak ini baik banget",  
                "pesan":"semangat kuliahnya kakak Califia"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "abang ini asik parah",  
                "pesan":"semangat kuliahnya bang Raid"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "17",
                "asal":"Bogor",
                "alamat": "Pemda",
                "hobbi": "Bersholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kakak ini ramah",  
                "pesan":"semangat kuliahnya kak Tria"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak ini asik banget",  
                "pesan":"semangat kuliahnya kakak Alya"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Ening",
                "alamat": "Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini kalem",  
                "pesan":"semangat kuliahnya kakak Asa"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Planning Content",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik sabar banget dan asik",  
                "pesan":"semangat kuliahnya kak Jasmine"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1up1KoDC6X6ivb6_j0AeRuOLqH3yIbvoI",
            "https://drive.google.com/uc?export=view&id=1ufs7CsC3mY8zEzN1icDCkQBZ8o7Ey8KD",
            "https://drive.google.com/uc?export=view&id=1ueywf4cLrUeLAqgH0Q9RrJ3ETHVNbCLe",
            "https://drive.google.com/uc?export=view&id=1ujCk25gOm0L9FWFZtYHtC81XLoxshysx",
            "https://drive.google.com/uc?export=view&id=1uhuiisTyhX0cOdn9dqCCY0_ezJ_IkUlB",
            "https://drive.google.com/uc?export=view&id=1u_BjaUWPiRuHT777xNJUV4N_wN_Uz8Uj",
            "https://drive.google.com/uc?export=view&id=1uu6Zg-00uIdKxMBIRmu-l3Wt0F4G9bLz",
            "https://drive.google.com/uc?export=view&id=1uu6abJnUPprfhyfbQIDcjJA7C4_LoaSS",
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
                "kesan": "Bang Dimas chill banget",  
                "pesan":"semangat terus kuliahnya bang dim"#1
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakak sangat ramah.",  
                "pesan":"Semangat kuliahnya kak Azizah"# 4
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakak ini ramah banget.",  
                "pesan":"Semangat kuliahnya Kak Meira"# 5
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "Abang ini asik banget.",  
                "pesan":"Semangat kuliahnya Bang Akbar"# 8
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Abang ini asik banget",  
                "pesan":"Semangat kuliahnya Bang Renta"# 9
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Lihat cogan",
                "sosmed": "@slwafhn_694",
                "kesan": "Kakak ini ramah banget.",  
                "pesan":"Semangat kuliahnya Kak Salwa"# 10
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Kakak ini ramah banget.",  
                "pesan":"Semangat kuliahnya Kak Yosia"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Bang ini chill banget.",  
                "pesan":"Semangat kuliahnya Bang Rendra"# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vFqyGSS1VcYo8RFZUXM3ea9R0QtAuWQq",
            "https://drive.google.com/uc?export=view&id=1vNSgphFHldtAHhYDYJv_4_Z6fYyZ6CMn",
            "https://drive.google.com/uc?export=view&id=1vWOKXSbWtg0ScQl5NqsZfpkj8xCZqPL2",
            "https://drive.google.com/uc?export=view&id=1va3iuIFS-xxjcm_f7wQvnbzYA7wbexif",
            "https://drive.google.com/uc?export=view&id=1v2PiwXDvEnY9Vx53ylrwkqZhkLUBUo9m",
            "https://drive.google.com/uc?export=view&id=1v53QT5A8X1gN_xvfwN6Nhybszij044eF",
            "https://drive.google.com/uc?export=view&id=1vVHEyK3d0hEXiCKjDkX_h2HEShUA5oyI",
            "https://drive.google.com/uc?export=view&id=1vNDUBrAbDce9I_8zAPeW3qHh97t82jdp",
            "https://drive.google.com/uc?export=view&id=1v8ZZUkxtR71LFoo4cbwj5IxvLeiGf6Hq",
            "https://drive.google.com/uc?export=view&id=1vEMUo3mqi3jnRO_gnEFDG8oz8FcI46f6",
            "https://drive.google.com/uc?export=view&id=1vBuakrrLUsRVe3VUC2QBmIDpJZyHKbDg",
            "https://drive.google.com/uc?export=view&id=1vlolJi23JM11D3e4lRuaHPziD9Ct7NwG",
            "https://drive.google.com/uc?export=view&id=1vggmKvLBXFIw-CaruF_yAiXajcK59i70",
            "https://drive.google.com/uc?export=view&id=1vlVUMhcoOkglafxC3GZ-0vIdbfaBOX3Z",
            "https://drive.google.com/uc?export=view&id=1v50yS9Spkv2AOaTo1m_NQKn4HYwMLX1n",
            "https://drive.google.com/uc?export=view&id=1vdJW_adhK2NtznAa3rA_Vq82QT93Y88E",
        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "",
                "kesan": "kakak ini chill",  
                "pesan":"Semangat kuliahnya Bang Wahyu"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@Elokfiola",
                "kesan": "kakak ramah sekali",  
                "pesan":"semangat kuliahnya kak Elok"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"semangat kak cintya kuliahnya"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "Kak Cia ini asik banget",  
                "pesan":"semangat kuliahnya Kak Cia"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmanellyana",
                "kesan": "Kakak ini asik banget",  
                "pesan":"semangat kuliahnya Kak Rahma"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"semangat kuliahnya kak Try"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Bang Kaisar asik banget",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"semangat kuliahnya kak Dwi"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@gymnn.as",
                "kesan": "Abang ini chill parah",  
                "pesan":"semangat kuliahnya Bang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kakak ini asik banget",  
                "pesan":"semangat kuliahnya kakkk"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@Arsal.utama",
                "kesan": "Abang ini ramah banget",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Abang ini chill banget",  
                "pesan":"semangat kuliahnya bang abit"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmail_faiz",
                "kesan": "Abang ini asik banget",  
                "pesan":"Semangat kuliahnya bang Akmal"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermawan.mnrng",
                "kesan": "Abang ini asik banget",  
                "pesan":"semangat kuliahnya Bang"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"semangat kuliahnya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yAX1N21VSIpAnWj-Ki9LGmGqJ01DL3ZA",
            "https://drive.google.com/uc?export=view&id=1y-_9i9KbchwdYxVQorL8thRhof4XdMPZ",
            "https://drive.google.com/uc?export=view&id=1y4SyqueTPH7c9gghi3fyClVUkVu63Y8h",
            "https://drive.google.com/uc?export=view&id=1xjrsOvaUmsIJo51w2bCpDRpetAlRquPQ",
            "https://drive.google.com/uc?export=view&id=1xRSvZyHwbyThSNh5PkgwwYFpF4lwTgL8",
            "https://drive.google.com/uc?export=view&id=1xf7dRGZ_Vawbm0VOVL4K5rG14tXBnwHW",
            "https://drive.google.com/uc?export=view&id=1y2VPqTdvr1LmJY4cVvNGRgRc2rf4z6tW",
            "https://drive.google.com/uc?export=view&id=1yHgylwaKY3x99TEGr9Yyk30nc0lf9hv6",
            "https://drive.google.com/uc?export=view&id=1yBJjIk-F1q22nwPtueO5KCfGeB6cbvC-",
            "https://drive.google.com/uc?export=view&id=1y7-BjLLm1cjxbVoJeq6hjHteuN3Ym7-4",
            "https://drive.google.com/uc?export=view&id=1yEZSy_IUNDEw2EXMJJCcfr88_lR8ZyRf",
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
                "kesan": "Abang ini asik banget",  
                "pesan":"Semangat kuliahnya Bang"
            },
            {
                "nama": "Adisty Syawalda Arianto ",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@Adhistysa_",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"Semangat kuliahnya kakk"
            },        
            {
                "nama": "Nabila azhari ",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "Kakak ini asik banget",  
                "pesan":"Semangat kuliahnya kak"
            },  
            {
                "nama": "Ahmad Rizqi ",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@Ahmda.riz45",
                "kesan": "Abang ini chill bgt",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Danang hilal kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Abang ini asik banget",  
                "pesan":"Semangat kuliahnya Bang"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "Abang ini asik banget pas ngobrol",  
                "pesan":"Semangat kuliahnya Bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakaniaa",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"Semangat kuliahnya kakk"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanfir",
                "kesan": "Kakak ini baik banget",  
                "pesan":"Semangat kuliahnya kak Nabilah"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alfiagntng",
                "kesan": "Kakak ini asik banget",  
                "pesan":"Semangat kuliahnya Kak Alvia"
            },
            {
                "nama": "Dhafin Rezaqa Luthhfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "Abang ini asik banget",  
                "pesan":"Semangat kuliahnya bang Dhafin"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "Kakak ini ramah banget",  
                "pesan":"Semangat kuliahnya kak Elia"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()