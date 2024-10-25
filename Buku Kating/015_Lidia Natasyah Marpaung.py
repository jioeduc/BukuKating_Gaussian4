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
            "https://drive.google.com/uc?export=view&id=1GC70kIDs87a6jIrplKSO-gEpMrbmGY1P", #1
            "https://drive.google.com/uc?export=view&id=1GDNOwDdRvfRCH0QtEe-p4Pm1oULUKLQ_", #2
            "https://drive.google.com/uc?export=view&id=1GF0lFLSGoQQOFCyXz6ygxzm5yPme4ju_", #3
            "https://drive.google.com/uc?export=view&id=1G9CAjFkLQfS_TZ2appwxG2Z6zsMJR28u", #4
            "https://drive.google.com/uc?export=view&id=1GIjjv6GRwL60lJ99oi3xKGJ-sPF9EmM8", #5
            "https://drive.google.com/uc?export=view&id=1GBgJOasaBQ2duyNuAVqqxc7fccCXSEt1", #6
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
                "kesan": "Kakak ini asik saya kagum dengan dia",  
                "pesan":"Semoga sukses selalu dalam studi dan aktivitas Kakak!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar", 
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" # 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakak memiliki wawasan yang luas dan selalu memberikan masukan yang berharga.",  
                "pesan":"Semoga terus memberi inspirasi bagi orang lain, Kakak!!" #3
            },
            {
                "nama": "Hartiti Fadhilaj",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak memiliki kemampuan berkomunikasi yang sangat baik.",  
                "pesan":"Semoga terus sukses dalam berkarier dan berinteraksi dengan orang lain, Kakak!"#4
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak memiliki sikap yang sangat rendah hati",  
                "pesan":"Semoga Kakak selalu dikelilingi oleh orang-orang yang mendukung!!"#5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "Kakak memiliki sikap yang sangat profesional dalam bekerja.",  
                "pesan":"Semoga kesuksesan selalu menyertai setiap langkah Kakak!!"#6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18VnXg-Cr-n_ik2eEU5rr2HkfMwRw2iG7",#1
            "https://drive.google.com/uc?export=view&id=18_RjtrrXy5fz1_5HVOalXSCdbxQiymnn",#2
            "https://drive.google.com/uc?export=view&id=18V7KLWDgGnCUDnd4dPzFWHMYOwKxi7T2",#3
            "https://drive.google.com/uc?export=view&id=18dWuWI8GD65UEkc6lPbpDcBR3nuf3FGI",#4
            "https://drive.google.com/uc?export=view&id=18gUZ788vVWGSDf6prMPTSC5zu92NouFy",#5
            "https://drive.google.com/uc?export=view&id=18Xz7H4yGUIzMWQyHvNEIX76xqmqP2XJf",#6
            "https://drive.google.com/uc?export=view&id=18Xz7H4yGUIzMWQyHvNEIX76xqmqP2XJf",#7
            "https://drive.google.com/uc?export=view&id=18U_Ly6xJlxFHsOQfFIn01ze2iuJ55MKu",#8
            "https://drive.google.com/uc?export=view&id=18bhNoBQ0CBfGrOzWcK2hRaUbMlm-IPKS",#9
            "https://drive.google.com/uc?export=view&id=18YISLUtCwA3XP2JlxiG5WSqEu5U2_fbs",#10
        ]
        data_list = [
            {
                "nama": "Tri Murnia Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Searching di perplexity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak sangat komunikatif dan jelas dalam menjelaskan",  
                "pesan":"semangat terus kuliahnya kakk semangat ngasprakk!!!"#1
            },
            {
                "nama": "Claudea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "Jeremia Susanto",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak sangat membantu dan mudah diajak bicara.",  
                "pesan":"Semoga lancar semua urusan Kakak, sukses terus!!"# 3
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak sangat profesional dan ramah.",  
                "pesan":"Semoga Kakak sukses dalam setiap langkah ke depan!!"# 4
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak luar biasa dalam membimbing.",  
                "pesan":"Semoga kebahagiaan selalu menyertai Kakak!!"# 5
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak memiliki kepribadian yang ramah dan menyenangkan.",  
                "pesan":"semangat terus kuliahnya kak !!!"# 6
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak sangat sabar dalam mengajarkan hal baru kepada kami.",  
                "pesan":"Semoga Kakak selalu diberi kemudahan dalam setiap usaha!!"# 7
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak selalu berusaha menciptakan suasana yang menyenangkan.",  
                "pesan":"Semoga semua usaha Kakak membuahkan hasil yang memuaskan!!"# 8
            },
            {
                "nama": "Berliana Inda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak sangat bersahabat dan menyenangkan!",  
                "pesan":"Semoga Kakak selalu dikelilingi orang-orang baik!!"# 9
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!!"# 10
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
                "nama": "Anissa Luthfi",
                "nim": "121450093",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahyu",
                "hobbi": "Bernyanyi",
                "sosmed": "@anissaluthfia_",
                "kesan": "Abangnya inspiratif",  
                "pesan":"Jangan lupa berdoa dan semangat selalu"
            },
            {
                "nama": "Ryan Bintang Wijaya ",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "Percaya gak percaya, Bang Bintang super supportif orangnya",  
                "pesan":"Tetep jadi orang baik bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


# Tambahkan menu lainnya sesuai kebutuhan
