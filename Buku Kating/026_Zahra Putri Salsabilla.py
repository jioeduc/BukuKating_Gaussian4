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
            "https://drive.google.com/uc?export=view&id=1OjA9sKz2K1Ix8hCvOuyemenUtCeD2R4s",
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
                "pesan":"Tetap amanah sebagai pemimpin"
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
                "pesan":"jangan sampai hilang lucunya"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakak sangat lucu, cantik, dan, seru",  
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
                "kesan": "Kakak hartiti pendiem tapi kadang tiba tiba teriak",  
                "pesan":"semangat mengurus keuangan"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak putri lumayan pendiam dan lucu dan cantik",  
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
                "kesan": "Kakak nadilla baik ",  
                "pesan":"Tetap semangat kak untuk kedepannya"# 1
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

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hqV0avIvNz5cYNsfyySZKdajdtMN2kL3",
            "https://drive.google.com/uc?export=view&id=1hnC0L4x1BL3LwFQ7EsIMi6zlmKVErYJ2",

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
                "kesan": "kak nisa asik banget kalo ngobrol",  
                "pesan":"Jangan lupa berdoa setiap langkah"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "Bang bintang keren bisa manajemen waktu dengan baik",  
                "pesan":"semoga selalu dalam lindungan semua orang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iSTLUWxZWhxyRKx8E77U_iNebWI2thjL",
            "https://drive.google.com/uc?export=view&id=1iq0E7w126XWWQEy1etdrKqws2tPl5PI5",
            "https://drive.google.com/uc?export=view&id=1iVg-LarG9uNIHqcfcErnWXav5hdew-hn",
            "https://drive.google.com/uc?export=view&id=1iW739P0tsIaHhMSx9Br0PGOm4dNZkG5o",
            "https://drive.google.com/uc?export=view&id=1iedQwmKv3GtOIMlw-AOvCAqyywckHHEK",
            "https://drive.google.com/uc?export=view&id=1iZ6kZT5_7xI8SJ6-bHn17uI4x-hoPaGh",
            "https://drive.google.com/uc?export=view&id=1idj6MN3yyTeYSrpOF52rEr5EJ6Jf7KVW",
            "https://drive.google.com/uc?export=view&id=1ifpEglIIDsSy2oyZW7Ny9fFCDcDcTnJb",
            "https://drive.google.com/uc?export=view&id=1ic3SR8ZtuRlTi8UrnqGBvkv5WkkPeLC0",
            "https://drive.google.com/uc?export=view&id=1hx7rJxdSXu2SlBLoV1o8M9FidN9Gz5Xe",
            "https://drive.google.com/uc?export=view&id=1i0E8UaMqLzJJ2WQehgnFhXz75mE5xHiY",
            "https://drive.google.com/uc?export=view&id=1i2jON3RGBnKUzcV-X-OKO2EU3puBb_xf",
            "https://drive.google.com/uc?export=view&id=1iEyFsGNp_a_Hq_al39RYFOaczj-CGnu1",
            "https://drive.google.com/uc?export=view&id=1htgg34GCuJuWCYGLB3cFeKN_crqUCPji",
            "https://drive.google.com/uc?export=view&id=1iJMU8ECnme2LxfYmXWiG3mBc07EDVZvL",
            "https://drive.google.com/uc?export=view&id=1iS40FdS5HihAnVFl17awOJnRTenytHuP",
            "https://drive.google.com/uc?export=view&id=1iKQqKdbVqxLBfwMiXGwjHy7DKx-5pnQF",
            "https://drive.google.com/uc?export=view&id=1iNvcHn8VfJY9SXRblwVgjPdoHNuWYTOU",
            "https://drive.google.com/uc?export=view&id=1iQe6M2a6ULq_WrJyuVOXvnr-N2tWW81-",
            "https://drive.google.com/uc?export=view&id=1iMBssV4k35ZZ2sMEAz1SeaF2E7PJJJRv",
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
                "kesan": "Kakaknya asik tapi agak seram pas nunjuk",  
                "pesan":"semoga lulus tepat waktu."
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan":"kak abeth cantik dan seru banget plus lucu",  
                "pesan":"semangat dalam hidup"
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
                "pesan":"Terus semangat kuliahnya Kak dan semoga berhasil dan sukses meraih cita-cita."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami",
                "kesan": "kakak inicantik banget dan pinter",  
                "pesan":"semoga sukses kak afifah"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakanya menyenangkan dan sangat baik hati",  
                "pesan":"semoga bisa selalu menjadi motivasi untuk orang banyak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakanyanya seru dan asik dan cantik",  
                "pesan":"Semangat terus kuliahnya Bang dan semoga sukses mengejar impian."
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya seru banget",  
                "pesan":"Semangat Bang kuliahnya dan sukses."
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "abangnya asik dan ceria",  
                "pesan":"jangan lupa kepada sang pencipta"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya menyenangkan dan baik",  
                "pesan":"trus menjadi contoh yang baik"
            },
            { 
                "nama": " Deyvan Loxefal", 
                "nim": " 121450148 ", 
                "umur":  "21", 
                "Asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanlo", 
                "kesan": "Kakaknya asik dan chill",   
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai." 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamy", 
                "kesan": "seru banget kakaknya, lain waktu ngbrol lagi kak",   
                "pesan" : "semoga selalu asik kak"
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "Kakaknya sangat humoris ",   
                "pesan":"jangan menyerah untuk mencapi apa yang di mau bang" 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "bang kemas pinter banget",   
                "pesan":"jangan bosen ngajari kita ya bang." 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Kakaknya asik dan seru dan baik hati serta lucu.",   
                "pesan":"semoga tercapai semua angan - angan setinggi langitnya" 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya ask dan murah senyum",   
                "pesan":"jangan pernah sendirian kalo ada masalah" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya sangat asik dan lucu",  
                "pesan":"Semangat terus Kak untuk apapun itu"
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya lucu dan baik",  
                "pesan":"kapan kapan ajari lomba ml bang"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "kak jac sedikit jamet tapi aku suka skaliee",  
                "pesan":"semangat mengurus anak-anak gauss yang membandel"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya sangat seru",  
                "pesan":"Semangat terus dan sehat selalu"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "kakaknya murah senyum ",  
                "pesan":"semangat kak kuliahnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kgz0m1Qhnj-xVqHzlnOP8D1d_gB2he9L",
            "https://drive.google.com/uc?export=view&id=1lyiZh2C-qYoswqp-R1bwoQ8JetTME9lv",
            "https://drive.google.com/uc?export=view&id=1m21WqxLUd0qsincxQTMiWKKHP257fPR1",
            "https://drive.google.com/uc?export=view&id=1lApeAacJoWQSU6Dc-Q-p20959WuQOGKj",
            "https://drive.google.com/uc?export=view&id=1lCChxzhQvhCtXbPbnGq5duDV5hWL0pdc",
            "https://drive.google.com/uc?export=view&id=1l_XG-lT0pDOKEBrQpU5X6ZmbWIquG-a0",
            "https://drive.google.com/uc?export=view&id=1lLlPWKj8LbekAg0YdHfZTdBgDNnBF4_J",
            "https://drive.google.com/uc?export=view&id=1l2p5Wq65asKbNYSbczoENp7qdF_w75XP",
            "https://drive.google.com/uc?export=view&id=1le66qmUL0kq2Aa6zQlfovaOu6bG8CKyx",
            "https://drive.google.com/uc?export=view&id=1lgyH2VY5ToZXIlxl7_HZFlE7eDPHp8VM",
            "https://drive.google.com/uc?export=view&id=1lgXMDPFs7LXbyREhkeBG4HBbuxj9guDb",
            "https://drive.google.com/uc?export=view&id=1kpRYVybsQenlHxZ-0eXCYh4yzguzZNOv",
            "https://drive.google.com/uc?export=view&id=1lngIiJZmNbRXeQc_Z6GsyXSok4lzp3xU",
            "https://drive.google.com/uc?export=view&id=1lISXsIV8DCNYK_ovPPV9G9W9pFVt3KHi",
            "https://drive.google.com/uc?export=view&id=1ks6Q5HASOPfVquRUWN5KO2VMwusBwn_P",
            "https://drive.google.com/uc?export=view&id=1l4lXxWSeMZ2AnrSaxFwpLURRQiNAYHWP",
            "https://drive.google.com/uc?export=view&id=1lK3BK-mnv2IzcQPYMEpP0VhmsaE75XQs",
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
                "kesan": "Suka sama namanya, gak deng orangnya juga :D",  
                "pesan":"Semanat terus kak jangan lupa istirahat"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Eak Bang Sahid",  
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
                "kesan": "Awalnya bingung ternyata kembar :D",  
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
                "kesan": "Abangnya keren banget?!",  
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
                "kesan": "Suka banget sama kakaknya?!",  
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
                "kesan": "Kakaknya ramah benget?!",  
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
                "kesan": "Suka sama Kak Rut...",  
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
                "kesan": "Senangnya bertemu kakak NIM :D",  
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
                "kesan": "Abangnya seru abis",  
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
                "kesan": "Gokil",  
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
                "kesan": "Abangnya pendiem kah?",  
                "pesan":"Semangat terus bang"
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
            "https://drive.google.com/uc?export=view&id=1h_RVXWsxyK69QAuZowPUAyFUoeSehVQ7",
            "https://drive.google.com/uc?export=view&id=1hYacDOjUlqSNiWqN9Bdb-E49AleY80Fc",  
            "https://drive.google.com/uc?export=view&id=1hd_9dFFbD9ZqT__z8uwDcaCi0IXekMKD",
            "https://drive.google.com/uc?export=view&id=1h572QRUFYwzdlQLsO9y78nS_bFgWKG2V",
            "https://drive.google.com/uc?export=view&id=1gpWCENrhpByWzvh-gggEAuFGRurl6vu2",
            "https://drive.google.com/uc?export=view&id=1h4PUdkjPXGq6wq4gupSdCOUjBXdKhTzE",
            "https://drive.google.com/uc?export=view&id=1hEWY5OM4AP82HNhX5iJb-A3FHJvV2C-p",
            "https://drive.google.com/uc?export=view&id=1gdGcMtFCPwk0zPeZHAalKcGEgenn9can",
            "https://drive.google.com/uc?export=view&id=1gid6VH-35sf2poGsoaw6EGutI-QHjRRO",
            "https://drive.google.com/uc?export=view&id=1gnthtYVIQjrp4rhAVIp9pKJfTUe6PLzO",
            "https://drive.google.com/uc?export=view&id=1gnjK8F6tsKRf6Axn_XQEwiegWbn4TbB6",
            "https://drive.google.com/uc?export=view&id=1hGJya9qm1zCm2NkIyeoFLTBGC-A2o_VI",
            "https://drive.google.com/uc?export=view&id=1hNmieV0nH4JVlvPbRv66FbHDEre4RSEr",
            "https://drive.google.com/uc?export=view&id=1h9cGDN7eUi0pGQpqJug9MS6kkp8ZKsxw",
            "https://drive.google.com/uc?export=view&id=1hS05xjuWAx0RJ9R-MHhmijg8_7Vcr9N9",
            "https://drive.google.com/uc?export=view&id=1hb0FPZXuR2HTeqQDztAuMVEXu1qPLRhd",
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
                "kesan": "Kakaknya Sangat Asik",  
                "pesan":"Semangat Kuliahnya kakak"
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
                "kesan": "kakaknya keren",  
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
            "https://drive.google.com/uc?export=view&id=1kPKewr-H7okTd4gEhuz-UiWgJFBlBBdA",#1
            "https://drive.google.com/uc?export=view&id=1k7JEYHeiFWnitBoXa62FlvZYHAZpTuVF",#2
            "https://drive.google.com/uc?export=view&id=1kE0XkxudU1yFS41M8sUglO-gCeXA1qQW",#3
            "https://drive.google.com/uc?export=view&id=1k36Wf1png7RE8-HCwKgEzBnRJfJ7xs4W",#4
            "https://drive.google.com/uc?export=view&id=1jiyzjAp3d-vv1YGjbSxy5Zwx9FPfiWx_",#5
            "https://drive.google.com/uc?export=view&id=1kBokKj_LdLFTaz8AkiSrLyF3-HXcGliD",#6
            "https://drive.google.com/uc?export=view&id=1kMPzbWcjiSnMBQ3iLxMVAP0JC4cfzI8w",#7
            "https://drive.google.com/uc?export=view&id=1jefO5vmC-xaNP19p_TOq1k3Skqch5Ba8",#8
            "https://drive.google.com/uc?export=view&id=1k28dUwfxN8JnnaC9dpCGwrCcqgwfbtl-",#9
            "https://drive.google.com/uc?export=view&id=1jpjcBJTv0-P_teWY38STwZdS6HB6A_QU",#10
            "https://drive.google.com/uc?export=view&id=1jrOsetMT0alfStmmr5aud4308FGKNxLd",#11
            "https://drive.google.com/uc?export=view&id=1kAPrinklfRGHXNVgnMGo3oxFhbu_WbQ_",#12
            "https://drive.google.com/uc?export=view&id=1jpTwWh7MU-Kp02h2_1jQ7vaTUHQwdVj8",#13
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
                "kesan": "Kakaknya baik,, positive vibes",  
                "pesan":"semangat terus kuliahnya kak, semoga semua urusannya diperlancar!!"# 2
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "Kakak sangat membantu dan mudah diajak bicara.",  
                "pesan":"Semoga lancar semua urusan Kakak, sukses terus!!"# 3
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
                "pesan":"Semoga Kakak sukses dalam setiap langkah ke depan!!"# 4
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakak luar biasa dalam membimbing.",  
                "pesan":"Semoga kebahagiaan selalu menyertai Kakak!!"# 5
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@lexanderr",
                "kesan": "Kakak memiliki kepribadian yang ramah dan menyenangkan.",  
                "pesan":"semangat terus kuliahnya kak !!!"# 6
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Kakak sangat sabar dalam mengajarkan hal baru kepada kami.",  
                "pesan":"Semoga Kakak selalu diberi kemudahan dalam setiap usaha!!"# 7
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar.resdika",
                "kesan": "Kakak selalu berusaha menciptakan suasana yang menyenangkan.",  
                "pesan":"Semoga semua usaha Kakak membuahkan hasil yang memuaskan!!"# 8
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
                "pesan":"Semoga Kakak selalu dikelilingi orang-orang baik!!"# 9
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
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!!"# 10
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
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!!"# 11
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Kakak sangat memotivasi",  
                "pesan":"Semoga Kakak selalu berhasil dalam semua!!"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Kakak sangat hebat",  
                "pesan":"Semoga Kakak selalu selamat"# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
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
            "https://drive.google.com/uc?export=view&id=1VXAkQfuQSrx3a0luWVHoZeRuNViowbuh",
            "https://drive.google.com/uc?export=view&id=1VXAkQfuQSrx3a0luWVHoZeRuNViowbuh",
            "https://drive.google.com/uc?export=view&id=1VXAkQfuQSrx3a0luWVHoZeRuNViowbuh",
            "https://drive.google.com/uc?export=view&id=1VXAkQfuQSrx3a0luWVHoZeRuNViowbuh",
            "https://drive.google.com/uc?export=view&id=1VXAkQfuQSrx3a0luWVHoZeRuNViowbuh",
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
                "kesan": "kakak ini asik sekali",  
                "pesan":"semoga bahagia dengan pilihan nya bang"
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
                "pesan":"semangat ngejar cita - citanya kak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Kakak dhea kelihatan aura anak pinter nya",  
                "pesan":"semangat kak buat belajarnya"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "Bang jeremy asik dan suka becanda , seru",  
                "pesan":"semangat bang ngejar cita - cita nya"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "sangat memotivasi dan lucu dan murah senyum",  
                "pesan":"semangat bang untuk ngejalanin hidup"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "Abang ini sangat kalem dan cantik",  
                "pesan":"semangat kak ngejar yang tidak pasti hehe"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "abang ini sangat baik dan seru",  
                "pesan":"semangat bang untuk hidup"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "saya terkesan dengan kakak ini karna baik",  
                "pesan":"selamat berjuang dimanapun dan kapanpun!"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@aimnn.as",
                "kesan": "abang ini sangat seru dan humoris tapi pendiem",  
                "pesan":"semangat kak ngejar cita - cita nya"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kak anisa dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya!"
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
                "kesan": "Kak anisa dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya!"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Kak anisa dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya!"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@akmal.faiz",
                "kesan": "Kak anisa dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "Kak anisa dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak belajarnya!"
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
                "pesan":"semangat terus kak belajarnya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fjL4e6p11hkV-i3CoA2CopO2HiatVW-J",
            "https://drive.google.com/uc?export=view&id=1fh9ouEnyJFg2lmz1nydLKC8zvjREIdwI",
            "https://drive.google.com/uc?export=view&id=1fXBmvWZZXwhmi9nTgOiQI_GoUsIKUR3-",
            "https://drive.google.com/uc?export=view&id=1gEOKg37dH-kMgBY5T8dZkH4DB95xiVdv",
            "https://drive.google.com/uc?export=view&id=1gMG-Zb2HiudX5KEHgcLGpp73zdr8fxFW",
            "https://drive.google.com/uc?export=view&id=1gEqEH2RRC4iSnFyCdcjkZerFgOSPprPL",
            "https://drive.google.com/uc?export=view&id=1fqT56goY7p6463t5ZS9dj8yWW6sghZB1",
            "https://drive.google.com/uc?export=view&id=1fr2vgh6HESLlyM6IarrVfjLnKamg6M7m",
            "https://drive.google.com/uc?export=view&id=1gDA-8Lt5Y7hXktt6H5m1LcnMWPAQRdqW",
            "https://drive.google.com/uc?export=view&id=1g41zyAqpDty2Ohkr7R30WE5d8BUbDUa_",
            "https://drive.google.com/uc?export=view&id=1gTDiaPVSI4XgTNPtO8U_oteHn1J1_dyu",
            "https://drive.google.com/uc?export=view&id=1ewq52q3WsBhg1p1XtmP2PZvc30xKWzss",
            "https://drive.google.com/uc?export=view&id=1fIk-6ixZGlvQoe2W4g-1D0MmFaK2u_kh",
            "https://drive.google.com/uc?export=view&id=1fTKVzxqQbZOOxxCQmch8KtGkqMXc6u2L",
            "https://drive.google.com/uc?export=view&id=1fWGS8eFoArggCZH5wTwERaD8F3ac_E2r",
        ]

        data_list = [
            {
                "nama": "Wahyudianto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "@wayyulaja",
                "kesan": "Bang Wahyu asik banget",  
                "pesan":"Sehat dan bahagia selalu bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@Elokviola",
                "kesan": "Kak Elok baik bangettt",  
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Kalau kata aku, Kak Cybel punya aura sekretaris",  
                "pesan":"Semangat terus ngontennya kak"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "Kak Cia ramah banget",  
                "pesan":"Semangat gasprak, ngonten, dan belajarnya kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "Kak Neli imut bener",  
                "pesan":"Semangat terus untuk brkembang ak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "Kak Try Yani baik banget",  
                "pesan":"Semangat kakak cantik!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Bang Kaisar kocak abiss",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kak Dwi pendiem ya?",  
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@aimnn.as",
                "kesan": "PDD abadinya Sains Data",  
                "pesan":"Semangat jadi dokumentasi bang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kak Nasywa baik banget",  
                "pesan":"Terus jadi orang baik kak"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kak Priska ramah banget?",  
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
                "kesan": "bang Arsal kece bener",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Bang Abit imut",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@akmal.faiz",
                "kesan": "Bang Akmal baik banget banget banget",  
                "pesan":"Semangat terus untuk jadi orang baik bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "Bang Mawan mood buster",  
                "pesan":"Semangat terus jadi orang baik bang"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kakak imut banget?!",  
                "pesan":"Semangat terus ngedesainnya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Q7-9Z5lJ3By4ZG-Wv0O_aa5umgQWF4RN",
            "https://drive.google.com/uc?export=view&id=1QFEDevvsb7V8FbnObYL9mggaCUq0d7hf",
            "https://drive.google.com/uc?export=view&id=1QBjLEwLX7YME5OUZyGnfztOP86HxeXx2",
            "https://drive.google.com/uc?export=view&id=1QNJl0YOhlSAJnNILqgu9GW967kaodDwG",
            "https://drive.google.com/uc?export=view&id=1QYbF4PB2JHv9QLgaL0WR1BqyYk1mSUnm",
            "https://drive.google.com/uc?export=view&id=1QTiAfMPQ7bXz_SWoydOX17kKRfX64owP",
            "https://drive.google.com/uc?export=view&id=1QCqcts9kBlh06fghOXJU12eLBb0QH1cH",
            "https://drive.google.com/uc?export=view&id=1Q1036JV_CSntthQw_o9B6BnEDsGWEDYW",
            "https://drive.google.com/uc?export=view&id=1Pt0wsVDZdDsd9XnAGtnB1vclnUNl5pio",
            "https://drive.google.com/uc?export=view&id=1Q5VVbfaDYb1yX8ojxflUj3GdGHLarreN",
	    "https://drive.google.com/uc?export=view&id=1Q1re9TUKPaeTQi3hxM-IZK0_b626W7CS",

        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "20",
                "asal":"Cirikalang",
                "alamat": "Dekat penjara",
                "hobbi": "Nyari hobi",
                "sosmed": "@andrianelgaol",
                "kesan": "Bang Adrian keren banget",  
                "pesan":"Semangat bisnisnya bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton film",
                "sosmed": "@adhistysa_",
                "kesan": "Kak Adisty keren banget?",  
                "pesan":"Semangat kuliahnya kak!"
            },
            {
                "nama": "Nabila azhari",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "Kec bener",  
                "pesan":"Semangat menghitung duitnya kak!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "Airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "Cool bet",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Bang Danang seru banget ><",  
                "pesan":"Stay positive!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "hobbi": "Jl.lapas",
                "sosmed": "@farrel__julio",
                "kesan": "Menyala capo Damaskus!",  
                "pesan":"Semangat terus jadi capo Damaskus bang!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakaniaa",
                "kesan": "Kak Tessa humble bener",  
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanfir",
                "kesan": "Kak Nabilah inspiratif banget",  
                "pesan":"Semangat menjadi dutanya kak!"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alfiagntng",
                "kesan": "Kak Alvia imut banget?",  
                "pesan":"Semanat terus Kak Alvia!"
            },
            {
                "nama": "Dhafin Rezaqa Luthhfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "Cool banget...",  
                "pesan":"Semangat terus Bang Dhafin!"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "12145002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "Kak Elia lucu banget?!",  
                "pesan":"Semangat terus kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()
