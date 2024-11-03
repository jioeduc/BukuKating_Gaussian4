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
            "https://drive.google.com/uc?export=view&id=1RNcxnfQxWVDSTdxSyIKPK1d2xS0ILt07",
            "https://drive.google.com/uc?export=view&id=1RJwVnzVLYxgZhw4L5cxro3RsnDMGqibs",
            "https://drive.google.com/uc?export=view&id=1RCEg40tcMQJtk4Z3cywkaatBXS53kHDN",
            "https://drive.google.com/uc?export=view&id=1RNtcY-grH0gsKdn5KRB5LZ5AG7b6oCdG",
            "https://drive.google.com/uc?export=view&id=1Z9zOpRHxJ9WPkmVA4hUMKIlM8IS7VwnT",
            "https://drive.google.com/uc?export=view&id=1MIZ8B_OlZHhnpovMtUMECLcyCGJYiMQd",
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
                "kesan": "Abangnya asik dan seru",  
                "pesan":"semangat buat abang semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abang ini baik dan suka membantu",  
                "pesan":"Semangat TA nya semoga bisa lulus tepat waktu"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakak ini lucu dan soft girl",  
                "pesan":"Semangat kuliahnya dan ditunggu wisudanya kak"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini baik dan keliatann malu-malu, kalem",  
                "pesan":"semangat kak dan bahagia terus yaa"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini asik diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kakak, semoga bisa lulus tepat waktu!"
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
                "pesan":"semangat selalu kak kuliahnya dan ditunggu lulusnya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19a5O-e5hWKNqlWy5wGC825qQ_VoV-ent",
            "https://drive.google.com/uc?export=view&id=1psHVbV49vti97FDyUjtkqCPcZ9SduWo8",
            "https://drive.google.com/uc?export=view&id=1yknEZLwWGy6WTfxlEwbjCJaAt__rdBCy",
            "https://drive.google.com/uc?export=view&id=19N3_m-ro4FeFi6qFw3FsccAgvhpKjHgp",
            "https://drive.google.com/uc?export=view&id=1EWIVkoPtDxnzDZApzhLHkZAWG8UzQHum",
            "https://drive.google.com/uc?export=view&id=1PGkmSM77Nl_JDo-xrKATgCRcmAiakU5t",
            "https://drive.google.com/uc?export=view&id=1gL3JR1rX2Nu9Uq6_yxM1l8d4n5e-1-Uc",
            "https://drive.google.com/uc?export=view&id=1a5ImtsHbYFD13jJwve5d9pBpM2vagPkn",
            "https://drive.google.com/uc?export=view&id=1xFoFv3a9JT6ysXJ35JL_fNyNL9f3C0yI", 
            "https://drive.google.com/uc?export=view&id=1TNgVvFP16kJvn0N1Vdx5ncbOU4QlD-xF", 
            
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
                "kesan": "Kakak ini asik dan lucu",  
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
                "kesan": "Kakak ini baik sekali dan asik",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakaknya informatif sekali",  
                "pesan":"semoga bahagia selalu dengan pilihannya kak"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini asik dan seru diajak ngobrol",  
                "pesan":"semangat terus bang kuliahnya"# 1
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
                "pesan":"bahagiaa terus bang"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini enak diajak ngobrol dan keren",  
                "pesan":"semangat terus bang kuliahnya"
            },
             {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya asik",  
                "pesan":"semoga bahagia dengan jalan yang dipilih bang"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak lucu banget plis",  
                "pesan":"sehat terus kak dan bahagia ya kak"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobbi": "Ngerjain tugas di dwar.io, suka ngeliat pekerjaan di linked in, puasa senin kamis",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ramah banget sih :D",  
                "pesan":"Kakak aesthetic bgt vibesnya?"
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobbi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini asik sekali dan ramah",  
                "pesan":"semangat terus kuliahnya kakak!"
            },
            ]    
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fiNGMbTIRnnixGOwoeTnTYGJcPgWcagE",
            "https://drive.google.com/uc?export=view&id=1fjus6m-fxR9OX-Y08sRzmPqSJdPuD494",
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
                "kesan": "kakak keren banget dan menginspirasi",  
                "pesan":"semangat selalu"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "bang Bintang berkharisma sekali",  
                "pesan":"Tetep jadi orang baik bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dDewo9_wdGad0w7PNdmfFcki79KZ979n",
            "https://drive.google.com/uc?export=view&id=1cPmYQ3tCiX7mRWndQUubd8iyRBZG1MmV",
            "https://drive.google.com/uc?export=view&id=1d8tlQxLgHfOR-sH2RivBl7pLSDCe8BW7",
            "https://drive.google.com/uc?export=view&id=1dF2Be1T6_YV3ZGwLPOVLrimyi3tGYGaA",
            "https://drive.google.com/uc?export=view&id=1crROPOT2FcA-Jk4EdrefaVNestBRtAZe",
            "https://drive.google.com/uc?export=view&id=1d8i-VL9qwzg7VNrlf9SX0sFOX8FO36Y2",
            "https://drive.google.com/uc?export=view&id=1ftfSzQZu5jZHg2XJF0WsdH9wXjM6Y2rn",
            "https://drive.google.com/uc?export=view&id=1cyqHRlVzyNaQ5MmdtSQezVUdVEokyx7X",
            "https://drive.google.com/uc?export=view&id=1cbMeSg-7cEWuxA_GzlNUailqYnuolKem",
            "https://drive.google.com/uc?export=view&id=1cZl2AWlMC3TmdFiW12e0wZi5RabU8q74",
            "https://drive.google.com/uc?export=view&id=1cWVCf5QDMPh5K_PfjTFl7IVHbVCD_LIt",
            "https://drive.google.com/uc?export=view&id=1cZVC7NHsBRR6kuL32SnS-Ul6b-rmU043",
            "https://drive.google.com/uc?export=view&id=1cHjtXxxJ0J8NrAuQhosd_Qc7hAn4e8rZ",
            "https://drive.google.com/uc?export=view&id=1cWWU2F2SwziGABIp-lvbriOTYEYcORiN",
            "https://drive.google.com/uc?export=view&id=1cZ4ZAvKOuTHephw9BSgsB0JT9ASBiDrR",
            "https://drive.google.com/uc?export=view&id=1dKuUJbx2G4k9eZO6YWG5vYpcjSxJanSd",
            "https://drive.google.com/uc?export=view&id=1dOnhA5jnfwxABfH-uwNsP5I1kydgOdXI",
            "https://drive.google.com/uc?export=view&id=1da4TsrtZy18HO9E_ipRtVEHrTA7SeFB4",
            "https://drive.google.com/uc?export=view&id=1dGEr5XRX_r7hb1Lyjae2yrQjqwHDriTu",
            "https://drive.google.com/uc?export=view&id=1dXgxbYxYyLU4aLEmvGgFqQ_Xo5YbnvGB",
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
                "kesan": "Kakaknya asik.",  
                "pesan":"semoga bisa lulus tepat waktu dan sukses dalam kariernya nanti."
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya keliatan jutek tapi ternyata lucu",  
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
                "kesan": "cantik banget",  
                "pesan":"Terus semangat kuliahnya Kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami",
                "kesan": "kakak ini keliatan jutek, asik dan seru diajak ngobrol.",  
                "pesan":"sukses mencapai apa yang diinginkan."
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakak asik diajak ngobrol dan keren",  
                "pesan": "semoga sukses dalam segala hal yang diusahakan."
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
                "pesan":"semoga sukses mengejar impian."
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
                "kesan": "abangnya asik",  
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
                "kesan": "Kakaknya receh dan lucu",  
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
                "pesan":"Semangat terus Kak kuliahnya" 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamy", 
                "kesan": "Kakaknya friendly",   
                "pesan":"Semangat terus Kak kuliahnya dan ditunggu wisudanya" 
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
                "pesan":"sukses selalu bang." 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "Kakaknya pinter banget",   
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai." 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Kakaknya soft spoken dan perhatian",   
                "pesan":"terus jadi orang baik ya bang." 
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
                "pesan":"bahagia terus ya kak." 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya ramah",  
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai."
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
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai."
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "kakak asik dan baik banget ",  
                "pesan":"semangat menghadapi anak gauss ini kak"
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
                "pesan":"semoga semua cita-citanya tercapai."
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "kakaknya seru.",  
                "pesan":"Semangat terus Kak kuliahnya dan semoga semua cita-citanya tercapai."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_zhOQ8HRcJMiccmgfA8u4bgsPFzpB3A5",
            "https://drive.google.com/uc?export=view&id=1_ahmPfb5V4Toi2YETeeiAYbQ7fjzVWSH",
            "https://drive.google.com/uc?export=view&id=1_UnYjB62XcWD4A1StS57n2LUxPyx7TUd",
            "https://drive.google.com/uc?export=view&id=1_XKHLnDtzmZ1SoRXezOnmCbMFr1Ih5Rh",
            "https://drive.google.com/uc?export=view&id=1_Q6WIxmXw4e2vuGPrq0QRrsls1zVeyZ_",
            "https://drive.google.com/uc?export=view&id=1_q1uiIxW1qxX2OC7o4FvgLDmzIrECCEj",
            "https://drive.google.com/uc?export=view&id=1_HD8E9DbC85037Ls2pBmjR9-7QW5NW5t",
            "https://drive.google.com/uc?export=view&id=1a5V5p0lRxBrNF3aquqaaM3oSjAHRNu6z",
            "https://drive.google.com/uc?export=view&id=1ZroH0i4wPY5hKO-Vvd28Anog7NYYvLjt",
            "https://drive.google.com/uc?export=view&id=1ZwW7nXm2RNiGKf9Nlt03b5wzhHKquc8C",
            "https://drive.google.com/uc?export=view&id=1_hYq8tCG3gjsZHrdUeu4dmBXRxszHTdg",
            "https://drive.google.com/uc?export=view&id=1_gQ3DtFqgH7UiVZ96lC0NKPEMgmGAp2s",
            "https://drive.google.com/uc?export=view&id=1_G2B_0h-210KupX_RWll_aHxgebQxBF7",
            "https://drive.google.com/uc?export=view&id=1_kgvrbWtRKj3FW9vqrSR01pqsf2k5yvv",
            "https://drive.google.com/uc?export=view&id=1a6SnfQcfaBkrNpjnWDuLAHvK2ki6YWeV",
            "https://drive.google.com/uc?export=view&id=1_-uZzqKteTWjHgfDZ-0FNdi15nU4bgyc",
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
                "kesan": "Keliatan tegas dan mandiri",  
                "pesan":"Semangat terus bang"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "bang sahid receh banget dan suka ketawa",  
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
                "kesan": "Abangnya keliatan pendiem",  
                "pesan":"Semangat terus bang kuliahnya"
            },

            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "abangnya keren banget",  
                "pesan":"Semangat terus kuliahnya"
            },

            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Baca novel",
                "sosmed": "@dkselsd_31",
                "kesan": "ternyata kakaknya punya kembaran",  
                "pesan":"ditunggu wisudanya kak"
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
                "kesan": "kakak kerenn banget",  
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
                "kesan": "Kakaknya ramahh sekali",  
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
                "kesan": "suka banget sama aura baiknya kakak",  
                "pesan":"Semangat terus kak dan ditunggu wisudanya"
            },

            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "kak rut baik banget dan suka menolong",  
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
                "kesan": "kakak baik bangett dan lembut banget sumpahh",  
                "pesan":"Semangat terus kak, aku tunggu wisudannya yaz"
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
                "kesan": "abangnya ramah dan keren abis",  
                "pesan":"Semangat bang semester 5"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Hobinya relate untuk kehidupan mahasiswa",  
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
                "kesan": "Abangnya pendiam sekali",  
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
                "kesan": "Bang Randa keren selalu sigap",  
                "pesan":"Semangat membantu keriwehan anak gauss bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bMWOFcEX12n0gK3QBnvYfnb0GaXIAm4g",
            "https://drive.google.com/uc?export=view&id=1bN6FYl833xd3nUWt9gUzkUVtIfBntVos",  
            "https://drive.google.com/uc?export=view&id=1b_khpFWneZv5ltztlxqgOa0hmikLcCuB",
            "https://drive.google.com/uc?export=view&id=1bV6TfE9OvS3qGNBTXsFBARTJHIeCR37c",
            "https://drive.google.com/uc?export=view&id=1bO9tzWCoMeS1D84N5rLNXdMhrP9di30z",
            "https://drive.google.com/uc?export=view&id=1bZpYFS3IOkFSMUz_j7Eu9w2WTk_DKb72",
            "https://drive.google.com/uc?export=view&id=1cAnW0aYniMW0Ns_RgrpeaLaAnARcJ_rF",
            "https://drive.google.com/uc?export=view&id=1cADmJF57wfuO67Arx8xmWnAL0E6-UALm",
            "https://drive.google.com/uc?export=view&id=1bwGJzlhUSOq0Z6xNHDWUkA_FvFsPQjoX",
            "https://drive.google.com/uc?export=view&id=1bgrreaQdzJsr3m_p4hxaC3gSUqzAcyZ4",
            "https://drive.google.com/uc?export=view&id=1bocKtaH0MgalLIsda8eNTrDgo32FX2uE",
            "https://drive.google.com/uc?export=view&id=1bIMZ6DTjpX5bvpukkU5kW1oQSVKhzhxk",
            "https://drive.google.com/uc?export=view&id=1c-1WvGA4yN1OK2ro27y8hz5-DIK9SZf_",
            "https://drive.google.com/uc?export=view&id=1c7kCfuJ2DgBEu_dH4GFmKkoD_idu5Ihq",
            "https://drive.google.com/uc?export=view&id=1c-u2FiuVJT5HqKMWEYi4iIUD1PgcKXt2",
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
                "pesan":"Semangat Kuliahnya Kakak dan jangan patah semangat"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kakak ini asik dan ramah",  
                "pesan":"selalu ceriaa ya kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya keren dan lucuu banget",  
                "pesan":"semangat kak skripsinya dan ditunggu wisudanya"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya asikk dan keren",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya lucuu pol",  
                "pesan":"ditunggu wisudanya kak"
            },
            {
                "nama": "Rizki Adrian Bennofry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abang ini seru dan ramah banget",  
                "pesan":"semangat kuliahnya bang dan ditunggu wisudanya"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@rafiramadhanmaulan",
                "kesan": "abang ini lucu dan ramah",  
                "pesan":"semangat kuliahnya bang"
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
                "pesan":"semangat kuliahnya kakak"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfawwwww",
                "kesan": "Kakak ini baikk dan humble",  
                "pesan":"selalu semangatt ya kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya ramahh",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Main Volly",
                "sosmed": "@@izzalutfiaa",
                "kesan": "Kakak asik diajak ngobrol",  
                "pesan":"semangat kak dan selalu jadi orang baik terus ya kak"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak ini cakep dan asik banget",  
                "pesan":"semangat menjalani kehidupan selalu kak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "abang ini pendiem dan baik",  
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
                "kesan": "Kakak ini unik dan lincah banget",  
                "pesan":"selalu ceria ya kakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fN8bV0t4IpK5Lo7NKX0ABdT30dr2KKkx",#1
            "https://drive.google.com/uc?export=view&id=1ehnRl8y4MUCdLw691jhKjQnLuvi-E8e8",#3
            "https://drive.google.com/uc?export=view&id=1fXsyz7iSITf8buA2zFRRc52uN2T-96MI",#4
            "https://drive.google.com/uc?export=view&id=1erTnz01TysSwDa3mggQgsf7y9bJKoojc",#5
            "https://drive.google.com/uc?export=view&id=1eqhThAQTaKKwz0wSMLtP-_0blYUCsv9p",#6
            "https://drive.google.com/uc?export=view&id=1fSGbb_K3BzmnmVsSjRFhJkxMSPacaHPE",#7
            "https://drive.google.com/uc?export=view&id=1feIU6Aib19EfUpSZNvdEmcUlnDqx_Xst",#8
            "https://drive.google.com/uc?export=view&id=1evMH_usIPQwd74SERUnK1Di9B-RVov3A",#9
            "https://drive.google.com/uc?export=view&id=1f1xfefPRGUdbK10xkOjRN4EA_q87w9du",#10
            "https://drive.google.com/uc?export=view&id=1fMNiS4KBoRYdETd7kwTT8CwjVqj4JIYw",#11
            "https://drive.google.com/uc?export=view&id=1fDFJutH8QC2HXndjZQDj_tYGv2_rySwD",#12
            "https://drive.google.com/uc?export=view&id=1elhiMenlPEN0RQ0C2KiWvNR52PN3lTKL",#13
            "https://drive.google.com/uc?export=view&id=1fK592hTEDBFMJaiIhsuzwZP-bbiTCK-9",
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
                "kesan": "Abang sangat menginspirasi dan keren banget",  
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
                "kesan": "Kakaknya baik dan positive vibes",  
                "pesan":"semangat terus kuliahnya kak"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "abang ini sangat membantu dan mudah diajak bicara.",  
                "pesan":"diperlancar segala urusan ya bang"# 3
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
                "pesan":"Semoga selalu sukses ya kak"# 5
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
                "pesan":"bahagia terus ya bang"# 7
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar.resdika",
                "kesan": "abangnya asik",  
                "pesan":"Semoga semua usaha abang membuahkan hasil yang memuaskan!!"# 8
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
                "kesan": "kakak ini super ramah",  
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
                "kesan": "kakak ini baik sekali",  
                "pesan":"Semoga Kakak selalu bahagia"# 11
            },
            {
                "nama": "Yosia Letare Banurea",
                "nim": "121450149",
                "umur": "21",
                "asal":"Dairi",
                "alamat": "Perum Griya Indah",
                "hobbi": "Bawa motor tapi pake kaki",
                "sosmed": "@yosiabanurea",
                "kesan": "Kakak sangat bijaksana.",  
                "pesan":"Semoga Kakak selalu berhasil dalam semua yang dilakukan!!"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "abang ini penuh pengalaman.",  
                "pesan":"bahagia terus ya bang "# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eLfNFQIzRV8Vpo_FezfVCx4q5ROGHSQa",
            "https://drive.google.com/uc?export=view&id=1eQPm2-TcDsLH1xnAA0rwSiSrz17beh4z",
            "https://drive.google.com/uc?export=view&id=1eX5IQOPge0-8mSbodNVM1_MUCTI0Zn1v",
            "https://drive.google.com/uc?export=view&id=1eQ5m8ohjxp4eyW7AIfFAdEVETQZp9-k1",
            "https://drive.google.com/uc?export=view&id=1dkjXXc5gEvavoDTv0wakmkpc7DPtgibR",
            "https://drive.google.com/uc?export=view&id=1dlYRu9VSiU_8HjdQwaK7LR6ratrG_Iyh",
            "https://drive.google.com/uc?export=view&id=1eCYzvvZSEGYLDNOp-wZXycWBK23ojKaM",
            "https://drive.google.com/uc?export=view&id=1dyUutA_wgiQflzw9jE5osZWZpzyZWmWp",
            "https://drive.google.com/uc?export=view&id=1dvLH5if-D7PV2bPwdvbhV4uPjrH8LgkI",
            "https://drive.google.com/uc?export=view&id=1dwV58CNvEtCxPkQzKLxczgPvzeOwIj4G",
            "https://drive.google.com/uc?export=view&id=1eAU43kEFnG2jVCwS8HoI1fto48RZixWZ",
            "https://drive.google.com/uc?export=view&id=1edwllDM5i0PX3QyAVCwd_hhKFsbvw4P9",
            "https://drive.google.com/uc?export=view&id=1eeES8pGm-DAHTkwyk8XwPID7uzJGJ9id",
            "https://drive.google.com/uc?export=view&id=1ec4udkeo1s6hdrUImqPGiYXyP-hjbkqr",
            "https://drive.google.com/uc?export=view&id=1drxvvZwwCveDI9i5Tj79qeeIsHmunRuh",
            "https://drive.google.com/uc?export=view&id=1eb0YTcxLLx3Q9mEZJkv9bIQEO04eMshl",
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
                "kesan": "kakak ini cantik sekali dan soft girl",  
                "pesan":"semangat ngejar semua hal kak"
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Kakak keliatan pintar dan postif vibes",
                "pesan":"semangat kak buat kuliahnya"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "Bang jeremy asik dan suka bercanda",  
                "pesan":"semangat bang ngejar cita - cita nya"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "kakaknya sangat responsif dan lucu",  
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
                "kesan": "kak ini sangat kalem",  
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
                "kesan": "Bang keliatannya asik",  
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
                "kesan": "Kakak ini super asik dan lucu",  
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
                "kesan": "abang ini responsif",  
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
                "kesan": "Kakak sangat sopan dan asik sekali",  
                "pesan":"bahagia terus kak!"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakak ini baikk",  
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
                "kesan": "abang ini sangat baik",  
                "pesan":"semangat terus kak kuliahnya!"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "abang ini ramahh",  
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
                "kesan": "abang ini kalem dan baik",  
                "pesan":"bahagia terus ya bang!"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "abang ini baikk",  
                "pesan":"semangat terus bang belajarnya!"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kakak ini dini sangat sopan dan asik sekali",  
                "pesan":"semangat terus kak menjalani kehidupan!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aIWSsuoH27tLzyXjFyFAaYwaUKAj-M4G",
            "https://drive.google.com/uc?export=view&id=1alnR1cMoV52cksUfxKz67G6oDv4vq6Rf",
            "https://drive.google.com/uc?export=view&id=1aUwpSGkX5zFhVIPuriqdjqD36eZhPNKj",
            "https://drive.google.com/uc?export=view&id=1apNC9YApH1xahNyQ2S12eMNur83h-n_6",
            "https://drive.google.com/uc?export=1mi6TZoIa6T-7y-u1sNb9Em0Zmk3qbv_i",
            "https://drive.google.com/uc?export=view&id=1jggLu0P8V8khpaAtI56cJ0SpsJr0aWKx",
            "https://drive.google.com/uc?export=view&id=1aa7uwKJZetEcrulDoxuuKI9bSahvM5Fb",
            "https://drive.google.com/uc?export=view&id=1aacBPqKJcpIpN-1GR0skS7GDtA0d2dEV",
            "https://drive.google.com/uc?export=view&id=1mXYHrNXrskYVtdbpsamkIZsPHqCfxtHu",
            "https://drive.google.com/uc?export=view&id=1maY9D7joacoVj7rFry0ipW-vDvF4O3qZ",
            "https://drive.google.com/uc?export=view&id=1m79gEn4y1sSl49wVWM8nj-gODwBwrPUQ",
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
                "kesan": "sangat informatif",  
                "pesan":"ditunggu wisudanya bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto ",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@Adhistysa_",
                "kesan": "kakany baik poll",  
                "pesan":"bahagia selalu kakk"
            },  {
                "nama": "Nabila azhari ",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "kakaknya ramah sekali",  
                "pesan":"ceriaa selalu ya kak"
            },  
            {
                "nama": "Ahmad Rizqi ",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@Ahmda.riz45",
                "kesan": "abangnya asik",  
                "pesan":"semangat bang kuliahnya"
            },      
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "keren banget bang",  
                "pesan":"sukses selalu bang"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "tipe cowok soft spoken abang ini",  
                "pesan":"bahagia terus kak"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakaniaa",
                "kesan": "kakanya ramah dan baikk",  
                "pesan":"semangat mengejar gelarnya kak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanfir",
                "kesan": "kakaknya super baik",  
                "pesan":"ceria selalu ya kakk dimanapun"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alfiagntng",
                "kesan": "kakaknya lucu",  
                "pesan":"sukses terus kak apapun pilihan kakak"
            },
            {
                "nama": "Dhafin Rezaqa Luthhfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "abangnya baik dan ramah",  
                "pesan":"semoga bahagia terus ya bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "12145002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "kakaknya lucu sekali dan ramahh",  
                "pesan":"semangat kak kuliahnyaa"
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()

