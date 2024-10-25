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
            "https://drive.google.com/uc?export=view&id=1-MWuLazmjcebcamq5p8T8_TswG534vaZ",
            "https://drive.google.com/uc?export=view&id=1-IBt9fNiE1n6_dLVnt26oZUgHpZuHenk",
            "https://drive.google.com/uc?export=view&id=1-Fx3EKHrjYJTdAdF3Nd9doTnUl8uhXqC",
            "https://drive.google.com/uc?export=view&id=1-U7TG5sF6yLn6qKicGjBQyasOG68QhGw",
            "https://drive.google.com/uc?export=view&id=1-BjJvnjt_OkfM9A2I1XXt5L_ZiznslXg",
            "https://drive.google.com/uc?export=view&id=1-SQXdKUxqSEQN0gxa_uRzwu0naKzzj-y",
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
                "kesan": "Abangnya keren dan asik.",  
                "pesan":"Semangat terus Bang dan semoga apa yang dicita-citakan tercapai."# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abangnya seru dan gokil.",  
                "pesan":"Semangat terus Bang kuliahnya dan terwujud buat semua impiannya."# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakaknya seru dan asik.",  
                "pesan":"Terus semangat kuliahnya kak dan semoga sukses selalu dan bisa terus menonton drakor favoritnya."# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya keren dan seru.",  
                "pesan":"Semangat terus Kak dan sukses dalam segala hal."# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakaknya kece dan seru.",  
                "pesan":"Terus semangat dan sukses dalam perjalanan kuliahnya Kak."# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "Kakaknya punya hobi menarik dan asik.",  
                "pesan":"semangat kuliahnya Kak dan Semoga sukses selalu."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()




elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14O4qO1l9TYSDk6xs-ZFbiTh0blNp_co-",
            "https://drive.google.com/uc?export=view&id=14IZAAHaGCkSdybsk_SSq7jpH9yFvV1Bu",
            "https://drive.google.com/uc?export=view&id=13p1uMYMMCQUERVd7NYvPYjOqS8_mO60i",
            "https://drive.google.com/uc?export=view&id=13qRSF7z4DtkjD23H0eA8gE3kqT95pLDQ",
            "https://drive.google.com/uc?export=view&id=13r9FKQG_K3xfj9ItVML_g3ib9qpf9-I3",
            "https://drive.google.com/uc?export=view&id=14T9y86d_B5DqghQvLpQW1ysB8gyjZMUL",
            "https://drive.google.com/uc?export=view&id=14K_EGfL_ILNh5Rt4RGMRqFHOmPoTwTmG",
            "https://drive.google.com/uc?export=view&id=13k9URuNPCXTzFOVFI8IHBnNQlHLFuRQg",
            "https://drive.google.com/uc?export=view&id=144xD1Kbck9T_CIe2QdSP4NYP-aD6Dwvz",
            "https://drive.google.com/uc?export=view&id=14LwQhnNTEj9yu-GvbVPxoBf-NiB0qffE",
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
                "kesan": "Kakaknya menyenangkan dan asik.",  
                "pesan":"Semangat terus kuliahnya Kak dan semoga bisa lulus tepat waktu dan sukses dalam kariernya nanti."
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakaknya baik dan menyenangkan.",  
                "pesan":"Semangat terus kuliahnya kak dan semoga sukses dan bisa mencapai apa yang diimpikan."
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya seru dan asik.",  
                "pesan":"Terus semangat kuliahnya Kak dan semoga berhasil dan sukses meraih cita-cita."
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini asik dan seru diajak ngobrol.",  
                "pesan":"semangat terus Bang kuliahnya dan sukses mencapai apa yang diinginkan."# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya menyenangkan dan asik.",  
                "pesan":"Semangat terus kuliahnya Bang dan semoga sukses dalam segala hal yang diusahakan."
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya seru dan asik",  
                "pesan":"Semangat terus kuliahnya Bang dan semoga sukses mengejar impian."
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya seru diajak ngobrol",  
                "pesan":"Semangat Bang kuliahnya dan sukses mengejar impian."
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakaknya asik dan menyenangkan",  
                "pesan":"Semangat terus kuliahnya Kak dan sukses mengejar cita-citanya."
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
                "pesan":"Semangat terus Kak kuliahnya dan sukses mengejar impiannya."
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakaknya asik dan seru.",  
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai."
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















