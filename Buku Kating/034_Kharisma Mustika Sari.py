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
            "https://drive.google.com/uc?export=view&id=1HP2zgYyOYy_bDx_CRpUYc_VQIvXTEyPK",
            "https://drive.google.com/uc?export=view&id=1HP1qwYIwt_SVVbfTSEb_Y64ty-fNli8Z",
            "https://drive.google.com/uc?export=view&id=1HNLtkRtuhcg5bK8TfReyPPQhtHQ1XJ9Q",
            "https://drive.google.com/uc?export=view&id=1HPrBxrJMusAZbdgDYPS0PxvdHnWTI67O",
            "https://drive.google.com/uc?export=view&id=1HRYMi4CmPfDoVKk8wnDSUutSQAvXQfPo",
            "https://drive.google.com/uc?export=view&id=1HSB0GgoJ_x5u-hRjIPCivf1sTRNiDS6d",
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
                "kesan": "enak diajak ngobrol dan enjoy",  
                "pesan":"semangat buat bang gumilang semoga makin sukses"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "suka becanda dan tidak bikin tegang saat ngobrol",  
                "pesan":"semangat bang pandra buat menyusun TA dan semoga lulus tepat waktu"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "asik kalo ngobrol",  
                "pesan":"semangat kak melin buat menyusun TA dan semoga lulus tepat waktu"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kakaknya sangat kalem dan lemah lembut",  
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
                "kesan": "asik tapi agak pendiem",  
                "pesan":"semangat terus kuliahnya kakak, semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@azilem",
                "kesan": "kakaknya asik",  
                "pesan":"semangat selalu kak kuliahnya, semoga bisa lulus tepat waktu!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EZRJkJfOc6sa0SvIIBY974NRRkfr4afS",
            "https://drive.google.com/uc?export=view&id=1EihJGH3oJrUbLiV9qH_GM5D4JdaFm8C-",
            "https://drive.google.com/uc?export=view&id=1EWKl1XBnvLZxRW8MkZSphkOOc1mDdoIb",
            "https://drive.google.com/uc?export=view&id=1Enn-adP0I17R_5qxvAsLC8nN2nNN9ihI",
            "https://drive.google.com/uc?export=view&id=1El7D7OyHX8Qye8LQxAxscssMbUxRzGkn",
            "https://drive.google.com/uc?export=view&id=1EaxQZdnJFLLfYFgTODoC63vxNunfTRae",
            "https://drive.google.com/uc?export=view&id=1EfVVqCgN5DrHcNBNY63c36p49i9fqMtS",
            "https://drive.google.com/uc?export=view&id=1EusqpbNa651aDJch78c9I534i6pYFTMy",
            "https://drive.google.com/uc?export=view&id=1EjhzbH-nJZ-V7XReVumNrsrnOWDNMwQd",
            "https://drive.google.com/uc?export=view&id=1EcLg-UbcJHMkcglj1Yq8HO4PUpUa0yH-",
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
                "kesan": "Kakak tri asik banget, enjoy dan baik",  
                "pesan":"semangat terus kuliahnya kakak, semoga dapat lulus tepat waktu"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121400124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini baik",  
                "pesan":"semangat terus kuliahnya kak, semoga dapat lulus tepat waktu"
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
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jeremia asik dan seru",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya asik",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Bang mirzan enak dan baik",  
                "pesan":"semangat terus bang kuliahnya bang"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya baik dan asik diajak ngobrol",  
                "pesan":"semangat bang kuliahnya, semoga dapat lulus tepat waktu"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kak annisa asik",  
                "pesan":"semangat terus kuliahnya kakak, semoga dapat lulus tepat waktu"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kak berlin baik dan asik pembawaannya",  
                "pesan":"semangat terus kuliahnya kak, semoga dapat lulus tepat waktu"
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
                "pesan":"semangat terus kuliahnya kakak, semoga dapat lulus tepat waktu"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ESNIc0NWpYLN4t24j768VcKltIK8niak",
            "https://drive.google.com/uc?export=view&id=1ERuRUKE9VHG06FeEBNJFQS1KcFJ0JbCw",
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
                "kesan": "Kak luthfi baik dan humble",  
                "pesan":"semangat kuliah kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "baik dan profesional",  
                "pesan":"Semangat bang dengan berbagai kesibukan bang bintang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FQG4m7sajO4dL0k2DHXyH28mHi71dPJR",
            "https://drive.google.com/uc?export=view&id=1FhnodflashyHkiHqYTEtRd0WOGVdehyV",
            "https://drive.google.com/uc?export=view&id=1Fl3KO9NYVHaRgLk6298SwSO3OIp-O7U6",
            "https://drive.google.com/uc?export=view&id=1FLrEcqNxcVe6G0HPqey_8FL6L1gukXw_",
            "https://drive.google.com/uc?export=view&id=1FbSRqPVlxqSWi0xsSvooqgp1xx16L1K1",
            "https://drive.google.com/uc?export=view&id=1FI-y_APDuX2I7D6KfmRCkfOhM6hFU3M_",
            "https://drive.google.com/uc?export=view&id=1FcVRYhdKDcqNv7g-acgeqOKzCKf9Xbw8",
            "https://drive.google.com/uc?export=view&id=1FJtLAa3eqgaxQPn2GskLUozbQX38UPF_",
            "https://drive.google.com/uc?export=view&id=1FWffpXpUq4--YWRquTf7oSp_srDkFBn6",
            "https://drive.google.com/uc?export=view&id=1FSY2DobnF9QmIFNtugrmZfizF9VjfMPl",
            "https://drive.google.com/uc?export=view&id=1FTKiaTylPNRx6y1ulvR5KGZOOhRghBdd",
            "https://drive.google.com/uc?export=view&id=1FS7XQvwIY4HlW-r_qqO2lRLU2Wr8LVwO",
            "https://drive.google.com/uc?export=view&id=1FU_saayT12LkMvU_ZDNMgKdlHpbUoCRf",
            "https://drive.google.com/uc?export=view&id=1Fk4F-my8FqYNnEnFKqxryly8_X7S8t-N",
            "https://drive.google.com/uc?export=view&id=1FO9KfsQJHDR9lG6Ys2B-EiTK3snH9FiV",
            "https://drive.google.com/uc?export=view&id=1FXUCCb9FmoCl6H1ldH8BYFLHJweclEno",
            "https://drive.google.com/uc?export=view&id=1FWfJWx6ECtcmVpN6QWYxgQ-x0LMJ56-i",
            "https://drive.google.com/uc?export=view&id=1Ft91fnfLFkM0UvnhMeRZyI9xFpNIwX-i",
            "https://drive.google.com/uc?export=view&id=1FVsVYNOka5smzwryLx_xjUWy1uWuodQL",
            "https://drive.google.com/uc?export=view&id=1FWn2LTci1NPafmNnd0WwqFgRi1Cj7E7C",
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
                "kesan": "bang ericson baikk",  
                "pesan":"Semangat terus kuliahnya bang dan semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya seru dan asik.",  
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
                "kesan": "kakak ini asik dan seru diajak ngobrol.",  
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
                "kesan": "kakanya menyenangkan dan asik.",  
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
                "kesan": "kakanyanya seru dan asik",  
                "pesan":"Semangat terus kuliahnya kak dan semoga sukses mengejar impian."
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
                "pesan":"Semangat terus kuliahnya Kak dan sukses mengejar cita-citanya."
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
                "kesan": "Kakaknya asik dan seru.",   
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
                "kesan": "Kakaknya asik dan seru.",   
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai." 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "Kakaknya asik dan seru.",   
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
                "kesan": "Kakaknya asik dan seru.",   
                "pesan":"Semangat terus bang kuliahnya dan semoga semua cita-citanya tercapai." 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Kakaknya asik dan seru.",   
                "pesan":"Semangat terus bang kuliahnya dan semoga semua cita-citanya tercapai." 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kakaknya asik dan seru.",   
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai." 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya asik dan seru.",  
                "pesan":"Semangat terus bang kuliahnya dan semoga semua cita-citanya tercapai."
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
                "pesan":"Semangat terus bang kuliahnya dan semoga semua cita-citanya tercapai."
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "abangnya asik dan seru.",  
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai."
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "abangnya asik dan seru.",  
                "pesan":"Semangat terus bang kuliahnya dan semoga semua cita-citanya tercapai."
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "abangnya asik dan seru.",  
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HUe5T5iKLiNqOnx4rvbC87LZnddSMUxS",
            "https://drive.google.com/uc?export=view&id=1I52hhS3LUUsM9th-5yW-s-GtiNkKrv9x",
            "https://drive.google.com/uc?export=view&id=1H_gMdp06_DNt_ZfY1-ATUXNeXqEb4l26",
            "https://drive.google.com/uc?export=view&id=1Hc-z5LICmNcbF6mn2AuFmRR64CkzY1UB",
            "https://drive.google.com/uc?export=view&id=1HvBTupkbZebVk7qtySYWmdxVh18GgQ1_",
            "https://drive.google.com/uc?export=view&id=1I6DFXPM5Du8LpTjZgH4IoAi-6NGiexZx",
            "https://drive.google.com/uc?export=view&id=1HUF1sZg4YMri5CEG7dVB-BYnGx4jnstf",
            "https://drive.google.com/uc?export=view&id=1HgCAOIf87h5hcCn_m5O6-z6in4DiJ9Ih",
            "https://drive.google.com/uc?export=view&id=1HwsuE3BFiUYAA_cEj-4r0wJ2LTIxZaO_",
            "https://drive.google.com/uc?export=view&id=1i_7Anhgr_qPAe5ONlKx_e7Mut6PPP1rr",
            "https://drive.google.com/uc?export=view&id=1I1OLzSIk5-SEVrhlFc5Xfe5KR5CIMj7T",
            "https://drive.google.com/uc?export=view&id=1Hh-wAcAaBqzPC_EGuVtuSpWYD-Sri2sU",
            "https://drive.google.com/uc?export=view&id=1I7reVeS6FqB1waiygSlBIt2182kPCuSe",
            "https://drive.google.com/uc?export=view&id=1Hd05bgYDu1YZCnnGIX_QBTT5A7XKOV6M",
            "https://drive.google.com/uc?export=view&id=1HmFXIxr0SS_fT6YV1EBH6NGYfxr-KT4K",
            "https://drive.google.com/uc?export=view&id=1IAAGvxnEa8wq2fr0sjzKH_T47INA_LPl",
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
                "kesan": "baik",  
                "pesan":"Semangat terus kak"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang"
            },

            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "baik",  
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
                "kesan": "asik",  
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
                "kesan": "Abangnya keren banget",  
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
                "kesan": "Suka banget sama kakaknya",  
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
                "kesan": "Kakaknya ramah benget",  
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
                "kesan": "Kak Marleta positive vibe banget, dan baikk banget",  
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
                "kesan": "Suka sama Kak Rut",  
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
                "kesan": "Senangnya bertemu kakak",  
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
                "kesan": "Abangnya pendiem",  
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
            "https://drive.google.com/uc?export=view&id=1nBGqqyljZ4yPtxs4_WyzD4m9aGU24FBd",
            "https://drive.google.com/uc?export=view&id=1GDMvPYGG6Yi1Pg_G9gUJ7EgN0pkkcDxH",  
            "https://drive.google.com/uc?export=view&id=1GHj-RELGy5R_EYqa75YRQt0pHVYEBLPF",
            "https://drive.google.com/uc?export=view&id=1G54ECHJuHANRWLL5gCZXcPw6Uh2AFfEJ",
            "https://drive.google.com/uc?export=view&id=1G7Ry4iFHoBsrfGAfeR78wlZEOLkh5CKL",
            "https://drive.google.com/uc?export=view&id=1G87omxqcNW7Bc15QDtgSAOhdYYX1Orjr",
            "https://drive.google.com/uc?export=view&id=1G-Eb68QXZ2FGAhsANmoeWG1osg3MqWKs",
            "https://drive.google.com/uc?export=view&id=1GRAYg_JXWrI6YcYN518_SaUqPwNNO3-1",
            "https://drive.google.com/uc?export=view&id=1GJY7XEgHEJEk7edNbl_fAE01jn9fbQkH",
            "https://drive.google.com/uc?export=view&id=1Fxaa5EfXy-e3GC3lixU6b-f767wUsZJS",
            "https://drive.google.com/uc?export=view&id=1GJ6AB0eTYhovM6UEhnX4gAKS9OOtNKBY",
            "https://drive.google.com/uc?export=view&id=1Fw8rDGYAMTd40i71-KOS1aALW3A5Qqeh",
            "https://drive.google.com/uc?export=view&id=1Fwk8pSXSBJyHLRKkyEPduWQfsWrQ3dZV",
            "https://drive.google.com/uc?export=view&id=1G0OM2HN34Fbfv2hE9Ol44yNN5eYtxyRr",
            "https://drive.google.com/uc?export=view&id=1GA0MRjbPu8s2_IwZX4elpZwIiKLkhUHw",
            "https://drive.google.com/uc?export=view&id=1GCYA61tqfVs3TBJ2E4pCfy78KCjz2XYL",
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
                "kesan": "Abangnya baik",  
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
                "kesan": "Kakaknya seperti pendiam",  
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
                "kesan": "abang nya baik",  
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
            "https://drive.google.com/uc?export=view&id=1HCaGwksZmisHJ4dh4JMWP6qyGkiRKuWP",
            "https://drive.google.com/uc?export=view&id=1H1X7QnumurgUbOb46Q9hpONuaSOk0-6D",
            "https://drive.google.com/uc?export=view&id=1HCNHsOt97fQVORS1QX8kkEEVRbGmc37h",
            "https://drive.google.com/uc?export=view&id=1H4dVhpZOPkRxbJz_AQ0V8n6CIiEmljyp",
            "https://drive.google.com/uc?export=view&id=1H5C3loOKdx3_hVyA_MshUULtJUqtpttS",
            "https://drive.google.com/uc?export=view&id=1HGwdEXDj1iX6sMVEyTwVenSvQ_oypc6O",
            "https://drive.google.com/uc?export=view&id=1H7hATwne01I1dGb0ILBLS8fzWdaOMedN",
            "https://drive.google.com/uc?export=view&id=1HFuSJkaTDzCmo-_ycZFhhaP14MTpraiO",
            "https://drive.google.com/uc?export=view&id=1HHMjfRO2NyL3oSrq-0QkF7d5CyH5NZEY",
            "https://drive.google.com/uc?export=view&id=1HDZNzJa9ip_0g8B995NSA7-rKcY1-PXZ",
            "https://drive.google.com/uc?export=view&id=1HBqKfAazBxvgxasOY1Gnk7wCM6cMtItC",
            "https://drive.google.com/uc?export=view&id=1HF8o6CFnp1MP-65yEiS28SzoGaqNbDkn",
            "https://drive.google.com/uc?export=view&id=1H8ATNvYDAhKuNU4gAmeYRVUsIv7UUxJ0",
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
                "pesan":"semangat terus kuliahnya bang, semoga lulus tepat waktu!!!"
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
                "pesan":"semangat terus kuliahnya kak, semoga semua urusannya diperlancar!!"
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
                "pesan":"Semoga lancar semua urusan Kakak, sukses terus!!"
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
                "pesan":"Semoga Kakak sukses dalam setiap langkah ke depan!!"
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
                "pesan":"Semoga kebahagiaan selalu menyertai Kakak!!"
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
                "pesan":"semangat terus kuliahnya kak !!!"
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
                "pesan":"Semoga Kakak selalu diberi kemudahan dalam setiap usaha!!"
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
                "pesan":"Semoga semua usaha Kakak membuahkan hasil yang memuaskan!!"
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
                "pesan":"Semoga Kakak selalu dikelilingi orang-orang baik!!"
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
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!!"
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
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!!"
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
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!!"
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
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1F4-S5anIL9xixuuZZ2SEHVV75M-ndyp8",
            "https://drive.google.com/uc?export=view&id=1F318Rn1oyX8KQUtC7sqq5K5Lq1SP5wX7",
            "https://drive.google.com/uc?export=view&id=1d0OVVLBVon2TcjbgODYxoTMdgj-x_y8M",
            "https://drive.google.com/uc?export=view&id=1FAEC6y43C-1zm1XSBcAl81SN2vo96arn",
            "https://drive.google.com/uc?export=view&id=1F7McohV9pixREUlcCbEVSKZ9eeua61rl",
            "https://drive.google.com/uc?export=view&id=1F6XAKTl2S8TZlWQEdWZfAYFcknOQMsxE",
            "https://drive.google.com/uc?export=view&id=1FCRAfbdHpHUmmaqJnKoxDJyPigCoPWi-",
            "https://drive.google.com/uc?export=view&id=1F4a3uY1xUmqdseRADiks-Bp8RpvPiFqB",
            "https://drive.google.com/uc?export=view&id=1F475KUMnzCfYj-I_U844C7W3T2NSFaBC",
            "https://drive.google.com/uc?export=view&id=1FA8nZ5jx85g7heLRyjeqmeunsJM21aWd",
            "https://drive.google.com/uc?export=view&id=1F5cy7iMkalS0FiDDuINy_ogFKP19NPdX",
            "https://drive.google.com/uc?export=view&id=1F987fu_jX7z45Cr3lLaO5u_7ka_JExmW",
            "https://drive.google.com/uc?export=view&id=1EyQLGFzy79ZkG_-MiAPlo4pZNFKRLe7S",
            "https://drive.google.com/uc?export=view&id=1EwyWP6ZSQn_8y1kt24BLT5Xhe6LlDVFr",
            "https://drive.google.com/uc?export=view&id=1F01JLoctA04etteBHo8HkK-EJ2CoHRP9",
            "https://drive.google.com/uc?export=view&id=1FCW0OGGf7YQRrrRP9Uh_N9yiBX4reDhL",
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
                "kesan": "kakak ini asik sekali",  
                "pesan":"semoga bahagia bang"
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
                "kesan": "kakaknya asik dan baik",  
                "pesan":"semangat kak ngejar cita - cita nya"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "kakaknya baik",  
                "pesan":"semangat kak untuk ngejalanin hidup"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "kakak ini sangat kalem",  
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
                "kesan": "Bang fahrul agak pendiem cuma keliatannya asik",  
                "pesan":"semangat bang untuk ngejalanin kehidupan"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kakak asik dan lucu",  
                "pesan":"semangat jangan menyerah dan terus berjuang!"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@aimnn.as",
                "kesan": "abangnya baik",  
                "pesan":"semangat bang ngejar cita - cita nya"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "baik dan kalem",  
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
                "kesan": "kakanya baik",  
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
                "kesan": "abangnya baik",  
                "pesan":"semangat terus bang belajarnya!"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "baik",  
                "pesan":"semangat terus bang belajarnya!"
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@akmal.faiz",
                "kesan": "ramah",  
                "pesan":"semangat terus bang belajarnya!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "baik",  
                "pesan":"semangat terus bang"
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

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GXkEINP4JHIaJ30I_sZseJk3Sj90-xHB",
            "https://drive.google.com/uc?export=view&id=1GckJNA2cj0BsCp2QBHS7YqJIWAW7kArS",
            "https://drive.google.com/uc?export=view&id=1GaZYOMfzUcsODjvFIVca1nNbcN2teIIh",
            "https://drive.google.com/uc?export=view&id=1GlUT5cH48vjY4XRupS-FoxLG1M0uapQf",
            "https://drive.google.com/uc?export=view&id=1Gg5ZY8Tkpm44jNeFYIQvrikzTPeDsyKN",
            "https://drive.google.com/uc?export=view&id=1GfsNEDqyPorrRYmMPUlXiewBTuK2wPLs",
            "https://drive.google.com/uc?export=view&id=1GeALRn3z726-aOdmBXuYodnnvU4oa8q8",
            "https://drive.google.com/uc?export=view&id=1GfvCY-8k6RxeUg04tpCIyyHbPkp7ErbT",
            "https://drive.google.com/uc?export=view&id=1GWVHNqs1ZoQ4DNV8-gEZMCgAsV3cpoYw",
            "https://drive.google.com/uc?export=view&id=1GXl6eY59ETGIwG_hYwtubN0SA0SjHtZL",
            "https://drive.google.com/uc?export=view&id=1Gmlzg2HsNAYKJxgz52PNimjQU_KO5KVG",
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
                "pesan":"Bahagia terus ya kakk, semangat selalu"
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
                "pesan":"Semangat kuliahnya ya kak, semoga cepet dapet gelar"
            },  
            {
                "nama": "Ahmad Rizqi ",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@Ahmad.riz45",
                "kesan": "abang ini ramah, keren banget abang",  
                "pesan":"semoga bahagia terus ya bang, semangat bang"
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
                "pesan":"semangat menjalani kehidupan bang, sehat-sehat"
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
                "kesan":"kakaknyaa motivator bangett,mantap kak ",  
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
                "kesan": "kakaknyaa lucu banget, seru banget kak",  
                "pesan":"semangat menjalani kehidupan kuliahnya kak, sukses selalu yaa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()
