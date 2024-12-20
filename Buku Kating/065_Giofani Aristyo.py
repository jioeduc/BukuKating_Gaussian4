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
            "https://drive.google.com/uc?export=view&id=1BJtmp3FopONZXAlLXqUWbJM8RygCHZG0",
            "https://drive.google.com/uc?export=view&id=1BLY5LuYAWIMn5v1oQ60_alGMNBHDrYHy",
            "https://drive.google.com/uc?export=view&id=1BLg_0PZHDue1fC2zyOEE0s3pknGgKc03",
            "https://drive.google.com/uc?export=view&id=1BKI6c6rxD1gD0NbPPQjV5AiopL8i9FM6",
            "https://drive.google.com/uc?export=view&id=1BMdrAVJVweDCJHsyl1dQ5efoM9xIaKVP",
            "https://drive.google.com/uc?export=view&id=1BJFSl3pCj43G6wT9inb5gl3UIvhYW5pR",
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
                "kesan": "Bang gumi sangat menginspirasi dan penjelasannya sangat informatif",  
                "pesan":"semangat buat abang semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abang ini asik dan seru, dan sepertinya jago bahasa lampung",  
                "pesan":"Semangkat bang kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak nya asik dan informasinya sangat jelas",  
                "pesan":"Semangkat kuliah kak, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak titi asik, tapi keliatannya yang paling kalem",  
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
                "kesan": "Kakak nya banyak diam, tapi keliatannya kakaknya asik",  
                "pesan":"semangat terus kuliahnya kakak, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@nadillaandr26",
                "kesan": "Kak nadilla juga banyak diam, tapi keliatannya juga asik",  
                "pesan":"semangat selalu kak kuliahnya, semoga bisa lulus tepat waktu"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Pl2TNCB1A7dm6yvzMFjfZRQOdgKM8I8g",
            "https://drive.google.com/uc?export=view&id=1PZscObTUTsiLAceFyRLNziAzw74N3MBJ",
            "https://drive.google.com/uc?export=view&id=1P_2Vv90edsVs3LRB0XwgWGVAo5j7MwhB",
            "https://drive.google.com/uc?export=view&id=1PcUUGiw7UjeHY0qY5Wxb4I6RO--UoJnX",
            "https://drive.google.com/uc?export=view&id=1Rf8UysKxY5AT1HsjkpuqoI0rj1UHBx7u",
            "https://drive.google.com/uc?export=view&id=1Plc12ULmjbIEtxoq7YG95Cx8po3_CtuE",
            "https://drive.google.com/uc?export=view&id=1PhuhWyVXKvi3ly-OiMLV75hGNBoSJLum",
            "https://drive.google.com/uc?export=view&id=1PgZKsqSTM4uMfzCCbpApj-GW0eDlfMom",
            "https://drive.google.com/uc?export=view&id=1PdTF8CPHteCyeYCFPAZ_214-Qc28RJOf",
            "https://drive.google.com/uc?export=view&id=1PhwK1pYlstZ3YhUgGiFB1tB0i_u0xsC3",
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
                "kesan": "Kakaknya aktif banget",  
                "pesan":"semangat terus kuliahnya kakak, semoga dapat lulus tepat waktu"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "12140124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini baik sekali, sayang belum sempat ngobrol banyak",  
                "pesan":"semangat terus kuliahnya kak, semoga lulus tepat waktu"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya juga baik dan ramah sekali, tapi belum sempet ngobroll lebih banyak",  
                "pesan":"semangat terus kuliahnya kak, semoga lulus tepat waktu"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang nya aktif banget",  
                "pesan":"semangat terus bang kuliahnya, semoga lulus tepat waktu"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya ramah banget",  
                "pesan":"semangat bang kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang nya sedikit pendiam, dan terlihat wibu, tapi baik dan ramah banget",  
                "pesan":"semangat terus bang kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya baik banget, enak juga ngasprak ads nya",  
                "pesan":"semangat bwang kuliahnya, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini terlihat pendiam dan cantik",  
                "pesan":"semangat terus kuliahnya kakak, semoga lulus tepat waktu"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak menyenangkan dan asik pembawaannya",  
                "pesan":"semangat terus kuliahnya kak, semoga lulus tepat waktu"
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
                "pesan":"semangat terus kuliahnya kakak, semoga lulus tepat waktu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QlNVcGNvijdA81ZDIbvFGaUQsahk7pf8",
            "https://drive.google.com/uc?export=view&id=1Qm_JkPfrk5_uwQRBKk3uMDrfnjZKivx4",
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
                "kesan": "Kakaknya inspiratif, dan sangat berwibawa",  
                "pesan":"Semangat kuliahnya kak, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang bintang asik dan inspiratif banget",  
                "pesan":"Semangat terus bang kuliahnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1L4l8UD7cx43-ymnEH045TOkl0FodTBsp",
            "https://drive.google.com/uc?export=view&id=1LZG2Q9VZSJpjBwzPrnrmLR3vmjiinuAf",
            "https://drive.google.com/uc?export=view&id=1L9TA_TO0pH5PoOSrrjZud7v0S9FGZqxq",
            "https://drive.google.com/uc?export=view&id=1L5fq2axaqwe3MdWeYZyT3ONtfvxGkwx5",
            "https://drive.google.com/uc?export=view&id=1LIwvWW0nDt4Uiik1oX5sbvfyYRAkYGfs",
            "https://drive.google.com/uc?export=view&id=1LEWWBARiJMOfQE76MDQam4GvAbvjVtp7",
            "https://drive.google.com/uc?export=view&id=1LXVlAdAU9YOOD-bAW7q9FWMuTUo0ckD2",
            "https://drive.google.com/uc?export=view&id=1LFyF-nIBO4z3L4DN2THJ6_ST6PQW90fh",
            "https://drive.google.com/uc?export=view&id=1LTI16sfaBWuNc-9N2GZugexma2XlaJlc",
            "https://drive.google.com/uc?export=view&id=1Kr1vdXE53e5CyVQIynw-_pnxo6-YyHr1",
            "https://drive.google.com/uc?export=view&id=1KuvnDu2v2h8QZGURQtX9aNgxRsFeDDsU",
            "https://drive.google.com/uc?export=view&id=1KtJKg5x_WN3CRJJFFxDDgUc69GSJ2Gor",
            "https://drive.google.com/uc?export=view&id=1Kt6Sumv5O5uFA5cefLVD2aygGLVHrVzM",
            "https://drive.google.com/uc?export=view&id=1KruvYK7WFL6swMLaxf9IHSSKjrJ2R70f",
            "https://drive.google.com/uc?export=view&id=1KuKy7yN5i7vUEsq6Cp2K1FYjjt9MVUv9",
            "https://drive.google.com/uc?export=view&id=1L5BwhBIkwFpbA8P3lT3-XjoKHKNVDMw2",
            "https://drive.google.com/uc?export=view&id=1L02KTwC5slPp8U3vG5jVSBJL5TGWmkXb",
            "https://drive.google.com/uc?export=view&id=1L4d6MrQTpiFzM2Ymy7-uS0ao3W1DwGlp",
            "https://drive.google.com/uc?export=view&id=1L02OtvTYjtamFdSanhaaINPA-ONh60q_",
            "https://drive.google.com/uc?export=view&id=1KxNj3pODO8enFJZF421QhQiTN3yldqLB",
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
                "kesan": "Bang econ sangat profesional orangnya",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya ternyata ramah, seru, dan asik",  
                "pesan":"Semangat terus kak kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Afifah ternyata orangnya seru dan asik.",  
                "pesan":"Terus semangat kuliahnya Kak dan semoga berhasil dan sukses meraih cita-cita."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami_",
                "kesan": "Kak Allya ternyata asik banget dan seru diajak ngobrol",  
                "pesan":"Semangat terus kak kuliah nya, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kak eksanty asik dan aktif banget",  
                "pesan":"Semangat terus kuliahnya, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakanya suka senyum",  
                "pesan":"Semangat terus kak kuliah nya, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya terlihat diam, tapi keliatannya juga asik",  
                "pesan":"Semangat Bang kuliahnya, dan semoga lulus tepat waktu"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "bang deri asik banget",  
                "pesan":"Semangat terus kuliahnya bang, semoga lulus tepat waktu dan kapan-kapan scrim ml"
            },
            {
                "nama": "Oktavia Nurwinda Puspitasari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya terlihat pendiam dan dingin",  
                "pesan":"Semangat terus Kak kuliahnya, semoga lulus tepat waktu"
            },
            { 
                "nama": " Deyvan Loxefal", 
                "nim": " 121450148", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanloo", 
                "kesan": "bang deyvan orangnya asik dan lucu.",   
                "pesan":"semangat terus bang kuliahnya, semoga lulus tepat waktu" 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamg", 
                "kesan": "Kakaknya cantik, tapi ga sempet ngobrol banyak",   
                "pesan":"Semangat terus Kak kuliahnya ,semoga bisa lulus tepat waktu" 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "Bang jo paling asik",   
                "pesan":"Semangat terus bang semoga bisa lulus tepat waktu" 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "bang kemas keren dan asik, dan jago ngoding",   
                "pesan":"Semangat terus bang kuliahnya ,semoga bisa lulus tepat waktu, dan ditunggu tutor ngodingnya" 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "bang sahid kayanya gamers banget",   
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus tepat waktu" 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya asik dan seruu",   
                "pesan":"Semangat terus Kak kuliahnya, semoga bisa lulus tepat waktu" 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya asik dan suka bikin suasana lucu.",  
                "pesan":"Semangat terus bang kuliahnya dan semoga semua cita-citanya tercapai."
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "bang gede asik, apalagi kalo lagi mabar ml",  
                "pesan":"kapan kita by one ml bang"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "kakak yang paling cantik dan ramah di PSDA",  
                "pesan":"Semangat terus Kak kuliahnya sama mengurus anak-anak gaussiannya"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "bang rafly sepertinya pengen banget scrim ml",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "awalnya bingung ternyata kembar :D",  
                "pesan":"Semangat terus Kak kuliahnya, semoga bisa lulus tepat waktu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A6HSvHwaq3xo8s6yX8Fgv4itJNmmu1Jq",
            "https://drive.google.com/uc?export=view&id=1AEY-j_CVFBch2xKTGaOZI9XN3395GqiO",
            "https://drive.google.com/uc?export=view&id=19nmaPW4KiSXMM4lmJ6-WOJeDoaqcfpoM",
            "https://drive.google.com/uc?export=view&id=19okVBJBEllAt0no8nJIDzuP1M4c4vrrX",
            "https://drive.google.com/uc?export=view&id=1QurzIt_q2rDwnaxjiIffTLt3UtFrKxMI",
            "https://drive.google.com/uc?export=view&id=1ACBzdfW4x40p8lronkcYBcD7SHNsX871",
            "https://drive.google.com/uc?export=view&id=1ABr-7sULFdKc0IB5grgxCaoUmDjeF4dR",
            "https://drive.google.com/uc?export=view&id=1AKkdohTijcOCqS35CNigrg4sl22CcJGA",
            "https://drive.google.com/uc?export=view&id=1ACL0n4DR1ZB7MrP-TyjAEEPcxFL7yyCR",
            "https://drive.google.com/uc?export=view&id=1AOrrnYRhVr4CxkM7VPi3YO1a0vtMmFyg",
            "https://drive.google.com/uc?export=view&id=1ANVocxUp2OZUQExoAA5_jSsTy3EHGm_T",
            "https://drive.google.com/uc?export=view&id=1ADHqSP5ov7rfzWOGHVeRYwPeUaSPMFJr",
            "https://drive.google.com/uc?export=view&id=1QsT5YsMTohRnxsqLBACq_14F-8OGaeec",
            "https://drive.google.com/uc?export=view&id=1Qtokd41owlKcYnaaI0FHvnv5Cc77l0nX",
            "https://drive.google.com/uc?export=view&id=1ACymEUhabYvjCZzUkyNzoEm5DII5zolA",
            "https://drive.google.com/uc?export=view&id=1QsKYybNFE82xSfsS1PTtr1OjxOdMH_Q7",
            "https://drive.google.com/uc?export=view&id=1A9A_CS478zk_sSlLDJW4ZnNWk3_Aoh6p",
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
                "kesan": "Bang rafi terlihat sangat pintarr",  
                "pesan":"Semangat terus bang bang kuliahnya, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Annisa Novatika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl.Pulau Sebesi, Sukarame",
                "hobbi": "baca novel",
                "sosmed": "@anovavona",
                "kesan": "kak anova asik orangnyaa, namanya sains data banget",  
                "pesan":"Semanat terus kak kuliahnya, semoga bisa lulus tepat waktu"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang paling mantap ini, kebanggaan warga gaussian",  
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
                "kesan": "bang fadhil sepertinya asik, tapi pendiam",  
                "pesan":"Semangat terus bang kuliahnya, semoga lulu tepat waktu "
            },

            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "bang regi asik banget orangnya, dan aktif banget",  
                "pesan":"Semangat terus bang kuliahnya, semoga lulus tepat waktu"
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
                "pesan":"Semangat terus kak kuliahnya, semoga lulus tepat waktu"
            },

            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@here.am.ai",
                "kesan": "Abangnya keren banget",  
                "pesan":"semangat bang semoga juara ositera matematika"
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "kakaknya asik dan menyenangkan",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus tepat waktu"
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya ramah benget, dan terlihat pintar",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus tepat waktu"
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
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus tepat waktu"
            },

            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "Kak rut terlihat pendiam, tapi ternyata asik",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus tepat waktu"
            },

            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kak puspa asik banget orangnya",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus tepat waktu"
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhm_adityaa",
                "kesan": "Abangnya seru abis, tutor figmanya sangat bermanfaat",  
                "pesan":"Ditunggu bang tutor figmanya lagi :D"
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "bang eggi ggwp",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus tepat waktu"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakaknya keliatannya asik sekali",  
                "pesan":"Semangat terus kak kuliahnya, semoga bisa lulus tepat waktu"
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abangnya terlihat ceria seperti namanya :D",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus tepat waktu"
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa gokil abiss, penutor handal",  
                "pesan":"Semangat membantu bocah-bocah Gauss bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GOuvbDufkT2lmvQcBNQAgYNmZ_aXS3_-",
            "https://drive.google.com/uc?export=view&id=1GS2igEhIVtRP95SGBHzxAYaBnVKzjFnq",  
            "https://drive.google.com/uc?export=view&id=1GVffWSbE5iZR7OFzH6CAHA5APaVPqlaD",
            "https://drive.google.com/uc?export=view&id=1Gagk2QBM7UCiIMKyOhEEjfw0jtHUkuqJ",
            "https://drive.google.com/uc?export=view&id=1GUFh12BlNOjr0a4fcAB7wvWRrqRtVNhJ",
            "https://drive.google.com/uc?export=view&id=1GR6pMcMRNBaGTtRHQ5djIkYe1whudpYO",
            "https://drive.google.com/uc?export=view&id=1GkDJfN0rxAtIPgbl-iGvqjOuvXuuGSiu",
            "https://drive.google.com/uc?export=view&id=1Gu7LiDkOJC5jgkrvP5bYQcP00B4ErxH8",
            "https://drive.google.com/uc?export=view&id=1GsnQF5iWHOfl6i_PV-NICn-0cXxHt_FI",
            "https://drive.google.com/uc?export=view&id=1Glt12d2oYM8pTFrK7GO0tP8bmnjf1rBe",
            "https://drive.google.com/uc?export=view&id=1GqyU_PdUs7CWiueVakqoG8dRsrqkgDse",
            "https://drive.google.com/uc?export=view&id=1GnzC0xkO0jaCMt6b7IJK8QKLLGLd8rLa",
            "https://drive.google.com/uc?export=view&id=1GntaFcT8QODLZDJUygVXLgcjAvFyl8E8",
            "https://drive.google.com/uc?export=view&id=1GgLF5tn6uJHFzEZqCj35aQSDu0I5N4tJ",
            "https://drive.google.com/uc?export=view&id=1GVwucDwfQRNtMebs8_wHj5OCUyVEQ-nN",
            "https://drive.google.com/uc?export=view&id=1OBx99MgPmggN6Yt3KC64yMyQ9N9tALoP",
        ]
        data_list = [
            {
                "nama": "Yogy Sa`e Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@yogyyyyyyy",
                "kesan": "abang namanya mirip karakter anime",  
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
                "kesan": "Kakaknya asik dan menyenangkan",  
                "pesan":"Semangat Kuliahnya Kakak semoga lulus tepat waktu dan cita-cita nya tercapai"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya kalem tapi asik",  
                "pesan":"semangat kuliahnya kak, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kak dea lucu dan asik sekalii",  
                "pesan":"semangat kak kuliahnya semoga lulus tepat waktu"
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
                "pesan":"semangat kuliahnya kak, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "bang tobias asik bangett, dan rambutnya paling keren",  
                "pesan":"semangat kuliahnya bang, semoga lulus tepat waktu"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya keliatan jago main ml",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abang ini kelihatan seru, sayangnya ga sempat ngobrol",  
                "pesan":"semangat kuliahnya bang, semoga lulus tepat waktu"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "abang nya asik dan suka melawak",  
                "pesan":"semangat kuliahnya bang, semoga lulus tepat waktu"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfawww",
                "kesan": "kakak nya seru dan menyenangkan",  
                "pesan":"semangat kuliahnya kakak, semoga lulus tepat waktu"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "abang nya terlihat pendiam",  
                "pesan":"semangat kuliahnya bang, semoga lulus tepat waktu"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "17",
                "asal":"Bogor",
                "alamat": "Pemda",
                "hobbi": "Bersholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kakak terlihat familiar, ternyata mirip temen sma",  
                "pesan":"semangat kuliahnya kakak, semoga lulus tepat waktu"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak ini asik bangett",  
                "pesan":"semangat kuliahnya kakak, semoga lulus tepat waktu"
            },
            {
                "nama": "Asa Do`a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Ening",
                "alamat": "Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini lucu dan kalem",  
                "pesan":"semangat kuliahnya kakak, semoga lulus tepat waktu"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Planning Content",
                "sosmed": "@jasminednva",
                "kesan": "Kakak nya lucu dan informatif",  
                "pesan":"semangat kuliahnya kakak, semoga lulus tepat waktu"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Main Volly",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kakak nya aktif banget, dan asik diajak ngobrol",  
                "pesan":"semangat kuliahnya kakak, semoga lulus tepat waktu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1acvmUDTA6d41VnG3h6oMl7ffUQo9uYGv",#1
            "https://drive.google.com/uc?export=view&id=1aW8_qCYQ0y47EZLf-N-qYLR043fDjyi7",#2
            "https://drive.google.com/uc?export=view&id=1a_mSWe4wWmPubZoD4gXGmkQs2t-CTnnl",#3
            "https://drive.google.com/uc?export=view&id=1acROqmNC4JgsVe8bdzT8BE5GpLY5J2Nc",#4
            "https://drive.google.com/uc?export=view&id=1amLlm8zkLDeWJFlPRne4B1C2xH2yRhi4",#5
            "https://drive.google.com/uc?export=view&id=1aYHt6Anbhvc9Ewd_sjPvlXT7FVpHbW1E",#6
            "https://drive.google.com/uc?export=view&id=1abvZPVOyJARFPuvJmbFT5H1oERNmtyRh",#7
            "https://drive.google.com/uc?export=view&id=1an10WFTpmBKyWuXEgu3XcmcjnlAhZ5-l",#8
            "https://drive.google.com/uc?export=view&id=1aew24yN3sHBtbWObhpJSo-nv_28NzP2U",#9
            "https://drive.google.com/uc?export=view&id=1afXWE_n8hW_jQWbzNEoWwlvTo527JfnA",#10
            "https://drive.google.com/uc?export=view&id=1af7AL8jI0oaKU7cxZ-HVcDXW9X1C7NyD",#11
            "https://drive.google.com/uc?export=view&id=1aXRZDwS-zChH-GcgN5bnuOAypGKtOnwb",#12
            "https://drive.google.com/uc?export=view&id=1afaF6F-WJu-ZDuljYyAeJLhJ-kyIpn4N",#13
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
                "kesan": "bang dimas sangat menginspirasi, dan sangat asik diajak ngobrol",  
                "pesan":"semangat terus kuliahnya bang, semoga lulus tepat waktu"#1
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "kakaknya asik dan menyenangkan, vibes nya positive sekali",  
                "pesan":"semangat terus kuliahnya kak, semoga lulus tepat waktu"# 2
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "bang sigit sangat informatif.",  
                "pesan":"semangat terus bang kuliahnya, semoga lulus tepat waktu"# 3
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "kakaknya asik dan menyenangkan",  
                "pesan":"Semangat terus kak kuliahnya, semoga lulus tepat waktu"# 4
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakak sangat menyenangkan dan asik",  
                "pesan":"Semangat terus kak kuliahnya, semoga lulus tepat waktu"# 5
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@rexanderr",
                "kesan": "bang rendi sangat informatif dan menyenangkan",  
                "pesan":"Semangat terus bang kuliahnya, semoga lulus tepat waktu"# 6
            },
            {
                "nama": "Josua Alfa Viando Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "abangnya terlihat lucu dan agak kaku, tapi sangat informatif",  
                "pesan":"Semangat terus bang kuliahnya, semoga lulus tepat waktu"# 7
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "abang nya asik dan informatif.",  
                "pesan":"Semangat terus bang kuliahnya, semoga lulus tepat waktu"# 8
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakak sangat menyenangkan",  
                "pesan":"Semangat terus kak kuliahnya, semoga lulus tepat waktu"# 9
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Lihat cogan",
                "sosmed": "@slwafhn_694",
                "kesan": "Kakak asik tapi belum sempat ngobrol banyak",  
                "pesan":"Semangat terus kak kuliahnya, semoga lulus tepat waktu"# 10
            },
            {
                "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@ranipuu",
                "kesan": "Kakak terlihat bijaksana",  
                "pesan":"Semangat terus kak kuliahnya, semoga lulus tepat waktu"# 11
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Kakak nya sangat asik",  
                "pesan":"Semangat terus kak kuliahnya, semoga lulus tepat waktu"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "abangnya asik dan jago ngomong",  
                "pesan":"Semangat terus bang kuliahnya, semoga lulus tepat waktu"# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OQHBsTyyJT2jeKEVYlyCGyAHc7_j9QyS",
            "https://drive.google.com/uc?export=view&id=1OhImEC96yIS_9e3TJWMSib9BHYjuv-Vj",
            "https://drive.google.com/uc?export=view&id=1OmgyrISnzfF000lAjRUGIfo67xenko9X",
            "https://drive.google.com/uc?export=view&id=1OlfjR0_OSHAwis5jOMa35j305lhssM6X",
            "https://drive.google.com/uc?export=view&id=1OZ9hd_Y9m374W9LltuTdP2KNUg5V5zNZ",
            "https://drive.google.com/uc?export=view&id=1Oa-jbdMq_38b5K4D1LR4gXE0ic7jiumE",
            "https://drive.google.com/uc?export=view&id=1OdnEah461DhmjCp6t2hlTE0-o_rTMh0l",
            "https://drive.google.com/uc?export=view&id=1Of4pg6v2ZJ00oQSM203K5fES4lTqX_Ee",
            "https://drive.google.com/uc?export=view&id=1Ogqq6fFI0C8HW5k877x9LSlEQZZ_ZFZw",
            "https://drive.google.com/uc?export=view&id=1OfQl70LsITgvJX9-KWL2VpuPcqdou0rq",
            "https://drive.google.com/uc?export=view&id=1ObS7Aluzwi4TJIZQyyaIHqgSDghn5bW9",
            "https://drive.google.com/uc?export=view&id=1P22HRP1EgJWdvUzoLFR2BJjIBajAGL3s",
            "https://drive.google.com/uc?export=view&id=1Os1nrSaAlI6lNq2HQsvdYikmhW2xz4Ne",
            "https://drive.google.com/uc?export=view&id=1Oxlm2u6xzsMHWzzxZaIbo6C1BF0_YLo_",
            "https://drive.google.com/uc?export=view&id=1OuBUNwlXzCya0J4p-MW4qmKLV4nHvm1h",
            "https://drive.google.com/uc?export=view&id=1OpTz9smDTiGqBxdzVlO3kl0LQ1z20hle",
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
                "kesan": "abangnya jauh banget dari Sulawesi",  
                "pesan":"semangat terus bang kuliahnya semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "kakak ini cantik sekali, dan super lembut",  
                "pesan":"Semangat kak kuliahnya"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella18",
                "kesan": "Kakaknya keren dan tinggi banget",  
                "pesan":"semangat kak kuliahnya"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@patriciadiajeng",
                "kesan": "kak cia asik dan suka bercanda",  
                "pesan":"semangat kak kuliahnya"# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "kak neli ceria banget orangnya",  
                "pesan":"semangat kakak kuliahnya"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kakaknya asik dan menyenangkan",  
                "pesan":"semangat kak kuliahnya"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "abangnya asik dan menyenangkan",  
                "pesan":"semangat bang kuliahnya"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@dwiratnn_",
                "kesan": "kakaknya asik sekali",  
                "pesan":"semangat kak kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@gymn.as",
                "kesan": "abangnya namanya keren",  
                "pesan":"semangat bang kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kakaknya asik sekali",  
                "pesan":"semangat terus kak kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kak priska sangat asik sekali",  
                "pesan":"semangat terus kak kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "-",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan": "bang arsal hobbinya mahal kayanya",  
                "pesan":"semangat terus bang kuliahnya dan lulus tepat waktu"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@abitahmad",
                "kesan": "bang abit lucu dan asik sekali",  
                "pesan":"Bang abit ayo kita by one ml"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "Kak akmal sangat sopan dan asik sekali",  
                "pesan":"semangat terus bang kulianya, semoga lulus tepat waktu"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "abangnya aktif dan asik sekalii",  
                "pesan":"semangat terus bang kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kak nisa asik sekali",  
                "pesan":"semangat terus kak kuliahnya, semoga lulus tepat waktu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HjEuUr_5SrrVXU0oBt_kJGACjf1zW-Rr",
            "https://drive.google.com/uc?export=view&id=1HfQG2ylVU82GQ3dz7YpvehSygO7kV_wv",
            "https://drive.google.com/uc?export=view&id=1HiFKISPIj3ZBp1D1JAq4UlZeoXGppPg2",
            "https://drive.google.com/uc?export=view&id=1HeL9AHhEJZAnYkhk_0QnRoNQ_VgtFhYW",
            "https://drive.google.com/uc?export=view&id=1Hd3d1vSddAVRlNJ5qbHpyJJW2jEAUeF3",
            "https://drive.google.com/uc?export=view&id=1HdQWmXWcW8zvIz5yt8AXDDWVglRnrcuO",
            "https://drive.google.com/uc?export=view&id=1HhRwcJkIPj4XR57WpihavkuBs78VIN5r",
            "https://drive.google.com/uc?export=view&id=1Hn3G-mRNNSdmLLvnFy-s4qwzwKk4zNOv",
            "https://drive.google.com/uc?export=view&id=1HjTSxdz8U8MHka63f4_pqP_6v_4_XNK2",
            "https://drive.google.com/uc?export=view&id=1Hj6XTc5hA44Mk4LrIuA6sm4KQK1D5KBw",
            "https://drive.google.com/uc?export=view&id=1HlYU4pi01wuK9PSeXBdPzHY6pfZk_ltn"
        ] 
        
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "20",
                "asal":"Sidikalang",
                "alamat": "Dekat penjara",
                "hobbi": "Nyari hobi",
                "sosmed": "@andrianlgaol",
                "kesan": "abangnya asik, informatif sekaliii",  
                "pesan":"semangat terus bang kuliahnya"
            },
            {
                "nama": "Adisty Syawalda Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@adistysa_",
                "kesan": "kakaknya informatif banget",  
                "pesan":"semangat terus kak kuliahnya"
            },        
            {
                "nama": "Nabila Azhari ",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "kakanya asik banget",  
                "pesan":"semangat terus kak kuliahnya"
            },  
            {
                "nama": "Ahmad Rizqi ",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@ahmdad.riz45",
                "kesan": "abangnya asik dan keren banget",  
                "pesan":"semangat terus bang kuliahnya"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "bang danang asik banget, dan jiwa bisnisnya terlihat tinggi",  
                "pesan":"semangat terus bang kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "bang julio keren sekali, terlihat sangat atletis",  
                "pesan":"semangat terus bang kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "kakaknya informatif banget",  
                "pesan":"semangat terus kak kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanfir",
                "kesan": "kakaknya seru dan informatif banget",  
                "pesan":"semangat terus kak kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@alfiagnnting",
                "kesan": "kakanya seru dan menyenangkan",  
                "pesan":"semangat terus kak kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "bang dhafin informatif banget",  
                "pesan":"semangat terus bang kuliahnya, semoga lulus tepat waktu"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@meylaniellia",
                "kesan": "kak elia asik banget",  
                "pesan":"semangat terus kak kuliahnya, semoga lulus tepat waktu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()
