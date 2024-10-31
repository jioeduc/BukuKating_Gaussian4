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
            "https://drive.google.com/uc?export=view&id=1D0SRw4U3pp2B4Q7jk8W2RPweZd6_5NAU",
            "https://drive.google.com/uc?export=view&id=1D_1B6x5l4Uk1blMcUYtBRUVBf3rqTaPH",
            "https://drive.google.com/uc?export=view&id=1CrhJ4bzIlTRToRdp1iw-yelRsZENc8gt",
            "https://drive.google.com/uc?export=view&id=1D5jLyX1Ti_ANlSRkUCUbPObaikwIgMLX",
            "https://drive.google.com/uc?export=view&id=1CsQJm8t6h6q7CsSlSoE4tL82WA7aapci",
            "https://drive.google.com/uc?export=view&id=1EHULWWY6cLJkMqvv8Z9Qe5AEpQu4T4Ic",
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
                "kesan": "Abangnya asik banget di ajak ngobrol",  
                "pesan":"semangat selalu buat abang semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abang nyaa asik banget ",  
                "pesan":"Semangat kuliah dan TA nya abang semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak lucu sekali dan positive vibes sekali",  
                "pesan":"Semangat menjalani kehidupan kuliah kak"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak nya gemay banget, so anggunly",  
                "pesan":"semangat terus kuliahnya kakak, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak nya baik banget, lucu banget",  
                "pesan":"semangat mengejar gelar kak, bahagia selalu"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak keren bangett sii",  
                "pesan":"semangat kuliahnya kak, sehat-sehat yaa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18lo42HFw9UPWLPswoF8tLq7sv8hSB_zB",
            "https://drive.google.com/uc?export=view&id=18Zrvkh49dDJnHstv1aJI9GV9jScqGhb9",
            "https://drive.google.com/uc?export=view&id=18TOq-CTKJqpmOnbZ7zR4wOAVB4VP7qcP", # 3
            "https://drive.google.com/uc?export=view&id=18B37vbT624hVEwuZL08D6Dh0rEaGYYAJ", # 4
            "https://drive.google.com/uc?export=view&id=185eE5RANBkBCH3p3Z57geCADKDs575hc",
            "https://drive.google.com/uc?export=view&id=18EqsUZxqJZRI78AlHVOgXWSDXzXcUg1Z",
            "https://drive.google.com/uc?export=view&id=181GMoyyH3h1nToGUr8m4kxzXu8tUffpX",
            "https://drive.google.com/uc?export=view&id=18YP2wTtaumxNxSSQfu_G8ql-7ZpP0znY",
            "https://drive.google.com/uc?export=view&id=18d5xzgZcyXvtQDkWWeqJZ3mttzt-VEhH",
            "https://drive.google.com/uc?export=view&id=18HM9A3NFCrWF94s0Xb2_XUAUC5ZbqVL8",
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
                "kesan": "Kakak asik banget, buat suasana menjadi cair",  
                "pesan":"semangat terus kuliahnya kakak, semoga cepet dapet gelar yaa"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini kiyowo + baik sekali ",  
                "pesan":"semangat menjalani kei=hidupan perkuliahan kakak"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya enak diajak ngobrol",  
                "pesan":"sehat-sehat kak, semangat terus"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang asik banget dan seru banget ngobrolnya",  
                "pesan":"semangat mengerjakan segala tugas bang, sehat selalu"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya menyenangkan dan asik",  
                "pesan":"semangat menjalani kuliahnya abangku"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang nya seru banget, keren banget abang",  
                "pesan":"semangat terus bang kuliahnya,semoga selalu dikelilingi kucing lucu"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya asik banget diajak ngobrol",  
                "pesan":"semangat terus mengerjakan tugasnya bang, sehat-sehat"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik buat diajak ngobrol",  
                "pesan":"sehat sehat kak, semangat kuliahnya"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak lucu banget",  
                "pesan":"semangat kak, bahagia selalu"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini baik banget, keren kak",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selalu"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1957HY5l7cN81pGIoDEEW6nNOu5WoQ8ZB",
            "https://drive.google.com/uc?export=view&id=190U6qJMVDUnmiGe-ReiJeje9rqEl4vjS",
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
                "kesan": "keren banget kakanya ++ kiyowo bangettt!!!",  
                "pesan":"semangat selalu dan tetap keren kakak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "Bang Bintang super supportif orangnya, keren banget bisa join semua kegiatan gitu bang",  
                "pesan":"Tetep jadi orang keren bang, bahagia selalu bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mJWg1yclTXpsiKhiR2e2UCPQp672L3TZ",
            "https://drive.google.com/uc?export=view&id=1mU2YD2nRrNO9uFllJkegSRHhks7Hxb1b",
            "https://drive.google.com/uc?export=view&id=1mKEJbYSGkcRJ8ve5e1rkiqpi-M8A5xhF",
            "https://drive.google.com/uc?export=view&id=1lx-SbfpaLirs-zoyiYaJKDIKilgGoA27",
            "https://drive.google.com/uc?export=view&id=1mSUa2Zq5DB0ZVHT2GrU-rWw6AU1CcFtz",
            "https://drive.google.com/uc?export=view&id=1mNYpSZhHJ_DjQnXPJcCG3sJk1py2p5FG",
            "https://drive.google.com/uc?export=view&id=1rL93wiyf_T9lDBjwxBXihEBk06OnbVh7",
            "https://drive.google.com/uc?export=view&id=1mKBtzsnJDipGpL5xVwgu1129JeZE4rnF",
            "https://drive.google.com/uc?export=view&id=1mKhqvASsnd6lM3BgbHHLoyYsK-_4MLI_",
            "https://drive.google.com/uc?export=view&id=1lT_jEq1oPe0qNntaH8Pc-Uo4LEJRiPty",
            "https://drive.google.com/uc?export=view&id=1l_RcT1DjkgMpKvAvMBFVoEM5Hs5R7QJD",
            "https://drive.google.com/uc?export=view&id=10-9Nk8Wb-d6qjSUajJhqda70cQXiVGIE",
            "https://drive.google.com/uc?export=view&id=1laHjiJEc_J3Ax9wQiM3IT4joOC1o3Qaa",
            "https://drive.google.com/uc?export=view&id=1lXn4_E482ALHyEltbG4-R4_BCUm-ZH3W",
            "https://drive.google.com/uc?export=view&id=1lcG6pCBWjL2dyfr-NHyAF3X5xRu-_UVV",
            "https://drive.google.com/uc?export=view&id=1ls12PHS65o45nAF_dFqwYvTN1jCUqH2y",
            "https://drive.google.com/uc?export=view&id=1loOtRf7rAJwDBgywlJzfHE8sKeMZnsK6",
            "https://drive.google.com/uc?export=view&id=1lncjXl1uPyMapiskS7l6HJP3ypLAdjFs",
            "https://drive.google.com/uc?export=view&id=1llWKVVDQrCpLFKqLdYLcTrWuSZaksOl6",
            "https://drive.google.com/uc?export=view&id=1lw_Ph9kJVYoPKNgJdf9QT77guqk-YBHV",
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
                "kesan": "abang asik banget, enak banget buat diajak deeptalk",  
                "pesan":"Semangat kuliahnya bang dan semoga bisa cepet lulus bang "
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya lucu pliss dan keren kak",  
                "pesan":"Terus semangat kuliahnya Kak dan sehat selalu kak"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya baik banget, lucu banget kakak",  
                "pesan":"sehat sehat kak, sukses selalu yaa"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami",
                "kesan": "kakak keren bangettt, sehat sehat kakak",  
                "pesan":"semangat menjalani kehidupan perkuliahan kak, sukses selalu ya"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakanya asik banget, mantap kak",  
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
                "kesan": "kakanyanya kiyowo banget, baik banget jugaa",  
                "pesan":"Semangat terus kuliahnya kak, sehat selalu yaa"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya seru banget buat diajak ngobrol, keren bang",  
                "pesan":"Semangat Bang kuliahnya dan sukses mengejar gelar"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "abangnya asik parah dan menyenangkan",  
                "pesan":"Semangat terus kuliahnya bang dan sukses mengejar gelarnya bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya menyenangkan dan asik jugaa",  
                "pesan":"Semangat terus Kak kuliahnya dan sukses mengejar impiannya."
            },
            { 
                "nama": " Deyvan Loxefal", 
                "nim": " 121450148 ", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanlo", 
                "kesan": "abang asik dan seru banget buat diajak ngobrol",   
                "pesan":"Semangat terus bang kuliahnya dan semoga cita-citanya tercapai" 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamy", 
                "kesan": "Kakaknya asik dan lucu banget pliss",   
                "pesan":"Semangat terus Kak kuliahnya dan semoga kuat mengerjakan semua tugas" 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "abangnya gokil banget, keren banget abang",   
                "pesan":"Semangat bang kuliahnya dan selalu jadi orang keren bang" 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "abangnya keren pliss, pinter banget bang",   
                "pesan":"Semangat bang kuliahnya dan semoga sehat selalu yaa" 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "abang baik banget,care banget sii, seru banget buat diajak tukar pikiran",   
                "pesan":"Semangat terus abang kuliahnya dan bahagia selalu abang" 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya lucu banget",   
                "pesan":"Semangat terus Kak kuliahnya dan semangat menjalani kehidupan dunia ini kak" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya seru banget buat diajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya, ditunggu gelar barunya yaa"
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya keren banget",  
                "pesan":"semangat menjalani kehidupan perkuliahan bang, semoga cepet dapet gelar Si.D nya"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "kakak terlucu dan terkiyowo, love banyak-banyak",  
                "pesan":"semangat dan bahagia selalu kakak, selalu jadi orang keren yaa "
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya keren parah",  
                "pesan":"Semangat selalu bang, sehat sehat bang"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "kakaknyaa lucu bangetttttt",  
                "pesan":"Semangat menjalani kehidupan kak, sehat sehat kakkkkk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kffFGJ8URC-R5IRICBhfuTxfBH2_9Z11",
            "https://drive.google.com/uc?export=view&id=1kGQIbwwt-3aiffAmUoa1rgjeUdbrRlz5",
            "https://drive.google.com/uc?export=view&id=1k2Ufv0rYjxyor_ZV9sz0iPkHEcItbV-N",
            "https://drive.google.com/uc?export=view&id=1kmYG17OTAWGpJkCznf7oET5RYAJrYCnt",
            "https://drive.google.com/uc?export=view&id=1jikS4fSz83S8nTsKRhpRsHHNbW20ncq_",
            "https://drive.google.com/uc?export=view&id=1uthuqLX2Zakr9EgcmBN9MfvyIXFT2wWf",
            "https://drive.google.com/uc?export=view&id=1k6QulPy-FDAjodgG__nsqrGbK5f0Fdv6",
            "https://drive.google.com/uc?export=view&id=10BoPl58YPznTfKgQjxd_U9h88qrhaly4",
            "https://drive.google.com/uc?export=view&id=1kWK3iqkWBtXWDr04NDpnJhek8yQeD2PW",
            "https://drive.google.com/uc?export=view&id=1kQ5Vg8jo_IpLgIBWKpAeDUGUaOmUclka",
            "https://drive.google.com/uc?export=view&id=1mLnft65u1DBDZZMkxO47IYBRQaMEY3qf",
            "https://drive.google.com/uc?export=view&id=1jbdwv9-l5SiYplwqZuxv-R7I5ioxuwqN",
            "https://drive.google.com/uc?export=view&id=1jI7B4yMJp3VXcB16PiL-NoNw1rqIRD9_",
            "https://drive.google.com/uc?export=view&id=1jpIR8kE3ZbuPUjxDIbsBVvYYXVx6Eew4",
            "https://drive.google.com/uc?export=view&id=1jYdNfsQqLdBMW5z5tlF_JiI882peMBjv",
            "https://drive.google.com/uc?export=view&id=1kjk9V_1l9nGoHnw3JkXpfbx-8TLwO-Z8",
            "https://drive.google.com/uc?export=view&id=1js6AJUXSDUdExxrS4_yb5cgCxygif9ou",
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
                "kesan": "abangnya baik banget, seruu banget",  
                "pesan":"Semangat terus bang, semoga cepet dapet gelar yaa"
            },
            {
                "nama": "Annisa Novatika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl.Pulau Sebesi, Sukarame",
                "hobbi": "baca novel",
                "sosmed": "@annovavona",
                "kesan": "kakaknya lucu bangett",  
                "pesan":"Semangat terus kak semoga cepet lulus yaaa"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abangg terbaikku, menyala selalu abangkuu",  
                "pesan":"Semangat menjalani kehidupan bang, bahagia selalu abang"
            },

            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya gokilll bangettt, keren bang",  
                "pesan":"Semangat terus bang, sehat sehat di dunia ini"
            },

            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "abangnyaaa keren parah pake bangettt, positive vibes",  
                "pesan":"Semangat terus bang, semangat menjadi manusia di bumi ini"
            },

            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Baca novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Awalnya bingung ternyata kembar, kakaknya lucuu banget",  
                "pesan":"Semangat terus kak, sehat selalu yaa"
            },

            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnya lucuuu banget, humble jugaa",  
                "pesan":"Semangat terus bang, semoga kuat sampai tamat"
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "121450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "kakaknyaa lucu banget, keren kak",  
                "pesan":"Semangat terus kak, semoga cepet dapet gelar kak"
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya humble banget, lucu jugaa",  
                "pesan":"Semangat selalu kak, semoga kuat sampai tamat kak"
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "kakak lucuuu bangettt, positive vibes jugaa",  
                "pesan":"Semangat terus kak, tetap keren kak"
            },

            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "pliss kakak baik bangett, friendly jugaa",  
                "pesan":"sehat sehat kakak, tetap jadi orang baik yaaa"
            },

            {
                "nama": "Syahdza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kakaknyaa humble bangett, lucu jugaa pliss",  
                "pesan":"Semangat terus kak, sehat sehat yaaa"
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhmn_adityaa",
                "kesan": "Abangnya keren bangettt, pinter banget sii bang",  
                "pesan":"keren selalu abangg, semangat menjalani kehidupan ini"
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "Gokil banget bangg, baik banget sih bang",  
                "pesan":"sehat sehat bangg, Semangat terus yaa bang"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "lucuu banget kakak",  
                "pesan":"semangat mengejar gelar kakak"
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "Abangnya kerenn yaaaa",  
                "pesan":"Semangat terus bang, sehat selaluuu"
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa gokil bangettt, kok bisa pinter banget sihhh bangg??",  
                "pesan":"sehat sehat di dunia ini bang, keren selalu yaaa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1i_A3IstSXJtV7vMaNCBLIopkx3q2ZvwR",
            "https://drive.google.com/uc?export=view&id=1fTeuYLBmLlW9vPOKzz3gsrAQx1Ch1e4K",  
            "https://drive.google.com/uc?export=view&id=1f_ZaxSTzLGF0P7dk0qkUIW3eRKsTru91",
            "https://drive.google.com/uc?export=view&id=1fhVujJrcFx4GQ5ZoyWpvAH20GQyN7UKj",
            "https://drive.google.com/uc?export=view&id=1rK-z3gFYjmvWWnnaoJjcFjekCLdT3rXL",
            "https://drive.google.com/uc?export=view&id=1fdc36TzDwoF7K8hdLhLxtGJTWHX8bQW0",
            "https://drive.google.com/uc?export=view&id=1g2gl1wrbiBIkZm_xk5dsqrFFQnNyr_RV",
            "https://drive.google.com/uc?export=view&id=1g1IAWHDU_0SWAttj6H9sc0nM4UPSOEQr",
            "https://drive.google.com/uc?export=view&id=1fjjGfKLrQEcuQ36xpss-bkERaiiPO6zC",
            "https://drive.google.com/uc?export=view&id=1nzMXjNZpftgwPOvM7gpGNVHp7rYCCSCr",
            "https://drive.google.com/uc?export=view&id=1fpnnwfolFp5iDYEnxSmzhw4mlvxHIabd",
            "https://drive.google.com/uc?export=view&id=1ip8EJKuTiJYax13mXU03Sv3uj-Ss5UzC",
            "https://drive.google.com/uc?export=view&id=1fj2NLXJ9NSK5ECjevHwcZXsd9EDopXPo",
            "https://drive.google.com/uc?export=view&id=1fzGK6n3PFBpc_q-1UDBaRk2dbwgjOKgZ",
            "https://drive.google.com/uc?export=view&id=1fyfFLRC_JR88z472dL0S2cpdg_dK7uuY",
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
                "kesan": "abangnyaa keren bangettt, sangat terlihat orang baiknya yaa",  
                "pesan":"Semangat Kuliahnya abang, sehat sehat yaa"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121400131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya lucuu bangett, luv luv",  
                "pesan":"Semangat Kuliahnya Kakak, semoga cepet dapet gelar yaps"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kakak nyaaa asikk banget",  
                "pesan":"semangat kuliahnya kak, sehat sehat yaa kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya keren banget",  
                "pesan":"semangat kuliahnya kak, semoga kuat sampai tamat"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya asikk banget, humble banget jugaa",  
                "pesan":"semangat kuliahnya bang, keren selalu abang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya kerenn banget ",  
                "pesan":"semangat kuliahnya kakak, sehat sehat kakak"
            },
            {
                "nama": "Rizki Adrian Bennofry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abang keren bangettt",  
                "pesan":"semangat kuliahnya bang, semoga cepet lulus ya bang"
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
                "pesan":"semangat kuliahnya bang, semoga kuat selalu yaa"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Ening",
                "alamat": "Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini lucuu bangettt",  
                "pesan":"semangat kuliahnya kakak, sehat sehat kakak"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfawwwww",
                "kesan": "Kakak ini baik dan asikk sekali",  
                "pesan":"semangat kuliahnya kakak, sehat selalu"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya keren sekaliii",  
                "pesan":"semangat kuliahnya bang, semoga sehat selalu yaa"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Main Volly",
                "sosmed": "@@izzalutfiaa",
                "kesan": "Kakak asik dan menyenangkan, humble bangett",  
                "pesan":"semangat kuliahnya kakak, keren selalu kakak"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak ini asik, lucu banget kakak",  
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
                "kesan": "Kakak asikk bangett, pliss keren banget kak",  
                "pesan":"semangat kuliahnya kakak, semoga kuat sampai tamat kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nUBJLi-i-TMspuAxC1qV9xbyG6pZ0vP8",#1
            "https://drive.google.com/uc?export=view&id=1ncvqt6S9ZlDLn70x0XzgQgFheqA83mAd",#2
            "https://drive.google.com/uc?export=view&id=1nY-57WEGpsGEVtVEOJ8lcu4iHvOXKtjW",#3
            "https://drive.google.com/uc?export=view&id=1nELoUXexoBbkn6F9tifKV6oLwGfEuPEm",#4
            "https://drive.google.com/uc?export=view&id=1nHtWubFjqX_zgv-FS0aMA1YLFeLMSR2L",#5
            "https://drive.google.com/uc?export=view&id=1naWGdYuQqA3IJXN4RWhYGM5Xl_0wyBMN",#6
            "https://drive.google.com/uc?export=view&id=1nVhvyeU81MteusnYj2CF8Wu9IdPVJHdQ",#7
            "https://drive.google.com/uc?export=view&id=1n92QLMeFJOD_qqoT2JYvHmPjgY81zean",#8
            "https://drive.google.com/uc?export=view&id=1nRP_8g7M-kn-fI4iQOltHoIQQZjuxbdj",#9
            "https://drive.google.com/uc?export=view&id=1nLH2ycBnIyRpMBoBssgIODLNsnAVkTEc",#10
            "https://drive.google.com/uc?export=view&id=1nNoZYu9n74otJCmkNXKy8rj9KeodfGI0",#11
            "https://drive.google.com/uc?export=view&id=1nb6-_OQigH3bb6biQNERrPSGj8mkPO9S",#12
            "https://drive.google.com/uc?export=view&id=1lGRaKMz-Kbe1F_B3ExYimfzmvXXoqqzr",#13
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
                "kesan": "Abang sangat menginspirasi, keren abang",  
                "pesan":"semangat terus kuliahnya bang, semoga lulus tepat waktu!!!"#1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@catherine.sinaga",
                "kesan": "Kakaknya baik, positive vibes banget kaka",  
                "pesan":"semangat terus kuliahnya kak, sukses selalu kakak"# 2
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "gokil banget bang, anw kita asalnyaa sama nih bang",  
                "pesan":"Semoga lancar TA nya abang, sukses terus!!"# 3
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakak sangat ramah, baik banget kakak",  
                "pesan":"Semoga Kakak sukses selalu, sehat-sehat kakak"# 4
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakak asik banget, baik banget",  
                "pesan":"bahagia selalu kak, semangat kuliah"# 5
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@lexanderr",
                "kesan": "abangnya keren banget, mantap bang",  
                "pesan":"semangat terus kuliahnya bang, semoga kuat sampai tamat"# 6
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "abang sangat baik dan positive vibes",  
                "pesan":"Semoga abang selalu diberi kemudahan menjalani kehidupan ini"# 7
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar.resdika",
                "kesan": "asik parah bang, lambar pride nih bang",  
                "pesan":"sehat-sehat abang, sukses selalu yaa"# 8
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
                "pesan":"Semoga Kakak selalu dikelilingi orang-orang baik yaa"# 9
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Lihat cogan",
                "sosmed": "@slafhn_",
                "kesan": "Kakak lucuu bangett, asik juga nih kak",  
                "pesan":"semoga kuat sampai tamat kak"# 10
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@ranipuu",
                "kesan": "Kakak lucu banget, keren kak",  
                "pesan":"sukses selalu kak, bahagia terus yaa"# 11
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "abang baik bangetttt, mantap bang",  
                "pesan":"Semoga abang selalu berhasil dalam semua yang dilakukan!!"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "abang asik parah, gokil parah bang",  
                "pesan":"Semoga sehat selalu bang, kuat sampai tamat yaa"# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vuJFxta4TY-pvOorj4cY1J1bshBkkXdg", #1
            "https://drive.google.com/uc?export=view&id=1vasAHoFOPsEqzcqqFuvyhBghUTXr1VXu", #2
            "https://drive.google.com/uc?export=view&id=1vajgAWZdSXAViOjo_mvyNuBU5PLRcCl3", #3
            "https://drive.google.com/uc?export=view&id=1vdQPF49oMjBsT8CDLdo4C3thnn9ArQI2", #4
            "https://drive.google.com/uc?export=view&id=1w0V9f0bL-KYLslLJIOFZDFGS57aLr4Av", #5
            "https://drive.google.com/uc?export=view&id=1vt509I_tvbsUSb2hOqgTcYtPswuul1wC", #6
            "https://drive.google.com/uc?export=view&id=1ve93FpdxQdoYs-Gc8MtbN5JDr8uRQ1-L", #7
            "https://drive.google.com/uc?export=view&id=1vqEGO_DpGJSsYY6Aex6HqAynuxO-wz2U", #8
            "https://drive.google.com/uc?export=view&id=1vg5AJn09LIxkq5nTuZ95hsnjvdpl4d7M", #9
            "https://drive.google.com/uc?export=view&id=1vq0aNusicZATzWHcv_oX9C6qSUU5aBNw", #10
            "https://drive.google.com/uc?export=view&id=1w-gJV_CZFj3NPXng-o2f4PbUCraR8SeM", #11
            "https://drive.google.com/uc?export=view&id=1w4tmnkP992NonPKjkIjwLfbX8b4fjUKf", #12
            "https://drive.google.com/uc?export=view&id=1vv8yIj7-y7WDgaqPmXFvDxALOqBAUriX", #13
            "https://drive.google.com/uc?export=view&id=1vToqQOgOKJxK6SO33tgs7gH7C4b_iKXN", #14
            "https://drive.google.com/uc?export=view&id=1w2ygJxO-tzZXdc1i_ks5R3h1hO5JPmPP", #15
            "https://drive.google.com/uc?export=view&id=1vUTIE6a1UTlB5ytcbQvAYlOHWpPG1omw", #16
        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "wayyulaja",
                "kesan": "abangnyaa gokil parah, seruuu!!",  
                "pesan":"semoga bahagia selalu bang, sehat-sehat yaa"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@Elokviola",
                "kesan": "kakak ini cantik sekali,terus lembut bangett",  
                "pesan":"semangat ngejar cita - citanya kak, bahagia selalu kak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Kakak lucu bangett, anggunly",  
                "pesan":"semangat kak kuliahnya, sehat-sehat yaa"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "kakak feminime bangett, lucuuu",  
                "pesan":"semangat kuliahnya kak, bahagia selalu yaa"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "kakak baik banget, positive vibes",  
                "pesan":"semangat ngejalanin kehidupan kuliah kak, bahagia selalu"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "kakak baik bangett, mantap kak",  
                "pesan":"semangat kak ngejar cita - citanya"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "abangnyaa keren banget, mantap bang",  
                "pesan":"semangat bang untuk ngejalanin kehidupan, sehat-sehat"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kak lucu bangett, asik jugaa",  
                "pesan":"semangat kuliahnya kak, sehat selalu"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@aimnn.as",
                "kesan": "abang keren banget, asikk banget bang",  
                "pesan":"semangat bang ngejar gelar nya"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kakaknyaa baik banget, asikk",  
                "pesan":"semangat terus kak, bahagia selalu"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakak baik banget, asik sekali",  
                "pesan":"semangat terus kak kuliahnya!!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "-",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@Arsalutama",
                "kesan": "abang keren bangett, seruuu banget",  
                "pesan":"semangat mengejar gelar bang, moga cepet lulus"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "abangnyaa keren banget,gokil parah ",  
                "pesan":"semangat terus bang kuiahnyaa, sehat-sehat"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@akmal.faiz",
                "kesan": "abangnyaa asik banget, keren bang",  
                "pesan":"semangat menjalani kehidupan kuliah bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "abangnyaa seruu parah, menyala bang",  
                "pesan":"sehat sehat bang, semangat kuliahnya"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kakaknyaa baik banget, humble parah",  
                "pesan":"semangat kuliah kak, bahagia selalu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KGo3Ijk_po69EtsZdxums9Xhq1vULFcX",
            "https://drive.google.com/uc?export=view&id=1Kbohseto8i879zgVfEPIBAY0A5MjmjlM",
            "https://drive.google.com/uc?export=view&id=1Jp2TpeMRjFyxng7vQJjJxG-4noo5gaK9",
            "https://drive.google.com/uc?export=view&id=1JulSRGm0gtK62JzSCIjPuI3X-U2udvi8",
            "https://drive.google.com/uc?export=view&id=1JmVGxcc4ReFF44QEocDZ8FcJsK0SzesH",
            "https://drive.google.com/uc?export=view&id=1Jr4IAutsmfH9avbROAX9GR7OPEPF_4-D",
            "https://drive.google.com/uc?export=view&id=1KVibUDa0sKfs8GNrNKSJewaCtdS4i4aO",
            "https://drive.google.com/uc?export=view&id=1KUXwuaWww76Cjt_BXit8-wMlfRa5F21c",
            "https://drive.google.com/uc?export=view&id=1KGQD_afuXZDGLfYl5_wIfGraifulE7Ng",
            "https://drive.google.com/uc?export=view&id=1KIYLkD5BNGD41dBMdSXG2aJU4OXc1u9Q",
            "https://drive.google.com/uc?export=view&id=1KfuAfQG7FsgOTCpIkuM8JGZKE-kjQIjt",
        ] 
        
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol ",
                "nim": "121450090",
                "umur": "20",
                "asal":"Sidikalang",
                "alamat": "Dekat penjara",
                "hobbi": "Nyari hobi",
                "sosmed": "@Andrianelgaol",
                "kesan": "abang asik parah, mantap bang",  
                "pesan":"Semangat bang semoga lulus tepat waktu, ditunggu gelar barunya"

            },
            {
                "nama": "Adisty Syawaida Ariyanto ",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@Adhistysa_",
                "kesan": "Kakak ini super ramah,keren banget kakak",  
                "pesan":"Bahagia terus ya kakk, semangat selalu ngejar gelarnya"
            },
            {
                "nama": "Nabila azhari ",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "kakak humble bangett, lucu kakaknya",  
                "pesan":"Semangat kuliahnya ya kak, semoga cepet dapet gelar baru"
            },  
            {
                "nama": "Ahmad Rizqi ",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@Ahmad.riz45",
                "kesan": "abang ini ramah, cool banget abang",  
                "pesan":"semoga bahagia terus ya bang, semangat kuliahnya bang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan":"abang gokil parah, enak buat diajak ngobrol, mantap bang",  
                "pesan":"semangat menjalani kehidupan bang, sehat-sehat selalu"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan":"abang keren, asik parah",  
                "pesan":"sehat-sehat bang, semangat kuliahnya"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakaniaa",
                "kesan":" kakaknya humble parah, baik bangett siii",  
                "pesan":"sehat sehat kak, semangat kuliahnya"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanfir",
                "kesan":"keren banget kakak, lucu pliss",  
                "pesan":"sehat-sehat kakak, semangat kuliahnya kak"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alfiagntng",
                "kesan":"kakaknyaa keren bangett,mantap kak ",  
                "pesan":"semangat kuliahnya kak, sehat-sehat kak"
            },
            {
                "nama": "Dhafin Rezaqa Luthhfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnyaa baik bangett, kalem banget abang",  
                "pesan":"semangat kuliahnya bang, sukses selalu"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "12145002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "pliss kakaknyaa lucu banget, seru banget kak",  
                "pesan":"semangat menjalani kehidupan kuliahnya kak, sukses selalu yaa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()
