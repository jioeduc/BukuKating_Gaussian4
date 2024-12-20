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
                "sosmed": "@gumilangKharisma",
                "kesan": "Keren banget magang di Telkom",  
                "pesan":"semangat menjalani hari-hari sebagai kahim bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Asik banget abangnya",  
                "pesan":"Spill main gitarnya bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "kakaknya suka makan",  
                "pesan":"semangat menjalani hari-hari sebagai sekretaris umum himpuanan kak"# 1
            },
            {
                "nama": "Hartiti Fadhilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kak titi keliatan pendiem ternyata asik",  
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
                "kesan": "kak putri paling pendiem diantara kesekjenan yang lain",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@nadillaandr26",
                "kesan": "kakaknya keren banget bisa magang di BPS",  
                "pesan":"semangat rapatnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1r5Pr5MOWBl1QGbT0FI1_dffZlPB9jb8-",
            "https://drive.google.com/uc?export=view&id=1WPQDP2x9Id-Ozxrwgf_YV2_0NeNt4Qf4",
            "https://drive.google.com/uc?export=view&id=1jY3oVcLc1UKZlHoSq7mBhn7prZ35IIyT",
            "https://drive.google.com/uc?export=view&id=1RKwOsD6v21cd5qxnQaQ4asCZAzXWU9Ah",
            "https://drive.google.com/uc?export=view&id=1wH5Urtfro4JWx4CMEEcpXHtPTnegSlzw",
            "https://drive.google.com/uc?export=view&id=1zHLSAsph8eOMXdbyp04kQDv--GUUcgR5",
            "https://drive.google.com/uc?export=view&id=1R-EdjpohuRstWF0xERHBQjJAXQy_8gJu",
            "https://drive.google.com/uc?export=view&id=1575tz9JYOkLufxhSVgXh6RhdyKO7hLXL",
            "https://drive.google.com/uc?export=view&id=1YAyY9VeA236ggGcAZI7wEi3ofOAXG6YW",
            "https://drive.google.com/uc?export=view&id=1y119uDgqm4banVxnuBs1BZT4Jl6TZU5l",
            "https://drive.google.com/uc?export=view&id=1CWfLDK9i9P4nTcBciUh5rTRiA79E5_8n", 
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
                "kesan": "suka banget sama public speaking kakaknya",  
                "pesan":"Blackbox AI juga bagus tau kak hehe"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Rumah kakaknya jauh bangett",  
                "pesan":"Semangat baca jurnalnya kak"# 1
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
                "pesan":"spill cara belajarnya dong kak"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "kakaknya lucu mau diajak foto gaya lucu-lucu",  
                "pesan":"semangat bercocok tanamnya kak, jangan lupa dirawat dengan sepenuh hati"# 1
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
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya baik terus friendly abis",  
                "pesan":"harusnya jangan demis dari bph pik-r bang"# 1
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
                "pesan":"jangan lupa kucingnya dikasih makan ya bang"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "bang fahrul sedikit pendiam",  
                "pesan":"jangan terlalu banyak minum kopi bang"# 1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "outfitnya keren banget",  
                "pesan":"jangan lupa sempetin marathon nonton film  kak"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "terlihat ambis",  
                "pesan":"Semangat puasa senin kamis nya kak"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Happy birthday kak, lucu banget wwc pas sama tanggal ultahnya",  
                "pesan":"selamat bertambah usia kak"# 1
            },
        ] 
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1D0msxBt8FaVAJsuVw3goLUXgXSqmprM8",
            "https://drive.google.com/uc?export=view&id=1GCD_SCw795DF0TwE0aBOt6lnfF0-wsy2",
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
                "kesan": "Kakaknya sangat inspiratif",  
                "pesan":"Semangat mewakili suara rakyat sains data kak"
            },
            {
                "nama": "Rian Bintang Wijaya ",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "Abangnya keren banget ikut LKMM-TD",  
                "pesan":"Semangat menjadi next senator bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kiWKQ6sLczifjIcbPvrZdN1FMQwLIXaS",
            "https://drive.google.com/uc?export=view&id=1UxBaE3IhoNyp9exa9eRf9bXXNHxkCqHV",
            "https://drive.google.com/uc?export=view&id=1dAIraPuh-CpfZEV69Z5TeSKG36FRoDp1",
            "https://drive.google.com/uc?export=view&id=1owz15WKIVAopULNDbcNIOODVyabhIJx-",
            "https://drive.google.com/uc?export=view&id=1oY1RrUN4go2giXlneIL4Y-eyH1ycl975",
            "https://drive.google.com/uc?export=view&id=1AkIqPxuTA99tHg92iwL0Zq5Eb5U5WDpe",
            "https://drive.google.com/uc?export=view&id=1M52Th2fy-l8ViuH7j40CdFt07FVSFXub",
            "https://drive.google.com/uc?export=view&id=1T_wVbHXFW86pDgdly4Qk0bA0vftz8jaH",
            "https://drive.google.com/uc?export=view&id=1J8tw379geI5e74JlD9SkRwYx-xYh-GYD",
            "https://drive.google.com/uc?export=view&id=1D3NQ_Gaibl0KtkQMA5yB2sFiulyQnaq7",
            "https://drive.google.com/uc?export=view&id=19FN8rUoYBnCr-C-x9V4sulU9RTHJ1iHf",
            "https://drive.google.com/uc?export=view&id=1kik7TRuBXsV-mP2pPum3pSIZKYSGZeBB",
            "https://drive.google.com/uc?export=view&id=1b0Zp_xJRVvlnT3FLJFuNDN2jd_C4oAhA",
            "https://drive.google.com/uc?export=view&id=1sxA585_pUEBwQR5a_7ML-5QCEYD7qBL_",
            "https://drive.google.com/uc?export=view&id=1JWjswR7H6Dc_myAWO1kdytUO4G8T5jHo",
            "https://drive.google.com/uc?export=view&id=1c78nzHYxVfNN7ArVWkXIOXp74vj6FJNY",
            "https://drive.google.com/uc?export=view&id=1S-2uzuWbqPYU1HMvXUMQMIWELAC4x7g3",
            "https://drive.google.com/uc?export=view&id=15frcLEiWrge7zDvZ3FMVVNW8oGTfU5pu",
            "https://drive.google.com/uc?export=view&id=1a3FVDb8I_9TeT4iwtR0awplUmWj5yujF",
            "https://drive.google.com/uc?export=view&id=1V-Jn2z2g1yUjbSw78Vgln-eaGjw9eQV8",
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
                "kesan":"Cara berpikir abangnya kritis banget",  
                "pesan":"Semangat menjadi Kadep PSDA nya bang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya seru terus keren banget jadi Sekdep PSDA",  
                "pesan":"Jangan lupa terus semangat bernafas kak"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya keren banget bisa jadi ketuplak kader",  
                "pesan":"Semangat terus kak dan stay kiyowo"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami",
                "kesan": "kakaknya asik dan sangat profesional",  
                "pesan":"jangan lupa istirahat dan banyak minum air mineral kak"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakanya asik dan pinter bangett",  
                "pesan":"Jangan sering-sering nitip sholat ya kak hehe"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakanyanya keren jadi bendahara kader",  
                "pesan":"Jangan minum kopi terus ya kak, air mineral lebih sehat"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "121450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya keliatan serius banget",  
                "pesan":"Spill playlist nya dong bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "121450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "abangnya asik dan enak diajak ngobrol",  
                "pesan":"Jangan lupa hapalin love language bang"
            },
            {
                "nama": "Oktavia Nurwinda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya keliatan pendiam tapi baik",  
                "pesan":"Makasi ya kak kontrakannya sudah boleh dipake kumpul magang terus"
            },
            { 
                "nama": " Deyvan Loxefall", 
                "nim": " 121450148", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanloo", 
                "kesan": "Abangnya lucu bisa boxing",   
                "pesan":"Semangat terus dan tetap happy kiyowo bang" 
            },
{ 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamg", 
                "kesan": "Selera musiknya keren",   
                "pesan":"Pliss spill playlistnya kak, penasaran soalnya" 
            },
{ 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjnnn", 
                "kesan": "Jago banget main basketnya",   
                "pesan":"Semangat jadi aspraknya bang" 
            },
{ 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "Sangat terlihat jago ngoding",   
                "pesan":"Cobain main monopoli digital bang, ga kalah seru" 
            },
{ 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Abang asik dan enak diajak ngobrol",   
                "pesan":"Semangat terus membangun band data bang" 
            },
{ 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "Belwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya seru dan cantik cuma agak pendiam aja",   
                "pesan":"Spill webtoon yang seru kak" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Bang ateng baik terus keren kalau lagi dampingin lomba",  
                "pesan":"Semangat dampingin peserta lomba"
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya terlihat pendiam",  
                "pesan":"Seimbang banget ya bang antara belajar dan main game nya"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "121450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "positive vibes sekalii dan sangat mengayomi anak gauss",  
                "pesan":"Sehat-sehat mamah gauss"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya terlihat sangat suka games",  
                "pesan":"jangan lupa belajarnya seimbang sama main game nya ya bang"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Baru sadar kakaknya kembar hehe",  
                "pesan":"Spill cara bedain kakak sama kak andina dong"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xyOUyzcf22Cb5l7Fc14tSAXWjlLJLxSb",
            "https://drive.google.com/uc?export=view&id=1bTEnfxldxqSHSzV43hR_TX2Cfrht8LVe",
            "https://drive.google.com/uc?export=view&id=16AGQFEEpYIBSASFdy171c7o1yBBQ_FqI",
            "https://drive.google.com/uc?export=view&id=1gpXEqBVrg4lXZxMOjtTTw7uj54bJWyOd",
            "https://drive.google.com/uc?export=view&id=1Paup03oqOT8knoYr5UHQtk1WqT7aS0rn",
            "https://drive.google.com/uc?export=view&id=1lo8stfgkjdAB7e7zoN122nfRQMfyK8CZ",
            "https://drive.google.com/uc?export=view&id=1SSYWZbW1OwHoozdz7i2AGbrsNMFl3dVy",
            "https://drive.google.com/uc?export=view&id=1kzOlQh6cCS5mGaM1pDEpMJif6e7jv6Bm",
            "https://drive.google.com/uc?export=view&id=1BtRSaTOXOu6WB_kjjZ_ZkX89QA1f8d8x",
            "https://drive.google.com/uc?export=view&id=1wKOyHr2U9qDDkvoios2F66P5uHFtHcdx",
            "https://drive.google.com/uc?export=view&id=1HODOciaTl7Hkq9mBZNWSHrt5obiNnPqd",
            "https://drive.google.com/uc?export=view&id=1ZeRGf43X8aHZGk8mLGZokVXcyEwVQVdr",
            "https://drive.google.com/uc?export=view&id=1ZZxNFCoYLaS36hCUsnLKEdnpL9adEFWP",
            "https://drive.google.com/uc?export=view&id=1jns94oxT4KNMDByKChWFIcSdqFqtvbLK",
            "https://drive.google.com/uc?export=view&id=1Ui7a6gRaUX_TFpjfj8SqsQDKj6xw53l-",
            "https://drive.google.com/uc?export=view&id=1niCXWr4b5CvV9WsfyfL95ETJmQ2drE_X",
            "https://drive.google.com/uc?export=view&id=1gYsNWe8TCxwByuek17e5ZC0FbdWxLN7w",
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
                "kesan": "Jago banget badminnya",  
                "pesan":"Semangat latihan badmin buat perlombaan berikutnya bang"
            },
            {
                "nama": "Annisa Novatika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl.Pulau Sebesi, Sukarame",
                "hobbi": "baca novel",
                "sosmed": "@annovavona",
                "kesan": "Suka banget sama vibes kakaknya",  
                "pesan":"Semangat jadi Sekdiv nya kak"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Bang sahid peduli bangett",  
                "pesan":"Semangat menemani anak-anak Gauss bang"
            },

            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Outfit abangnya keren",  
                "pesan":"abangnya tinggi bangett"
            },

            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "Aura duta nya sangat terasa",  
                "pesan":"Semangat menjalankan tugas sebagai duta bang"
            },

            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Baca novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Awalnya bingung ternyata kembar",  
                "pesan":"Spill cara bedainnya kak"
            },

            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@her.iam.ai",
                "kesan": "Abangnya terlihat pendiam tapi lucu",  
                "pesan":"Spill tiktok yang sering di tonton bang"
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "121450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "kak deva positive vibes banget terus keliatan asik",  
                "pesan":"Spill dong kak flim yang seru"
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Keren banget hobinya belajar",  
                "pesan":"Semangat belajarnya kak"
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya positive vibes bangett",  
                "pesan":"Semangat jadi aspraknya kak"
            },

            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak rut terlihat introvert",  
                "pesan":"Spill bacaannya dong kak"
            },

            {
                "nama": "Syahda Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kak puspa baik bangett terus welcome banget sama orang baru",  
                "pesan": "Semangat menjadi daploknya kak"
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhm_adityaa",
                "kesan": "Abangnya cakep",  
                "pesan":"Totur ADS dong bang"
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "Abangnya tinggi sekali dan ramah banget",  
                "pesan":"Semangat bang larinya"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya cantik dan lucu",  
                "pesan":"Spill drama yang seru bang"
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "Bertemu lagi dengan abang asprak",  
                "pesan":"Spill game yang seru bang"
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa keren bangett",  
                "pesan":"Semangat membantu warga Gauss"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ficuxH4qYTpSWpLC3xE3ojuyg66YZTh-",
            "https://drive.google.com/uc?export=view&id=1QMXLMD42Cy9Xg7ZqYy5NetHQ2lYl1Ux6",  
            "https://drive.google.com/uc?export=view&id=1XjHyNhSPp9tVBEZt7Faej-FeoJgSHbV9",
            "https://drive.google.com/uc?export=view&id=1SQPnNY_4mgnVIn9KRVXm3sLNrtMsjzG8",
            "https://drive.google.com/uc?export=view&id=1O8Xd_W4I-kPU8f5BE8TMSv1b7eGYGWfK",
            "https://drive.google.com/uc?export=view&id=1rL6SeA1tdasUiORBayj97M9KhBHWkRL7",
            "https://drive.google.com/uc?export=view&id=1m1rmtV2mTQmX7T7CMA-uCV0FEksbgX0W",
            "https://drive.google.com/uc?export=view&id=1rxLqQreC68Ilzyac___OGjiWX4qB_AH2",
            "https://drive.google.com/uc?export=view&id=1sL8vVBPq0kBLdotxI4a1pWSGkrlSnRQa",
            "https://drive.google.com/uc?export=view&id=1wC0PnxBZBAMnWR-FKk3cmWjEY8B8pSSP",
            "https://drive.google.com/uc?export=view&id=1uA-Jug1N_e3gOYQiK_lU2N9E4diAPEys",
            "https://drive.google.com/uc?export=view&id=1sWOHNbELY3yblXmCDZeT2pNzFhgnPFG-",
            "https://drive.google.com/uc?export=view&id=1N7jFBMNUfA4nMrJMWp7h3uuh8M-rNeYr",
            "https://drive.google.com/uc?export=view&id=10VMJaQpHFkcEPuIFjTeRXXlw4TH8YC1r",
            "https://drive.google.com/uc?export=view&id=1QJyCFxkIL9oJHQEdYZ6loN3TeVy1_LjW",
            "https://drive.google.com/uc?export=view&id=19g76GxnG-TRKPUnbFW6OTvXMx7Cn09IP",
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
                "kesan": "Abangnya terlihat banyak banget pengalamannya",  
                "pesan":"Semangat menjadi Kadep nya bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121400131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya sangat baik",  
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
                "kesan": "Kakaknya lucuu",  
                "pesan":"semangat kak ditunggu publikasi jurnalnya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kakaknya asik dan seru",  
                "pesan":"spill jurnal yang udah terbit dong kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya keren dan positive vibes bangett",  
                "pesan": "semangat kak jangan tidur terus hehe"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Rambutnya bagus bangett",  
                "pesan":"semangat kuliah dan menjadi caponya bang"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang Irfan vibes anak baik banget",  
                "pesan":"spill chanel yt yang seru bang"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abangnya cakep hehe",  
                "pesan":"semangat menjadi staff ekternalnya bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@rafiramadhanmaula",
                "kesan": "Vibes abangnya good boy banget",  
                "pesan":"semangat menjadi staff pengmasnya bang"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfaw",
                "kesan": "Kakaknya positive vibes banget terus lucuu",  
                "pesan":"semangat terus untuk berbuat baiknya kak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "bang raid vibesnya mirip ariel 23",  
                "pesan":"semangat ikut seminarnya bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "17",
                "asal":"Bogor",
                "alamat": "Pemda",
                "hobbi": "Bersholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya yuna aktif banget kegiatan",  
                "pesan":"semangat menjalani banyak tanggung jawab kak"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakaknya  lucu dan cocok banget di pengmas",  
                "pesan":"Semangat belajar tilawahnya kak"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya kalem dan unik",  
                "pesan":"semangat cari ice breakingnya kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Planning Content",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya positive vibes bangett",  
                "pesan":"semangat menjalani kegiatan yang banyak itu kak"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Main Volly",
                "sosmed": "@@izzalutfiaa",
                "kesan": "Kakak asik dan baik bangettt",  
                "pesan":"ayo main volly bareng kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14k7yOupFQ_UGV9A0mgd-jzUv6ozRNlWl",#1
            "https://drive.google.com/uc?export=view&id=1p1gHK2noGwnTU6vCBMGIfQw7u9JimwSf",#2
            "https://drive.google.com/uc?export=view&id=1UzdXb1QW-ddYP3UWXxiuBMRapBP_lvJS",#3
            "https://drive.google.com/uc?export=view&id=1fBzRyIiNSDqTAJpbaElgKXZXgo9F0xb7",#4
            "https://drive.google.com/uc?export=view&id=1uSPLUzV4v6aCdiDIjjG_7_UniT3nIQKI",#5
            "https://drive.google.com/uc?export=view&id=1SgwB1uxQczoOQVdf-LnLpIH3jTDaf_EY",#6
            "https://drive.google.com/uc?export=view&id=1DWudfaR2it2ykP2-9gm_un6EWStkgYSr",#7
            "https://drive.google.com/uc?export=view&id=1R3itnXDe1GJ3NjkC1qT7xHSXjo0cRCsL",#8
            "https://drive.google.com/uc?export=view&id=1nq3iXvyaMQ4UbWGEJq4pvP0rzuRBUdWK",#9
            "https://drive.google.com/uc?export=view&id=1beFR9TIv9ZwptWSsWQoDrfzX2opglnUY",#10
            "https://drive.google.com/uc?export=view&id=1j-nwoJ9ASgoZMazKMji6TrYSiSmf9sC9",#11
            "https://drive.google.com/uc?export=view&id=1f5sCm59OFEqugd6yzPrB_0sWkeY-2aqx",#12
            "https://drive.google.com/uc?export=view&id=1anQ7hOyK3CedKvlOden08M_TeeuL59fv",#13
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
                "kesan": "bang dimas sangat ekstrovert",  
                "pesan":"hati-hati bang kalau manjat tower sutet"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@catherine.sinaga",
                "kesan": "Kakaknya positive vibes banget",  
                "pesan":"baca tere liye kak, bagus-bagus"# 2
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "Abangnya terlihat introvert",  
                "pesan":"Semangat bang olahraganya"# 3
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakaknya ramah bangett",  
                "pesan":"Semangat berkebunnya kak, ditunggu hasil kebunnya"# 4
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakaknya baik banget cuma kaya agak pendiem",  
                "pesan":"Semangat kak, jangan terlalu sering halu hehe"# 5
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya seru dan asik",  
                "pesan":"next time perform nyanyi di FG bang"# 6
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Abangnya baik cuma agak pendiam",  
                "pesan":"jangan lupa cupangnya dikasih makan bang"# 7
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "Abang iimut mukanya baby face",  
                "pesan":"awas di gigit dino bang"# 8
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya keliatan friendly",  
                "pesan":"Spill tempat mancing yang enak kak"# 9
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Lihat cogan",
                "sosmed": "@slwafhn_694",
                "kesan": "Kak Salwa positive vibes banget",  
                "pesan":"next time kalau liat cogan ajak-ajak kak"# 10
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@ranipuu",
                "kesan": "Kak rani vibesnya keren bangett",  
                "pesan":"Ayo kita ngaji bersama kak"# 11
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Abangnya mirip nim 001 di angkatan 23",  
                "pesan":"Semangat bang bawa motornya"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abangnya seru dan asik bangett baik banget juga waktu jadi asprak",  
                "pesan":"Spill lagu yang udah ditulis dong bang"# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lj_LGp6dk3pX45J99HYgyMVlkKXe8oKJ",
            "https://drive.google.com/uc?export=view&id=1vTPLpz1MOD0M1tNq_dtDcHXJtoMISxi_",
            "https://drive.google.com/uc?export=view&id=11J3i8A4pCsYooH4eXpi6NaRjIbFcFnd4",
            "https://drive.google.com/uc?export=view&id=1zkGR0qhgPf4cuL6EujknxinRScYAttZ6",
            "https://drive.google.com/uc?export=view&id=1yFoLK3Lsm23fv4WoR4_wvvh_YOmLWMa_",
            "https://drive.google.com/uc?export=view&id=1AkQKXrkVNRk615AqZZOVOOIq_J0bQQFr",
            "https://drive.google.com/uc?export=view&id=1pipb0-XYr1Sbvqe1dOUeuA0T5gajk3cL",
            "https://drive.google.com/uc?export=view&id=1KU78iQB5U1eYQlj4CqmCcTm2Hq6ckZL9",
            "https://drive.google.com/uc?export=view&id=1wnCSSBnKOZS5tmwtEIhAK-1HdcF2FdMR",
            "https://drive.google.com/uc?export=view&id=1Bd9yNb3Kt5dynO9GaDUKwuWnw6dgdzBp",
            "https://drive.google.com/uc?export=view&id=11MKn3sPAHOBzhf6h-A1e3WHtWwYApSOu",
            "https://drive.google.com/uc?export=view&id=1-OQBdr4jiM2QfnVBXs18-KBX49h7SLCf",
            "https://drive.google.com/uc?export=view&id=1w30R6ti-6H748QBTaqapQEqosxd0D_3k",
            "https://drive.google.com/uc?export=view&id=1G3QGssyvM9efg_mx7NEie9cpUwhGA0Kq",
            "https://drive.google.com/uc?export=view&id=19zkt_iOZfGpI0zGG8c4AozRO50X9EiTc",
            "https://drive.google.com/uc?export=view&id=1qQJnpaWiNkUUj5wrXxSeBu4_AIzJG5HF",
        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "wahyudnt_0202",
                "kesan": "Abang ini asik sekali",  
                "pesan":"Spill movie yang bagus bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@Elokviola",
                "kesan": "kakaknya cantik bangett",  
                "pesan":"semangat ngeditnya bang"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Suka banget sama make-up kakaknya",  
                "pesan":"semangat ngegym nya kak"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "Kak cia lucu sama asik bangett",  
                "pesan":"Semangat kepanitiannya kak ciaa"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "Kakaknya asik dan seru",  
                "pesan":"jangan makan geprek terus kak, ayam bakar juga enak kok"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "Kak cia cantik banget",  
                "pesan":"semangat buat kontennya kak"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Abangnya baik dan asik",  
                "pesan":"semangat nyari hobinya bang"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kakaknya keliatan kalem dan pendiam",  
                "pesan":"semangat terus kak jangan lupa dengerin maliq"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Buzzcut",
                "sosmed": "@aimnn.as",
                "kesan": "Bang gym baik bangett cuma waktu marah agak serem ya",  
                "pesan":"semangat nyari tuyul nya bang, kabarin kalau dapat"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "kakaknya asik dan seru",  
                "pesan":"tips cara semangat buat bersih-bersih dong kak"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakaknya baik dan keliatan positive vibes",  
                "pesan":"ikut lomba kak biar hobinya tersalurkan"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@Arsalutama",
                "kesan": "Abangnya baik banget dan vibesnya good boy abis",  
                "pesan":"spill parfum yang enak wanginya bang!"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Abangnya baik bangett dan keliatan peduli banget",  
                "pesan":"gass main uno bareng bang!"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@akmal.faiz",
                "kesan": "Bang akmal baik banget terus lucu",  
                "pesan":"tips belajarnya bang biar walaupun hobi tidur tapi piter!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "Abangnya seru dan asik cuma agak jahil",  
                "pesan":"semangat terus bang jangan bengong teruss!"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kakaknya baik bangett terus positive vibes banget",  
                "pesan":"Jangan lupa diberesin ya kak kamarnya haha!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y0tFq7HecSSnGHDk5nDLmS26mbaug_MY",
            "https://drive.google.com/uc?export=view&id=1JjxICmYHmqkhfHKmmAn4PN1ulkuP2e0Q",
            "https://drive.google.com/uc?export=view&id=1CCVlDpVoCo0Pj9MKg4htSvM4heir0QWe",
            "https://drive.google.com/uc?export=view&id=1gm7UVvbTkvf5ppPdcSKvzaUjCDBqryKn",
            "https://drive.google.com/uc?export=view&id=1MpnShddNiMnnCBH4ZtjKrmIoZ5l6sZNj",
            "https://drive.google.com/uc?export=view&id=14MAlXYl-nqMUqHb6TPF_pmJ3KyGcuPBq",
            "https://drive.google.com/uc?export=view&id=1w5FpuCBEn60aE6qkgrli0HqZB-EmKhjl",
            "https://drive.google.com/uc?export=view&id=1icx9se9iN6WECi_voFjxKjMccVff4VGM",
            "https://drive.google.com/uc?export=view&id=1Vw4rlVBKWbpB9jjUB973R8h2WIXWCLDS",
            "https://drive.google.com/uc?export=view&id=13ldQjRhjNumFMkn7pHL81ZPUerYNQ6y4",
            "https://drive.google.com/uc?export=view&id=1Fjv0Mxy_eR6_xj478bIDy8ukppQ2UNG5"
        ] 
        
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol ",
                "nim": "121450090",
                "umur": "20",
                "asal":"Cirikalang",
                "alamat": "Dekat penjara",
                "hobbi": "Nyari hobi",
                "sosmed": "@Andrianlgaol",
                "kesan": "Abangnya asik dan keliatan banyak banget pengalamannya",  
                "pesan":"Semangat bang nyari hobinya"
            },
            {
                "nama": "Adisty Syawaida Ariyanto ",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@Adistysa_",
                "kesan": "Kakaknya cantik dan keliatan asik",  
                "pesan":"Spill film yang bagus kak"
            },        
            {
                "nama": "Nabila azhari ",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "Kakaknya asik dan cantik",  
                "pesan": "Semangat ngitung duit nya kak"
            },  
            {
                "nama": "Ahmad Rizqi ",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@Ahmda.riz45",
                "kesan": "Abangnya baik dan vibes anak pinter banget",  
                "pesan":"Semangat main badmin nya bang"
            },
            {
                "nama": "Danang hilal kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Abangnya asik dan baik",  
                "pesan":"Ditunggu stiker pandanya bang"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat menjadi capo nya bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakanias",
                "kesan": "Kakaknya baik dan positive vibes banget",  
                "pesan":"Semangat menulisnya kak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanfir",
                "kesan": "Kakaknya sangat inspiratif",  
                "pesan":"Semangat mengejar gelar duta-duta yang lainnya kak"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alviagnting",
                "kesan": "Kakaknya baik cuma keliatan pendiam",  
                "pesan":"Semangat belajarnya kak jangan lupa marathon film biar tetap waras"
            },
            {
                "nama": "Dhafin Rezaqa Luthhfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "Abangnya keliatan pendiem",  
                "pesan":"Semangat Olahraganya bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "Kak mey cantik terus senyumnya manis",  
                "pesan":"Semangat teruss kakk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()