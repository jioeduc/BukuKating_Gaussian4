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
            "https://drive.google.com/uc?export=view&id=18rYWEB2lO2pdRpbCl8Gk84gYpBz2vrTH",
            "https://drive.google.com/uc?export=view&id=18rMTUQfS01x5t60bg-jC32lnst-U8vAm",
            "https://drive.google.com/uc?export=view&id=18n5PRfkmOD6sF8kEMEKdFOMFmVfz-1Tx",
            "https://drive.google.com/uc?export=view&id=191jWPD0TpG4bWqmJtsDgY1fejW2VBW2a",
            "https://drive.google.com/uc?export=view&id=18uc6r3z6piCwlfuIQwUkwsuD55PsYXMm",
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
                "kesan": "keren bang gumi, tetaplah menyala",  
                "pesan":"semangat bang gumi, kalo dah kerja info loker ya bang, wkwk"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "bang pandra kece betull, teruss senyumnya maniss",  
                "pesan":"Semangkat kuliah dan TA nya semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kak melizaa lucu bgtt",  
                "pesan":"Semangat untuk TA nya kak semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak seru dan asik banget diajak ngobrol",  
                "pesan":"semangat untuk segala hal kakak"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "uni yang kece, dan manis banget",  
                "pesan":"semangat uni, semoga lulus tepat waktu!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18H9RoOq_Cx73ePKwGXgjJy7iR48n3N5K",
            "https://drive.google.com/uc?export=view&id=18WjxfUd_qKIIJfTtAdysthVT0PYJlZI2",
            "https://drive.google.com/uc?export=view&id=18gjYXoIdfHxzr_qt-gTp87l0TFbR3uDD",
            "https://drive.google.com/uc?export=view&id=18WP2ZezxZEKDkCKxf4VVT4lHoZ92-yO5",
            "https://drive.google.com/uc?export=view&id=18gGL5qqEh7B_5eJeSuUYYtRyo6GfGsvy",
            "https://drive.google.com/uc?export=view&id=183FhdLvGW4xTiDyzDzerdWPH1ytzI4p2",
            "https://drive.google.com/uc?export=view&id=18dAEr-Zj6NLulTETarvcsThUSSn-gwkX",
            "https://drive.google.com/uc?export=view&id=18ZiOr_fof0k6UKfTfoemtieFTveRT6MH",
            "https://drive.google.com/uc?export=view&id=18Eewr3JZELdaRxMln-l_f3YE-ncdyufB",
            "https://drive.google.com/uc?export=view&id=187A1CN_DQUa3bsI_ewZw2V78aeAGEXfT",
            "https://drive.google.com/uc?export=view&id=18IgsnfgROYPkDby7rQuR1txcmek0R8Nk",
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
                "kesan": "Kakak tri positive vibe terus asik babngett diajak ngobrol",  
                "pesan":"semangat kakaaa loveyouu"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakak kece bgtt",  
                "pesan":"tetap jadi orang baik yaa kak"
            },
             {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Salah",
                "hobbi": "belajar, nonton film,tidur",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak wulan keren bgt postive vibes and ambis banget lohh",  
                "pesan":"keep smile dan moga lancar luncur untuk semua kegiatannya kak"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "mantap betull kak dhea seru amay",  
                "pesan":"semangat menjalani kuliahnya kakak"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang nya chill banget dan asik",  
                "pesan":"semangat bang buat panit dan kuliahnya"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya keren betulls",  
                "pesan":"semangat terus kuliahnya abangku"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Paling kece dan ganteng bgt hshshs",  
                "pesan":"banyakin senyum yaa bang"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang stylenya kece ",  
                "pesan":"semangat bangg kuliahnya dan stay healty"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kak Nisa kece parrrah",  
                "pesan":"semoga dimudahkan untuk seluruh perkuliahannya yaa kak"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya seru uy dan asik pembawaannya",  
                "pesan":"semangat menjalani hari harinya kaka"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini asik sekali",  
                "pesan":"semangat terus kuliahnya kakak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AZ6EwOUDV0Xxa1sON6nU8H6_zDPCjRZq",
            "https://drive.google.com/uc?export=view&id=1AXej5aW4tR7vorHCG68JQLeQAmIUzpSg",
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
                "kesan": "kakanya asik buat diajak diskus",  
                "pesan":"Jangan lupa sampaikan aspirasi kami kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Percaya gak percaya, Bang Bintang supportif orangnya",  
                "pesan":"Tetep jadi orang baik bang dan sampaikan aspirasi kami yaa bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
          "https://drive.google.com/uc?export=view&id=1AFombiUvKyrCSATvTC5I5pcDH9qGV5vi",
          "https://drive.google.com/uc?export=view&id=1A7UNckLgPV7ahJvGzdxY3I5mzF2JEyN8",
          "https://drive.google.com/uc?export=view&id=1APZb_z-lF-FrvbimzowiKw6rRo67_01O",
          "https://drive.google.com/uc?export=view&id=1AHAMhNZJN1UN5DA6v1vsAZwxLtlVdbsl",
          "https://drive.google.com/uc?export=view&id=19ywxuV6jhWzRtFTkI7S5hYQGtkyt78Fu",
          "https://drive.google.com/uc?export=view&id=1ASILNlxvNXueZWaQe6oFv1bpL_KPNped",
          "https://drive.google.com/uc?export=view&id=1A7FMKlXe8WWjiIdTaTj8nAPuKP1y5zC0",
          "https://drive.google.com/uc?export=view&id=1AKeU1C7wmE8piKPcSkYp51ODrySKfUHp",
          "https://drive.google.com/uc?export=view&id=1A5NjehETPuS215nXLnfFDe5zV97BjG1R",
          "https://drive.google.com/uc?export=view&id=1AF_alIzQvwgekMuw6wrmdz_b7wiiMHTE",
          "https://drive.google.com/uc?export=view&id=1AFT426Io7b4JHmy9uwq8VN1NHtyxngdD",
          "https://drive.google.com/uc?export=view&id=19zNvUIiHyRlWebzXs5U1Z5PgegAbq0az",
          "https://drive.google.com/uc?export=view&id=1ADET6vp_-GmgaEQ9iRWrXJL0pKwxZiqe",
          "https://drive.google.com/uc?export=view&id=19zf-7Tx0UPViwHTaicZ63lhQFkTY2W4F",
          "https://drive.google.com/uc?export=view&id=1AGjpVwuxwAVy5rZ_SzMTSGk48xu4Zgcr",
          "https://drive.google.com/uc?export=view&id=1A9GWZRMVES3j1uPZNFGNYvH_Oypy18cJ",
          "https://drive.google.com/uc?export=view&id=1A25pNcYbfhmuVKOC0L3hdojFD1foDkX6",
          "https://drive.google.com/uc?export=view&id=1A9GWZRMVES3j1uPZNFGNYvH_Oypy18cJ",
          "https://drive.google.com/uc?export=view&id=1A3NuoOcjkt_15UZ0_sEOuB166JirrWG1",
  
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
                "kesan": "menyala abangku, abang keliatan wibawa bgt",  
                "pesan":"Semangat terus ngurusin sumber daya manusia HMSD bang."
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya asik.",  
                "pesan":"Terus semangat kuliahnya Kak dan semoga berhasil dan sukses meraih cita-cita."
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "namanya sama kayak aku hehe, cantik banget kak",  
                "pesan":"semangat untuk mengemban tugasnya kakak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami_",
                "kesan": "kak alya keren dan wajahnya kelihatan positif vibes .",  
                "pesan":"semangat terus kak kuliahnya dan sukses mencapai apa yang diinginkan."
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakanya chill dan seru bgtt.",  
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
                "kesan": "kakanya manis terus namanya juga kembar 3 kita hehe",  
                "pesan":"Semangat terus kuliahnya kak dan sukses mengejar impian kak hanum."
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
                "kesan": "kece bangg",  
                "pesan":"Semangat menjalani harinya bang dan sukses mengejar cita-citanya."
            },
            {
                "nama": "Oktavia Nurwinda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya menyenangkan dan asik pembawaannya",  
                "pesan":"Semangat terus Kak kuliahnya dan sukses mengejar impiannya."
            },
            { 
                "nama": " Deyvan Loxefal", 
                "nim": " 121450148 ", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanloo", 
                "kesan": "Kece betull bang",   
                "pesan":"Semangat dalam segala hal bang." 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamg", 
                "kesan": "Kakaknya asikk bgttss.",   
                "pesan":"happy terus Kak kuliahnya." 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "abang nya kece dan baik.",   
                "pesan":"menyala bang jo dan tetaplah semangat." 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "abang alproo bgtt",   
                "pesan":"semangat bang, sekali kali tutor bolehlah." 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "asikkk betull abangnya",   
                "pesan":"Semangat abang sehat sehat terus orang baik." 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "Belwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya asik dan seru.",   
                "pesan":"Senyum dan semangatlah terus kaka." 
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "asik dan seru.",  
                "pesan":"Semangat dalam perkuliahanya."
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "kakak tergemes dan daplok ter asik ",  
                "pesan":"sehat sehat selalu kak jaclin, loveyou."
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya kece parah terus jago game deh.",  
                "pesan":"Semangat terus menjalani harinya bang."
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "baikkk bgtt kaa.",  
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
          "https://drive.google.com/uc?export=view&id=1Jsjkm7IXksjrZQt9U7wT3BXs8mW6mVye",
          "https://drive.google.com/uc?export=view&id=1J_GbzVgoHB1OZ-vvLPCf6O6cOEoc7gTy",
          "https://drive.google.com/uc?export=view&id=1Kgxb-zeQ0oFVQp_HGVGckMwJXV4C-ETm",
          "https://drive.google.com/uc?export=view&id=1P393FHhFDE1wx7Z4MgfFf6qKVsA_VUTI",
          "https://drive.google.com/uc?export=view&id=1JzbLZyoP28YAzv2fjX5GV2vFt6jNPyC6",
          "https://drive.google.com/uc?export=view&id=1P3rQOqyxmz6aDWqsO0aMPdFXMcaj-PIT",
          "https://drive.google.com/uc?export=view&id=1Jmdp8SJknDxIuNvRtIMzqwFqjHwcBKms",
          "https://drive.google.com/uc?export=view&id=1JixtgD39UNJftzt8brzGpf_1lHZF7l78",
          "https://drive.google.com/uc?export=view&id=1JZ-0LqSLJxCRSbMXtosn6agqFwlnQWy2",
          "https://drive.google.com/uc?export=view&id=1JuNj2lvXXch7av5Om3LQfnz47841NXaH",
          "https://drive.google.com/uc?export=view&id=1K-fv4LsgKvMGIZhZNJfVNwLq3tphC_Z5",
          "https://drive.google.com/uc?export=view&id=1JeODNMy9KfAXEvhX-x_Z39bCgeBiMmPg",
          "https://drive.google.com/uc?export=view&id=1JdWHUtSzfMMVpI03mXCI7L6QWzkoqQJn",
          "https://drive.google.com/uc?export=view&id=1JdhFl9GzvFmUx2CeyDLk__K0_TP6QYcE",
          "https://drive.google.com/uc?export=view&id=1KDT48t6MU-85EgNhRANTlobyFDof6T2C",
          "https://drive.google.com/uc?export=view&id=1KBeoFSmSrd13M9ITMkZ8hpDnzI7r1pcS",
          "https://drive.google.com/uc?export=view&id=1Jl7sjt7Qj3yBpCSVhiyntpGordzCMYJC",
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
                "kesan": "abang asli pertama aku liat keren gitu, kek manly bgtt",  
                "pesan":"Semangat terus bang rafii"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "daplok ter-care love you bang sahid, terus juga selalu bikin kita nyaman. BIG LOVE dari Gaussian abanggkuh",  
                "pesan":"Selalu hibur kami dikala sedih ya bang, dengan jokes receh abang hehe"
            },

            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya pendiem kah?",  
                "pesan":"Semangat terus bang"
            },

            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "Starr banget bang regii, emang duta bengett sih hehe",  
                "pesan":"Semangat untuk duta-duta selanjutnya bangg"
            },

            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Baca novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kembaran ter-kece hehe, awalnya aku nggak bisa bedain lhoo",  
                "pesan":"Semangat terus kak, aku gatauu nih cara bedain kakak gmn soalnya salah satu tuh asprak ads ku hehe"
            },

            {
                "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "121450107",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kemiling",
                "hobbi": "membuka wisata",
                "sosmed": "@nathanndaniel_s",
                "kesan": "Abangnya so cool dan first impresiion aku tuh abangnya care banget terus fast respon juga jawabin chat ku hehe!",  
                "pesan":"Tetap kece dan selalu fast respon ya bang hehe"
            },

            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@here.am.ai",
                "kesan": "abangnya ucull gituu lhoo hehe",  
                "pesan":"Semoga sehat selalu dan sukses selalu buat tugasnya bang"
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "kakanya murah senyum, ramah dan inget nama aku kalo di sapa hehe",  
                "pesan":"Semangat terus kaka cantikk dan sellau murah senyum ya kaka",
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya ramah dan lucu terus pinter bgtt",  
                "pesan":"Semangat terus kak menjalani harinya semangat di mikfess yaa kaka"
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Etaa cantik terus auranya keliatan banget pinterr",  
                "pesan":"selalu ramah dan jangan bosen kalau aku sering nanya ya kak, hehe"
            },

            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Suka sama Kak Rut senyumnya manis",  
                "pesan":"Keep smile dan healty kaka"
            },

            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Senangnya bertemu kakak love",  
                "pesan":"Semangat terus yaa kak"
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rahm_adityaa",
                "kesan": "Abangnya maniss bangett",  
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
                "kesan": "Gokil parahh",  
                "pesan":"Sehat sehat terus bang"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Hobinya samaan nih kak",  
                "pesan":"Semangat terus yaa kakak maniss"
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "Abangnya stay cool bgt yaa",  
                "pesan":"Selalu senyum yaa bang"
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "agak nyebelin yaa, tapi baik kok",  
                "pesan":"Semangat membantu anak anak Gauss bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
          "https://drive.google.com/uc?export=view&id=1KQkLaFLVOYIZN8jCPK88DtijjIIxWmjz",
          "https://drive.google.com/uc?export=view&id=1J-qFwN9EvDlTD2aoQth-o2toc11X7vJN",
          "https://drive.google.com/uc?export=view&id=1KUEpIrLSvDAfdTKh9esqjRcd94fzBiO7",
          "https://drive.google.com/uc?export=view&id=1KURW_QSBC-u8uAZYfwALc5VSwXZDR5F1",
          "https://drive.google.com/uc?export=view&id=19bcgHJ_g6WilL76NblpcypJUH2tmIRGO",
          "https://drive.google.com/uc?export=view&id=19V6RfXZj1hOC2SB17IuO3vOsSl4Prz-N",
          "https://drive.google.com/uc?export=view&id=19V2dz0CGvKMvhABoSZwcXTjJzL2t4kQO",
          "https://drive.google.com/uc?export=view&id=1KRh5kkrF_UP-3VAcQ5mppWPZRRZEVNvn",
          "https://drive.google.com/uc?export=view&id=19XfsajWqB1HM83ne08Lb8or44RNdDY4k",
          "https://drive.google.com/uc?export=view&id=19_dImQRLldo0IkKMScMUpJnP6MCrMbos",
          "https://drive.google.com/uc?export=view&id=19YSUGzbS4SsYp9EaoHwRmXl7zVWVmUzH",
          "https://drive.google.com/uc?export=view&id=19Y3EFKruV8KkvUnmUfHmPLfMOB-jWq_Z",
          "https://drive.google.com/uc?export=view&id=19WgQ4NNFOdWBQAlvh0NCKOssKr158Cx6",
          "https://drive.google.com/uc?export=view&id=1J3OKvHP0BfJfIdCQ9b1OuRINxoEJiEKH",
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@Yogyyyyyyy_",
                "kesan": "bang yogy tuh kek beda bgt vibesnya, terus aura leadernya keliatan bgtt",  
                "pesan":"Please bang nggak mau narik aku ke Hublu kah?"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "kak dhitaa ramah banget uyy, teruss juga baik banget. Makasii yaa kakak kertasnyaa",  
                "pesan":"Kakak lirik aku yukk biar aku join hublu hehe"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya kalem dan lucu gituuu, kiyowooo dech",  
                "pesan":"semangat kuliahnya kakak dan sehat selalu yaa"
            }, 
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "aku notice nama kakaknya lucuu, karena novelia jadi aku inget novel hehe",  
                "pesan":"selalu sehat selalu kakak dan keep smile "
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang gondrong ya kalo kata orang orang, aku kira abang beneran anak teknik hehe",  
                "pesan":"bang tobias selalu ramah dan soft spoken yaaa hehe"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "menyala selalu uda irfann, semangat daa",  
                "pesan":"samangaik udaaa, minangkan HMSD wkwk"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abang rizkii seruu matanya sipit gituu terus maniss",  
                "pesan":"stay healty dan keep smile ya bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "NIM kita sama dong bang, 02 Gang",  
                "pesan":"buktikan nim 02 itu selalu menyala abangkuu"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfawwwww",
                "kesan": "uniii aca ramah dan asikk betulls",  
                "pesan":"semangat sekdep ikm ku hehe"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "kece bang gayanya unikk",  
                "pesan":"semangat cari relasii abanggg"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "17",
                "asal":"Bogor",
                "alamat": "Pemda",
                "hobbi": "Bersholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kak Triaa canciii amayy",  
                "pesan":"langgeng ma doinyaaa ya kaka"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanefi",
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
                "kesan": "Kak Mine aku kira awalnya cuekk tauu, tapi ternyata seasik ituu kalau dah dekett",  
                "pesan":"selalu menerbarkan aura positive kak Minee"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OCcFPkVB3QFTFLwb8q1hcEDWiIAK7TBT",
            "https://drive.google.com/uc?export=view&id=1O_-GmReBmNSfZYEzspJwRgJ7phwgb4_L",
            "https://drive.google.com/uc?export=view&id=1OL0aj9CzcEbaNUeP7h-B-samxxg5fYz0",
            "https://drive.google.com/uc?export=view&id=1J7wMq7g-tpVooMI5v3Wmc9yoFqz6Yv9m",
            "https://drive.google.com/uc?export=view&id=1JCi49oiq1EJNX7Sv2NKYjzMT3PTwa7S1",
            "https://drive.google.com/uc?export=view&id=1ORYlIdEHGo9hTp7XUZ0Y7jSW_kInO-TY",
            "https://drive.google.com/uc?export=view&id=1OQqpGSmVTOqj1sb9mfLj5SYgSgxwlXQN",
            "https://drive.google.com/uc?export=view&id=1O9bgLT_02744WwhLqZufWgEmSF_oGe0N",
            "https://drive.google.com/uc?export=view&id=1OF28eAOzYo8gnltSazZOzvlvK3FHQZOD",
            "https://drive.google.com/uc?export=view&id=1JANgcQ8AqGOOynDKUFqg8slB9mWvfBs2",
            "https://drive.google.com/uc?export=view&id=1J9ERYpCstwsCyQAoSuMw-MorcWDBGxS0",
            "https://drive.google.com/uc?export=view&id=1OXZDh8ed6NtDPRzt-5Hu-A75dgl3rgSE",
            "https://drive.google.com/uc?export=view&id=1OHc69wyhrjYQXyxz0VSF9HrYW8aORq2S",
            "https://drive.google.com/uc?export=view&id=1OL0aj9CzcEbaNUeP7h-B-samxxg5fYz0",
            "https://drive.google.com/uc?export=view&id=1J7wMq7g-tpVooMI5v3Wmc9yoFqz6Yv9m",
            "https://drive.google.com/uc?export=view&id=1JCi49oiq1EJNX7Sv2NKYjzMT3PTwa7S1",
            "https://drive.google.com/uc?export=view&id=1ORYlIdEHGo9hTp7XUZ0Y7jSW_kInO-TY",
            "https://drive.google.com/uc?export=view&id=1OQqpGSmVTOqj1sb9mfLj5SYgSgxwlXQN",
            "https://drive.google.com/uc?export=view&id=1O9bgLT_02744WwhLqZufWgEmSF_oGe0N",
            "https://drive.google.com/uc?export=view&id=1OF28eAOzYo8gnltSazZOzvlvK3FHQZOD",
            "https://drive.google.com/uc?export=view&id=1JANgcQ8AqGOOynDKUFqg8slB9mWvfBs2",
            "https://drive.google.com/uc?export=view&id=1J9ERYpCstwsCyQAoSuMw-MorcWDBGxS0",
            "https://drive.google.com/uc?export=view&id=1OXZDh8ed6NtDPRzt-5Hu-A75dgl3rgSE",
            "https://drive.google.com/uc?export=view&id=1OHc69wyhrjYQXyxz0VSF9HrYW8aORq2S",
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
                "kesan": "Abang Dimass menginspirasi dan keren banget publik speakingnyaa",  
                "pesan":"semangat terus kuliahnya bang, semoga lulus tepat waktu yaa!"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@catherine.sinaga",
                "kesan": "Kakaknya baik, positive vibes",  
                "pesan":"semangat terus kuliahnya kak, semoga semua urusannya diperlancar!"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "abang tuh asik di ajak diskusi",  
                "pesan":"lancar luncur semua urusannya bang sukses terus!!"
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
                "pesan":"Semoga Kakak sukses selalu ke depannya!"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakak tuh imut tauu.",  
                "pesan":"Semoga bahagia dan happy happy aja yaa Kakak!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@lexanderr",
                "kesan": "Aselii chill gitu lho abangnya dan memiliki kepribadian yang ramah dan menyenangkan.",  
                "pesan":"semangat terus kuliahnya ya abangg!"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "abang kece badaii",  
                "pesan":"Semoga abang selalu diberi kemudahan dalam setiap usaha!!"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar.resdika",
                "kesan": "Selalu menciptakan suasana yang asik abangnya",  
                "pesan":"Semoga semua usaha abang membuahkan hasil yang memuaskan yaa!"
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
                "pesan":"Semoga Kakak selalu dikelilingi orang-orang baik!"
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
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!"
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
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!"
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Kakak sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Kakak sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Oc18UYYbXZoHX3wrs5_l6xnFI_3NHtdp",
            "https://drive.google.com/uc?export=view&id=19mrD21DBctqJRC9zti3j_HHHStTASp_g",
            "https://drive.google.com/uc?export=view&id=19qo5X5GLd3M2Za1slhevgcIMbGWJfCPC",
            "https://drive.google.com/uc?export=view&id=19lRWR81B9a9Y2QmbNZz76Gt88rEmJfqB",
            "https://drive.google.com/uc?export=view&id=19jkG7oFBpalL2gqAk5kcKGxw-UXX2XpQ",
            "https://drive.google.com/uc?export=view&id=19lSHRCoFb8uFZKMTApMouiF2ct7Tf-Wb",
            "https://drive.google.com/uc?export=view&id=1OeWPyuCQ2pWd58ukX4m2Jpu8GMS8FMBj",
            "https://drive.google.com/uc?export=view&id=19hIwNPj-F5Aspb0Jo1Iimvkr_h0MjD5D",
            "https://drive.google.com/uc?export=view&id=1OeXOjyimSHm_zfYMa-IPkJrsnK1BYCCR",
            "https://drive.google.com/uc?export=view&id=19u2bOds-1rDXPJE5Jv7P0v_MkYxlHIi6",
            "https://drive.google.com/uc?export=view&id=19tTfYI9J_aUsQn17wxomBpYWYnqsp9E2",
            "https://drive.google.com/uc?export=view&id=1Ogx4gLWXpgTg6k_Wg8MbC1-xWVyeCVt2",
            "https://drive.google.com/uc?export=view&id=1Og_bfM-jYKph7F7VMv02q1-FQEI2VIVg",
            "https://drive.google.com/uc?export=view&id=1Ofu5tJB8aJ7b7-IBK3RLq6Yy43Ewf16l",
            "https://drive.google.com/uc?export=view&id=19t8L46KMTPcYBrhQfTFfSzN3b58qO2sn",
            "https://drive.google.com/uc?export=view&id=19riWo0ArUYGC092nTRBdUl-31O7QA2sl",
        ]

        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@wayyulaja",
                "kesan": "abangnya asik dan gayanya kece terus kreatif bgttt",  
                "pesan":"semangat ngontennya abang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "kakak ini cantik sekali, dan soft gituuu lhoo terua aku inget sepupuku karena namanya juga elok hehe",  
                "pesan":"semangat kaka cantikk, lucuu selalu yaa"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Kak cibell ini mengingatkan aku dengan cherrlybell",  
                "pesan":"Stay healty dan selalu murah senyum kaa Cibell"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "kak Cia paling lucuu, suaranya lembut dan super baik",  
                "pesan":"semangat kakak love you, jangan bosen yaa tiap aku nanya pas prak hehe"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "kaka sangat responsif dan lucu",  
                "pesan":"jangan pantang menyerah terhadap apapun yaa kakak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "sangat kalem dan lucu",  
                "pesan":"semangat mengejar cita - citanya kak"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "bang kaisar namanya keren hehe",  
                "pesan":"semangat bang untuk ngejalanin kehidupan yang sulit ini"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kakaknya super asik dan lucu",  
                "pesan":"semangat jangan menyerah dan terus berjuang!"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@jimnn.as",
                "kesan": "kece betul bang, kukira ditangannya pas foto itu oreo hehe",  
                "pesan":"semangat bang ngejar cita-cita nya"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kakaknya asik sekali, eh btw nama afifah banyak juga ya wkwk",  
                "pesan":"ayo sinari dunia lewat nur mu kak heh!"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakak ucull bgt ekspresinya",  
                "pesan":"sehat selalu kakak!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@arsalutama",
                "kesan": "Kece badai dan apa abang emang kalem ya bang?",  
                "pesan":"semangat terus bang belajarnya!"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@abitahmd__",
                "kesan": "asikk banget bang, pasti jago uno nichh",  
                "pesan":"ayooo bang main uno barengg"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "ucul banget rambutnya mirip prof, hehe",  
                "pesan":"sehat sehat abang akmall!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Bang mawan pelawak handal, moodboster bgtt pokoknya",  
                "pesan":"sehat sehat abang penghibur!"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kak nisa ucull bingitss",  
                "pesan":"semangat terus kak belajarnya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1E1BMCcdmV6jhL66dnM8_slLsXtY9DVnX",
            "https://drive.google.com/uc?export=view&id=1fKx4ch7R1P1wa2_z2XjQUbUWvXXQCtG5",
            "https://drive.google.com/uc?export=view&id=1-AIN-kaJxiLVARoa28Gn2ecj7shCZUPB",
            "https://drive.google.com/uc?export=view&id=16WPciEooa7Y4Dr5TUfXnRzqO9vaJW54j",
            "https://drive.google.com/uc?export=view&id=1ytB-OIYTRVhZNg3Yy5xIaSoCrihAWjUb",
            "https://drive.google.com/uc?export=view&id=1Ld2o-wmt3AAeO-VIFmu4ZW8PorN0gqWC",
            "https://drive.google.com/uc?export=view&id=1RAhPfc8eNuo15lMBGc4EkoOQSnuH8O92",
            "https://drive.google.com/uc?export=view&id=1nATm6szPGQchtRofOePRKY0dmglAxUlB",
            "https://drive.google.com/uc?export=view&id=19ygCZ5B5B4gcQsI5l_jC8LJ3KdeGzN_H",
            "https://drive.google.com/uc?export=view&id=1clsgasMmaJO9k0jOq9_q2pyersRdX7LM",
            "https://drive.google.com/uc?export=view&id=1fDMBgj7x_GhHf9cvvaViOKXpVGYo9ulq",

        ]
        data_list = [
             {
                "nama": "Andrian Agustinus Lumbangaol",
                "nim": "1211450090",
                "umur": "21",
                "asal":"Cirikalang",
                "alamat": "Dekat Penjara",
                "hobbi": "nyari hobi",
                "sosmed": "@andriangaol_",
                "kesan": "kece betul abangda, semangatt jadi kadep abangg",  
                "pesan":"sehat sehat abangdaaa, moga cepat lulus yaaaw"
            },
            {
                "nama": "Adisty Syawalda Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "nonton film",
                "sosmed": "@adistysa_",
                "kesan": "kece betul kakaknii, kiyowoo",  
                "pesan":"sehat sehat orang baik dan cantik"
            },
             {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zhjung_",
                "kesan": "kakanya lucu nan imut",  
                "pesan":"sehat sehat orang baik dan cantik"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Bukittinggi",
                "alamat": "Airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "uda ni kece badai abiss terus ganteng pisan euyy",  
                "pesan":"sehat sehat dan elok elok dirantau da"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "cool banget gayanya bang",  
                "pesan":"sehat sehat bang"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Salatiga",
                "alamat": "Bogor",
                "hobbi": "Jl.lapas",
                "sosmed": "@farrel__julio",
                "kesan": "Kapo ter kece badai",  
                "pesan":"tunjukkan biru rmas itu selalu menyala bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "maniss bgt kaka senyumnya",  
                "pesan":"sehat selalu kaka"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "kece badai kakak duta nii",  
                "pesan":"selalu raih mimpi appaun setinggi mungkin kak"
            },
            {
                "nama": "Alvia Asrinda Br.Ginting",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alfiagntng",
                "kesan": "ucullnyaa terus glowing bangett",  
                "pesan":"sehat selalu kaka"
            },
            {
                "nama": "Dhafin Rezaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnya pendiem kah hehe?",  
                "pesan":"sehat selalu bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "kakanya mood bangettt",  
                "pesan":"selalu sebar kebahagiaan lewat senyum ya kaka"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()
