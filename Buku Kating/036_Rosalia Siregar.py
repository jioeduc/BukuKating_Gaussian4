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
            "https://drive.google.com/uc?export=view&id=1HUivsFHXM6FKYmyYtsbQ5ivxpzmxaIpm",
            "https://drive.google.com/uc?export=view&id=1qKMDZ0aS9cseL9Tq3GxROs72Vmg564CF",
            "https://drive.google.com/uc?export=view&id=1S1tqUtSU73T6wYmuF9aQd8nhNc5oVieI",
            "https://drive.google.com/uc?export=view&id=1bnJ2NEcsUqJEAtHZ4woplrrFwhdGVd0L",
            "https://drive.google.com/uc?export=view&id=1eJoNIeasbttkgY7iptvu6zyMRToYNIOH",
            "https://drive.google.com/uc?export=view&id=10j9d7wO_DNqgbyuYzlWNmlssP5Ljj_LD",
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
                "kesan": "Abangnya sangat seru diajak ngobrol",  
                "pesan":"semoga lulus tepat waktu"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abang ini membuat suasana jadi menyenangkan",  
                "pesan":"Semoga lulus tepat waktu"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan":"Semoga lulus tepat waktu"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini asik, seru dan baik",  
                "pesan":"Semoga lulus tepat waktu"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini sangat asik",  
                "pesan":"Semoga lulus tepat waktu"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "Kakak ini seru dan asik",  
                "pesan":"Semoga lulus tepat waktu!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fk9ltkHFD2Hg0vFkr4Ty8F91lZOPssOx",
            "https://drive.google.com/uc?export=view&id=1nLYC3-22sBAUmt8wcxCOWx5V6-sn_FCN",  
            "https://drive.google.com/uc?export=view&id=1TM7wZ6xCd4-niA6s7kgubmTQN26rhcbK",
            "https://drive.google.com/uc?export=view&id=1WZDtnkB5a2f8b52V1RYgZVQEO_fO5grf",
            "https://drive.google.com/uc?export=view&id=1K4nagqDkOy0IPvqsQd_vy_Zl5FAhTn7k",
            "https://drive.google.com/uc?export=view&id=1z2hnkOrAHF3yFFrxNdAQGp74WdmmdBDA",
            "https://drive.google.com/uc?export=view&id=1K5HcK3XxYYOC2TurntwIDzjObg845oMF",
            "https://drive.google.com/uc?export=view&id=1rsUOlKpBuRSm8Pj8tDIfrn6yhpXWu1Yh",
            "https://drive.google.com/uc?export=view&id=1U_VPH_42XqtlVy1IvDes_gDCpTr-unn0",
            "https://drive.google.com/uc?export=view&id=1Utl60DK1uJdc6rLTkNVpWAgebPxvBCvZ",
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
                "kesan": "kakak ini sangat aktif sekali dan sangat kiyowoo",  
                "pesan":"semangat kuliahnya kakak dan  selalulah bahagia"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "cantik bangatt",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya kalem dan lucu",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini asik",  
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya keren",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya asikk",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya keren dan asik diajak ngobrol",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "sama kakak  ini seru banget",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak asik dan menyenangkan",  
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini baik dan asik",  
                "pesan":"semangat kuliahnya kakak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OvhdA0v16VUgWEINSJqsT5jM0cqKEvHa",
            "https://drive.google.com/uc?export=view&id=1X-auaP7cmt6uicFvRWjhz-P4LvGUVLQ3",
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
                "kesan": "Kakaknya keren banget dan sangat berkharisma",  
                "pesan":"Semangat kakak dan selalulah bahagia"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "keren banget",  
                "pesan":"Semangat bang kuliahnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1DqKLKB05ihSGLdryi_Pgzp565RR1-xs1",
            "https://drive.google.com/uc?export=view&id=1ml9Npv_okXrnB1-gWqtRquTUjf0WLhyb",
            "https://drive.google.com/uc?export=view&id=1fMWhxzcId0KqzfdHv3tJWNg21QxK_KRc",
            "https://drive.google.com/uc?export=view&id=1oXiUQVJTuJeMZDkaPWIWdypEV_yhk8xr",
            "https://drive.google.com/uc?export=view&id=12F4V3NgmZWteLFhdJhrCLJj7CcDmXS5n",
            "https://drive.google.com/uc?export=view&id=1504K0aX7xBkvUXGqQhnODb7pW1lRaPnZ",
            "https://drive.google.com/uc?export=view&id=1miGvomwyts3n0jq7MqEBA7NxtwfDSMoW",
            "https://drive.google.com/uc?export=view&id=1hkb_wRjy_X6Bhsj462PcxngOhxsTeCA4",
            "https://drive.google.com/uc?export=view&id=1NxfLtUx3K99EkPOYC8ZfDHvqpb7C7zPe",
            "https://drive.google.com/uc?export=view&id=1n0LQjKdtc8frnoDfbdOzXzlaTNVbw-_y",
            "https://drive.google.com/uc?export=view&id=1mw7Hd6sAO6dPcm3Zvw28A1GvL2yqyQ3S",
            "https://drive.google.com/uc?export=view&id=1mcEwe3KAHSgqK3fAgE0Ka-HQswiU6xCd",
            "https://drive.google.com/uc?export=view&id=1myQmbRTO8rYObUb66DGxeo_fBhH5epCX",
            "https://drive.google.com/uc?export=view&id=1mePO-OEc-RzRKzBl9cTQnpT5N5Xw3o3E",
            "https://drive.google.com/uc?export=view&id=1mq_uAAwYKYDrqjvuLyjY7RjNCc_ZNSP4",
            "https://drive.google.com/uc?export=view&id=1eCBN6RtRGVHFdgPfRiSRmxnAbGdPWfDc",
            "https://drive.google.com/uc?export=view&id=1J8PCuCQsF6M0ov8YorruPWdxfaCswAja",
            "https://drive.google.com/uc?export=view&id=1oWBO23KCTW13xtht1lccS3DEo1Sz0Tym",
            "https://drive.google.com/uc?export=view&id=1mTleh-ayTqFwamBVM0NYFZt4xbbhPp6N",
            "https://drive.google.com/uc?export=view&id=1YVKwoEwxVW4bmuLoY7UK_TZ_88TEYMY2",
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
                "kesan": "Abangnya keren",  
                "pesan":"Semangat kuliahnya bang dan semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya asik",  
                "pesan":"Selalulah bahagia kakak"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya seru dan asik.",  
                "pesan":"Semangat kuliahnya kakak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami",
                "kesan": "kakaknya keren dan asik",  
                "pesan":"semangat kuliahnya kak dan selalulah bahagia"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakaknya keren",  
                "pesan":"Semangat terus kuliahnya kak dan semoga sukses dalam segala hal yang diusahakan."
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakaknya keren",  
                "pesan":"Semangat kuliahnya kak "
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
                "pesan":"Semangat kuliahnya kakak dan selalulah bahagia"
            },
            { 
                "nama": " Deyvan Loxefal", 
                "nim": " 121450148 ", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanlo", 
                "kesan": "Abangnya keren",   
                "pesan":"Semangat bang kuliahnya dan semangat boxingnya" 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamy", 
                "kesan": "Kakaknya asik",   
                "pesan":"Selalulah bahagia kakak" 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "Kakaknya keren dan asik",   
                "pesan":"Semangat bang kuliahnya" 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "Kakaknya baik",   
                "pesan":"Semangat kuliahnya bang" 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Kakaknya asik dan keren",   
                "pesan":"Semangat bang kuliahnya" 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya positif vibes banget",   
                "pesan":"Semangat kuliahnya kakak dan selalulah bahagia" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya asik dan baik",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya asik dan seru.",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakaknya baik, asik, cantik, lucu, kalem dan masih banyak lagi",  
                "pesan":"Selalulah bahagia bersama anak Gauss kakak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya asik dan seru",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Semangat terus Kak kuliahnya dan selalulah jadi orang baik"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()


elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pawVPASOaWsQKl-aqnEsadhPnNhf1Xgk",
            "https://drive.google.com/uc?export=view&id=1qNlaCBMFMftuq6O_RdOdSM5P1hgYqKeg",
            "https://drive.google.com/uc?export=view&id=1pZvM-zbkBWlFnIe2K_w13WU4b3nr8uI_",
            "https://drive.google.com/uc?export=view&id=1pOiprU_jVe546XdLeCXjUt6jH4ZZZEeH",
            "https://drive.google.com/uc?export=view&id=1pR7CZpTN2kjzQNvtkCfL3TsgNQZQlgx_",
            "https://drive.google.com/uc?export=view&id=1pSCHt378T8vXU8M3V9HhCdn7rGHMm1ES",
            "https://drive.google.com/uc?export=view&id=1psojHRixkUZTnGqsRHX6o9lqV7H3ILHf",
            "https://drive.google.com/uc?export=view&id=1paMnieXnWFANWJOS2YDv_RAbWOhAeY75",
            "https://drive.google.com/uc?export=view&id=1pyeXJVHw_9kHUQSiJjRO2pLsUuAKtoMT",
            "https://drive.google.com/uc?export=view&id=1pzq4BokWMykEossh5sAqgvLETSyo22to",
            "https://drive.google.com/uc?export=view&id=1q0yvFKRRHA2uGLlBApCtYXYdxqoFASmc",
            "https://drive.google.com/uc?export=view&id=1pLKCekTQY9V9TLoFOS-041L1BVZBHpnv",
            "https://drive.google.com/uc?export=view&id=1q8RVnEa6YtrNp5KHKc-hmMzCEiViro4o",
            "https://drive.google.com/uc?export=view&id=1pUHV1S-EUNoVox6uGtBE86nilwHc5gm0",
            "https://drive.google.com/uc?export=view&id=1pYLpuu2I-bfRy44IbXWjuZ5A4-PZ8FSp",
            "https://drive.google.com/uc?export=view&id=1pz7z5weYdbEPwrIOeLFf3-kAeDRkl52Y",
            "https://drive.google.com/uc?export=view&id=1pUhMjH8JGa9EIxefQ-8vE55Cs_zgPyOo",
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
                "kesan": "Abangnya keren dan asik",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Annisa Novatika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl.Pulau Sebesi, Sukarame",
                "hobbi": "baca novel",
                "sosmed": "@annovavona",
                "kesan": "Kakaknya positif vibes",  
                "pesan":"Selalulah bahagia kakak dan jangan lupa istirahat"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Tidak bisa berkata-kata, keren banget pokoknya",  
                "pesan":"Selalulah  bahagia bersama anak Gauss bang"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya asik",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "Keren bangetttttt",  
                "pesan":"Selalulah menjadi bintang bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Baca novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Semangat terus kakak"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnya keren dan baik",  
                "pesan":"Selalulah bahagia bang"
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "121450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakaknya baik dan positif vibes",  
                "pesan":"Semangat kuliahnya kakak"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya baik",  
                "pesan":"Semangat kuliahnya kakak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya positif vibes",  
                "pesan":"Semangat kuliahnya kakak"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya baik",  
                "pesan":"Selalulah bahagia kakak"
            },
            {
                "nama": "Syahdza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya asik",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhmn_adityaa",
                "kesan": "Abangnya baik dan keren",  
                "pesan":"Semangat kuliahnya bang"
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "Abangnya keren, asik dan baik",  
                "pesan":"Semangat kuliahnya bang dan selalulah bahagia"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya baik  dan seru",  
                "pesan":"Semangat kuliahnya kak"
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "Abangnya baik",  
                "pesan":"Selalulah bahagia bang"
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya asik dan keren",  
                "pesan":"Semangat kuliahnya bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1npTbdo78Gq-JGS6NJUsdyAy2f7uQ4R9s",
            "https://drive.google.com/uc?export=view&id=1npsahfnVGJH3b44_NNOO8iReimMXDn_R",  
            "https://drive.google.com/uc?export=view&id=1o-jRfe5I0Sx3o5o2Q0DgJeGM2BM2QTzW",
            "https://drive.google.com/uc?export=view&id=1oC87ckkP6RBOm3y5T5z33BurAtQCyxzi",
            "https://drive.google.com/uc?export=view&id=1o9tzxL-vTLQTIpY2FBtkxOaf_R7dITxp",
            "https://drive.google.com/uc?export=view&id=1oA5IOAGV0uo7P6PKHdu71bqvZYhK2e0y",
            "https://drive.google.com/uc?export=view&id=1oRwK7rkQu36tONZbNfPZtJ2mAXnODOWX",
            "https://drive.google.com/uc?export=view&id=1p9_hmippF-Lqw6hrjCZ1d92PeoXoFThg",
            "https://drive.google.com/uc?export=view&id=1nzUXNaL1HGuZhDrL0UwliyCJSGcK_Zqo",
            "https://drive.google.com/uc?export=view&id=1ozv1FQWYzUcNBrmkC5BNoZKyh9EFJVyD",
            "https://drive.google.com/uc?export=view&id=1oIObDjcXMljpMIl-oXP0-zMWuuOKFjVb",
            "https://drive.google.com/uc?export=view&id=1oDQKrxRgKGN-4sX3uR6-ag6lqsCdGXYR",
            "https://drive.google.com/uc?export=view&id=1oQJvGRKrAlcGJw0w6OqgqfHW0ZgDpyct",
            "https://drive.google.com/uc?export=view&id=1p5R2-Tf1LpfkBWHCeE6rAoiFHgI2e_8i",
            "https://drive.google.com/uc?export=view&id=1o3kUksnEhKiCa1-RS4yKiYy9Ijdx4c3A",
            "https://drive.google.com/uc?export=view&id=1pGCLP4NWzk15v1dJDPrDIEC-YV2caNe0",
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
                "kesan": "Abangnya baik dan asik",  
                "pesan":"Semangat Kuliahnya bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121400131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya baik dan seru",  
                "pesan":"Semangat Kuliahnya Kakak"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya kalem dan lucu",  
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
                "kesan": "kakak ini asik",  
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
                "kesan": "kakaknya keren!",  
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
                "kesan": "Abangnya asikk",  
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
                "kesan": "Abangnya keren dan asik",  
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
                "kesan": "abang ini seru",  
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
                "kesan": "abang ini asik dan menyenangkan",  
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
                "kesan": "abang ini asik dan seru",  
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
            "https://drive.google.com/uc?export=view&id=1masnxJWaMpY9tL9G5kcav-1dNHSYnUTB",#1
            "https://drive.google.com/uc?export=view&id=1mHlbjMyQgl1-q-1JJTRLR5j2c9bj_VZy",#2
            "https://drive.google.com/uc?export=view&id=1mBW18sY9wu5oiXKg35KXMrg5OMJLOXs8",#3
            "https://drive.google.com/uc?export=view&id=1li47HQx-zb-djPIM2iK5rHwk7f9mQGxd",#4
            "https://drive.google.com/uc?export=view&id=1lrI5EqUvuYp_PL-3HJzbgJQveGFGwCaQ",#5
            "https://drive.google.com/uc?export=view&id=1mNl5-6amVubzt5zXy7qVs_X-9Z7ZW4Zp",#6
            "https://drive.google.com/uc?export=view&id=1mGAfYB_cUlKwSJMQaAXHmFiHeFhDF_o2",#7
            "https://drive.google.com/uc?export=view&id=1m2yq-GpJTe6CIL4tHqirapp5Aoczt5SW",#8
            "https://drive.google.com/uc?export=view&id=1mG1n9P4V1ipyxSpiUd0b7XnbaLAtr9TV",#9
            "https://drive.google.com/uc?export=view&id=1lnCm3obVtySz0UfYTDdIqYxgogFg2BBm",#10
            "https://drive.google.com/uc?export=view&id=1m2z1BwEUldqlqne76shJZLXiOPp0cSCl",#11
            "https://drive.google.com/uc?export=view&id=1mIPmLENxz_6j__dDG5wpzUU9hl4zHFks",#12
            "https://drive.google.com/uc?export=view&id=1ldWxXxGTKSW2wyjlQ8I-A2e6lvmzrrot",#13
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
                "kesan": "Abangnya keren, baik dan sangat berkharisma",  
                "pesan":"Selalulah bahagia bang"#1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@catherine.sinaga",
                "kesan": "Kakaknya baik dan positive vibes",  
                "pesan":"semangat terus kuliahnya kak dan selalulah bahagia"# 2
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "Abangnya keren",  
                "pesan":"Semangat kuliahnya bang"# 3
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakak baik dan ramah",  
                "pesan":"Semangat kuliahnya kak"# 4
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Selalulah bahagia kakak"# 5
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@lexanderr",
                "kesan": "Kakak asik dan seru",  
                "pesan":"semangat terus kuliahnya bang"# 6
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Abangnya keren dan baik",  
                "pesan":"Semangat kuliahnya bang"# 7
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar.resdika",
                "kesan": "Abangnya baik dan keren",  
                "pesan":"Semangat terus kuliahnya bang"# 8
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak baik dan seru",  
                "pesan":"Semangat terus kakak"# 9
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Lihat cogan",
                "sosmed": "@slafhn_",
                "kesan": "Kakaknya keren",  
                "pesan":"Jangan lupa bahagia kakak"# 10
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@ranipuu",
                "kesan": "Kakaknya asik",  
                "pesan":"Semangat kuliah kakak"# 11
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Abangnya keren",  
                "pesan":"Semangat kuliahnya bang"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abangnya baik dan soft spoken",  
                "pesan":"Selalulah bahagia bang"# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ku09OuPaNvSoo9PcPEndwEsJzu3r17Pm",
            "https://drive.google.com/uc?export=view&id=1kR0NX6L_WmXNfCbpq4B96q-fGP0Jg2xX",
            "https://drive.google.com/uc?export=view&id=1kZNCs6UvqPlTNEjJcJwts5-jDue4uCd7",
            "https://drive.google.com/uc?export=view&id=1lUn6XBJJ7_9HI-4DdOCpLl2vc-LsxULz",
            "https://drive.google.com/uc?export=view&id=1lX2D4jWi_ygSg_sFYoYkRSwijGw_pmPN",
            "https://drive.google.com/uc?export=view&id=1lRqsKH-8PkWANQPDp9DZsU6moOBWoSds",
            "https://drive.google.com/uc?export=view&id=1klM4pFpAyInSW1mA0i5ot1xeZLlrBVHl",
            "https://drive.google.com/uc?export=view&id=1kRxst2Go2DuZ1R8u9ioWRAlztk6q-vVX",
            "https://drive.google.com/uc?export=view&id=1lPrpCWZ4hxUud2L0C0s09QTeHzCRa9RH",
            "https://drive.google.com/uc?export=view&id=1kYdb3piTLBA5zcTSEVpWM2t2pp17DZSw",
            "https://drive.google.com/uc?export=view&id=1keHD82nSr88GkeAp0s0BWgGhlnLyPFfY",
            "https://drive.google.com/uc?export=view&id=1l0kCtgTs8sE-Odh7-egg2hnSJai4Oj-C",
            "https://drive.google.com/uc?export=view&id=1kxSYdxgluzMgNK1SPvyWlgo4gDj-yQqk",
            "https://drive.google.com/uc?export=view&id=1lJDg47BLb-LR3qSXGWaGzXUrfHUtbufk",
            "https://drive.google.com/uc?export=view&id=1kOGs6WIXoVjWQ9hU6cAemCMJ3JyeB5tj",
            "https://drive.google.com/uc?export=view&id=1kwmo3nCSUB1KDYnB6VLQRsxZzwG4vJE5",
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
                "kesan": "Abangnya keren",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@Elokviola",
                "kesan": "kakak cantik dan sabar",  
                "pesan":"Selalulah bahagia kakak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat kak kuliahnya"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "Kak cia ceria bgt",  
                "pesan":"Selalulah jadi orang yang ceria kakak"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "Kakaknya asik dan baik ",  
                "pesan":"selalulah jadi orang yang ceria kakak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Semangat kakak kuliahnya dan selalulah bahagia"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Abangnya keren",  
                "pesan":"sSemangat bang kuliahnya"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kakaknya baik",  
                "pesan":"selalulah jadi orang baik kakak"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@aimnn.as",
                "kesan": "abangnya baik dan asik",  
                "pesan":"semangat bang kuliahnya"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "kakaknya baik",  
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
                "kesan": "Kakaknya asik dan  baik",  
                "pesan":"selalulah bahagia kakak"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "-",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@Arsalutama",
                "kesan": "abangnya keren",  
                "pesan":"semangat terus bang kuliahnya"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Abangnya asik",  
                "pesan":"semangat bang kuliahnya"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@akmal.faiz",
                "kesan": "Abangnya baikkk",  
                "pesan":"semangat bang kuliahnya dan selalulah bahagia"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "Abangnya keren dan asik",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kakaknya asik",  
                "pesan":"semangat kak kuliahnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nD_9Yx0IrzKOKVH3ClfFconN8SGFFPrs",
            "https://drive.google.com/uc?export=view&id=1n2vNz_DefJo5DAaq20c6dZiywiCMoTt0",
            "https://drive.google.com/uc?export=view&id=1nRZHw-8szJT7u1Vute-PFa8zF6S_qbxW",
            "https://drive.google.com/uc?export=view&id=1nOwo8mOn1n5ZdpPqkCpKviziyX_Go-wv",
            "https://drive.google.com/uc?export=view&id=1n41-LDLzlGH4H7GkjQ4K50MoJtBrNAJN",
            "https://drive.google.com/uc?export=view&id=1n7q1Bg3vxyqRfZnbX-IOLvH-LoYNwZlc",
            "https://drive.google.com/uc?export=view&id=1n868_u8sWCSziXHw-Ovs27XThrDOJdUJ",
            "https://drive.google.com/uc?export=view&id=1nFRl1AtcGLlQMK5X3lhTcenhINw4l-na",
            "https://drive.google.com/uc?export=view&id=1nUud4nkNo3bI5IOi7BI-BKcYDO7WvamE",
            "https://drive.google.com/uc?export=view&id=1nAoNrxBzh4ZpTvAWYwX8nsFQEzlHnqJF",
            "https://drive.google.com/uc?export=view&id=1nQ39l_RzfL8Po0Mbx9WuLuprm1GuVPY4",

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
                "kesan": "Abangnya seru dan keren",  
                "pesan":"Selalulah bahagia bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto ",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@Adhistysa_",
                "kesan": "Abangnya asik",  
                "pesan":"Semangat terus bang"
            },        
            {
                "nama": "Nabila azhari ",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "Kakaknya seru dan asik",  
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
                "kesan": "Abangnya keren",  
                "pesan":"Semangat selalu bang"
            },
            {
                "nama": "Danang hilal kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Bang danang keren bangatttt",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Salatiga",
                "alamat": "Bogor",
                "hobbi": "Jl.lapas",
                "sosmed": "@farrel__julio",
                "kesan": "Abangnya keren dan asik",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakaniaa",
                "kesan": "Kakaknya baik",  
                "pesan":"Selalulah bahagia kakak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanfir",
                "kesan": "Kakaknya seru dan asik",  
                "pesan":"Semangat kuliahnya kakak"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alfiagntng",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kak dan selalulah bahagia"
            },
            {
                "nama": "Dhafin Rezaqa Luthhfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "Abangnya asik",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "12145002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "Kakaknya keren dan seru",  
                "pesan":"Selalulah bahagia kakak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()