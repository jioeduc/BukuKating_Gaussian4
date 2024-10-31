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
                "kesan": "Abang ini asik saya kagum dengan dia",  
                "pesan":"Semoga sukses selalu dalam studi dan aktivitas bang!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar", 
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang !!!" # 2
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
            "https://drive.google.com/uc?export=view&id=18V7KLWDgGnCUDnd4dPzFWHMYOwKxi7T2",#2
            "https://drive.google.com/uc?export=view&id=18U_Ly6xJlxFHsOQfFIn01ze2iuJ55MKu",#3
            "https://drive.google.com/uc?export=view&id=18dWuWI8GD65UEkc6lPbpDcBR3nuf3FGI",#4
            "https://drive.google.com/uc?export=view&id=18gUZ788vVWGSDf6prMPTSC5zu92NouFy",#5
            "https://drive.google.com/uc?export=view&id=18Xz7H4yGUIzMWQyHvNEIX76xqmqP2XJf",#6
            "https://drive.google.com/uc?export=view&id=18ZxH2WSpR8Y1sfMwZOeQMVJJjY_NSua7",#7
            "https://drive.google.com/uc?export=view&id=18_RjtrrXy5fz1_5HVOalXSCdbxQiymnn",#8
            "https://drive.google.com/uc?export=view&id=18bhNoBQ0CBfGrOzWcK2hRaUbMlm-IPKS",#9
            "https://drive.google.com/uc?export=view&id=18YISLUtCwA3XP2JlxiG5WSqEu5U2_fbs",#10
            "https://drive.google.com/uc?export=view&id=19aOQC7WIyunKwVPIXscLq_f1ld0URcWp",#11
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
                "nim": "122450004",
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
                "kesan": "Abang sangat profesional dan ramah.",  
                "pesan":"Semoga abang sukses dalam setiap langkah ke depan!!"# 4
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan khobam",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya baikk, keren!!",  
                "pesan":"Semoga kebahagiaan selalu menyertai Abang!!"# 5
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kopri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang memiliki kepribadian yang ramah dan menyenangkan.",  
                "pesan":"semangat terus kuliahnya bang !!!"# 6
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Sukarakarta, Jawa Tengah",
                "alamat": "Pahomaan",
                "hobbi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "abang sangat sabar dalam mengajarkan hal baru kepada kami.",  
                "pesan":"Semoga abang selalu diberi kemudahan dalam setiap usaha!!"# 7
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
            {
                "nama": "Wulan sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan": "Kakak ramah bangett!!",  
                "pesan":"Semoga lancar kuliahnya kak!!"# 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19UCjPs4XFLPHG_s0MTD5HmJmlRd-47mr",
            "https://drive.google.com/uc?export=view&id=19Z3U-7UNNQpcnMm4if8VLTIcwPrkXCwq",
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
                "kesan": "pengalaman kaka menginspirasi banget!!",  
                "pesan":"Semangat kuliah kak, terus bersinarr!!"
            },
            {
                "nama": "Ryan Bintang Wijaya ",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@Bintangtwinkle",
                "kesan": "abangnya baik banget",  
                "pesan":"menginspirasi selalu bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12aE8NC1dhhKScb3q9OnBVa_ipabM2Oz0", #1
            "https://drive.google.com/uc?export=view&id=12tuOJAMDFuKsMDrPzSg6SlOGEXAQdzGO", #2
            "https://drive.google.com/uc?export=view&id=12mYruRhwmwoQY9ElEdVzBx2zvCVDGKGg", #3
            "https://drive.google.com/uc?export=view&id=12XoxQLgyd97JRp8UZszEWJRdV9ZkoQk7", #4
            "https://drive.google.com/uc?export=view&id=12qJyWJqa-eMLgegWUZI87gIZjlYfRbZi", #5
            "https://drive.google.com/uc?export=view&id=12ho-f0Pb4QKikSqZd7lesnt7aw4OnbPQ", #6
            "https://drive.google.com/uc?export=view&id=12nzxF4O5VZsBH0D4anTrsoUkH8P6_0Vi", #7
            "https://drive.google.com/uc?export=view&id=12kL6fRVBqO3wRpZVzL_W_7csLaPqlRie", #8
            "https://drive.google.com/uc?export=view&id=12e-81dHzu3Q4ljCuEe69R6s0JMr2hfLp", #9
            "https://drive.google.com/uc?export=view&id=11xGqYNs0EeygLDovwERD6i1D6bqK5pWa", #10
            "https://drive.google.com/uc?export=view&id=12Ft9DN8YVbfNIigyTMqTHl1W-gSKD3OH", #11
            "https://drive.google.com/uc?export=view&id=11oPT6h_Ujj27eMDYGI3235co4V6JqSlr", #12
            "https://drive.google.com/uc?export=view&id=122jodsP4ii4s88o2EbR6JGZqeMBgqG0l", #13
            "https://drive.google.com/uc?export=view&id=11q7FSY3ipUtUXVbnApHf9KVYcB6Qc9dj", #14
            "https://drive.google.com/uc?export=view&id=11yMRH8ZqNOJcvfm_aK77gr6iWfswy28t", #15
            "https://drive.google.com/uc?export=view&id=12ai8qY-qy-zuCKIYrWVxiet0SWLEOQHq", #16
            "https://drive.google.com/uc?export=view&id=12S-CntW7dFBxrgUs9i0QP-oBpuzDE-By", #17
            "https://drive.google.com/uc?export=view&id=12KJVZ6QNvcyg9sSU_L9jxe2z2U_UO3hf", #18
            "https://drive.google.com/uc?export=view&id=12Qhi2O1-4_uv8znQqZ7rPa-HPM2jd3mg", #19
            "https://drive.google.com/uc?export=view&id=12b1ldKdrmbs7UgwAnUX5ifPS_jM2jutu", #20
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing", #1
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "abangnya asik buat diajak diskusii",  
                "pesan":"Semangat terus bang, semoga lulus tepat waktu"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",#2
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kakaknya seru parahh!!",  
                "pesan":"semangat terus kakk, jangan lupa berdoa "
            },
            {
                "nama": "Nisrina Nur Afifah", #3
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya seru dan asik.",  
                "pesan":"semangat kuliahnya kakk, semoga semuanya diperlancar!"
            },
            {
                "nama": "Allya Nurul Islami Pasha", #4
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami",
                "kesan": "kakak baik dan seru diajak diskusi!!",  
                "pesan":"semangat kuliahnya kakk, semoga sehat selalu!!"# 1
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty", #5
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakanya baikk, asik parahh",  
                "pesan":"Semangat selalu kak menjalani semester 5 nya!!"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah", #6
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakanyanya seru dan asik parahh",  
                "pesan":"Semoga sehat selalu kak, semangat belajarnya!!"
            },
            {
                "nama": "Ferdy Kevin Naibaho", #7
                "nim": "121450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya seru bangett",  
                "pesan":"Semangat kuliahnya bang!!"
            },
            {
                "nama": "M. Deriansyah Okutra", #8
                "nim": "121450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "abangnya asik dan menyenangkan",  
                "pesan":"Semoga sukses dan semangat selalu bangg!!"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari", #9
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
                "nama": " Deyvan Loxefall",  #10
                "nim": " 121450148 ", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanlo", 
                "kesan": "abangnya kece bangett, gokil!!",   
                "pesan":"Semangat kuliahnya bangg, semoga lulus tepat waktu!!" 
            },
            { 
                "nama": "Presilia", #11
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamy", 
                "kesan": "Kakaknya asik parahh!!",   
                "pesan":"Semangat kakk, semoga lulus tepat waktu!!" 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", #12
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjon", 
                "kesan": "Abangnya kerenn, gokil parah!!",   
                "pesan":"Semangat belajarnya bang, sukses teruss!!" 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", #13
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "abangnya menginspirasi banget, kerenn!!!",   
                "pesan":"semoga sehat selalu bang, sukses disetiap langkah!" 
            },
            { 
                "nama": "Sahid Maulana", #14
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "abangnya seru diajak ngobrol, keren bang!!",   
                "pesan":"Semoga kuliahnya lancar bang, tetap semangat!!" 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", #15
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "JBelwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Abangnya asik parah soalnya hobi kami sama!!!",   
                "pesan":"semoga hari hari abang menyenangkan!" 
            },
            {
                "nama": "M. Farhan Athaulloh", #16
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "abangnya seru bangett!!",  
                "pesan":"Semangat kuliahnya bang, semoga segalanya diperlanacar!!"
            },
            {
                "nama": "Gede Moana", #17
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "abangnya asik dan seru.",  
                "pesan":"Semangat terus kedepannya bang, semoga lulus tepat waktu!!"
            },
            {
                "nama": "Jaclin Alcavella", #18
                "nim": "121450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakanya kece bangett, menyala kakak daplok + kakak nim akuu!!!",  
                "pesan":"semoga hari-hari kakak menyenangkan, soalnya ada nak-anak gauss !!"
            },
            {
                "nama": "Rafly Prabu Darmawan", #19
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Abangnya seru, inspiratif sekalii",  
                "pesan":"Semoga hari abang selalu bahagia!!"
            },
            {
                "nama": "Syalaisha Andini Putriansyah", #20
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakaknya bikin suasana lebih baik!!",  
                "pesan":"Semangat belajarnya kak, semoga lancar kuliahnya!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19P1KmV5dIZ9EsrmUgUikGv4N_2BFPZcQ", #1
            "https://drive.google.com/uc?export=view&id=18u6B29eJRwmZQwoaMGo_FZmlNVEKuPxe", #2
            "https://drive.google.com/uc?export=view&id=1cOf7qs4buqiKf5CtvGej8zJR1LQX-dGo", #3
            "https://drive.google.com/uc?export=view&id=14VQq2any_tG_SJCRL3ra9bti1zWa6AfN", #4
            "https://drive.google.com/uc?export=view&id=14VSyDZ5Ujvuqv1n5qcOT41Ec-ezruCG4", #5
            "https://drive.google.com/uc?export=view&id=14efYTb200LRKZIcK_mp9YtnniJLzwzjU", #6
            "https://drive.google.com/uc?export=view&id=14dSo5qXgRQmTqkHk_UN0A2-rXFBeEg6C", #7
            "https://drive.google.com/uc?export=view&id=190Rp0j8JZ80DAeRL9KtDCJ7lANm_avVs", #8
            "https://drive.google.com/uc?export=view&id=14i0wQdkUWwzJxD2VRUcpDXHv23OifvjY", #9
            "https://drive.google.com/uc?export=view&id=19MhogXNol71vuuOOF52YISANmLKE7TL-", #10
            "https://drive.google.com/uc?export=view&id=14PQ2u9g6UI2Ok_av8jIhEw5xcLroRtZ6", #11
            "https://drive.google.com/uc?export=view&id=19TDZovyrsJHLLqvOAzOzH9B6auw6YMxH", #12
            "https://drive.google.com/uc?export=view&id=14WkjRsjySp1IePV8EekKS2AeSlKBKUIU", #13
            "https://drive.google.com/uc?export=view&id=18zKpdv_UhxxxCRVkfiYFqahS4NYtFmBG", #14
            "https://drive.google.com/uc?export=view&id=19JqDgnwlKhLXhKaxBQLcXMhTtUAHe277", #15
            "https://drive.google.com/uc?export=view&id=14YpGBoFbxSzzbIYuF-IaWroOqD4j1RnB", #16
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
                "kesan": "Abangnya sangat menginspirasi!!",  
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
                "kesan": "kakaknya seru bangett",  
                "pesan":"Semoga sukses selalu kak, semangat kuliahnya!!"
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Bang sahid gokil abiess, daplok gauss nih boss!!",  
                "pesan":"Semoga kuat bang ngurusin anak-anak gauss yang berisik :'"
            },

            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya asik diajak ngobrol!!",  
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
                "kesan": "bang regi keren bangett!!",  
                "pesan":"Semangat bang, jangan berhenti bersinar"
            },

            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Gg. Yudistira",
                "hobbi": "Baca novel",
                "sosmed": "@dkselsd_31",
                "kesan": "kaget kakaknya ada dua, ternyata kembarr :)",  
                "pesan":"Semangat kak, semoga kuliahnya lancar"
            },

            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@here.am.ai",
                "kesan": "Abannya baik bangett!!",  
                "pesan":"Semangat kuliahnya bang, semoga sehat selalu"
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "121450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "kakaknya asik parahh, keren kak!!",  
                "pesan":"Semangat kuliahnya kak, jangan sampai sakit"
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya positive vibe bangett!!",  
                "pesan":"Semangat semester 5 nya kak, semoga sukses selalu"
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya asik banget diajak ngobrol!",  
                "pesan":"Semangat kuliahnya kak, jangan lupa berdoa"
            },

            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Membaca",
                "sosmed": "@junitaa_0406",
                "kesan": "kakanya baik bangett, kerenn!!",  
                "pesan":"Semangat kak, semoga segala urusannya diperlancar"
            },

            {
                "nama": "Syahda Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya seru abiss",  
                "pesan":"Semangat kuliahnya kak, sukses selalu!!"
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhmn_adityaa",
                "kesan": "Abangnya kecee!!",  
                "pesan":"Semoga selalu sehat bang!!"
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "Abangnya asik bangett!!",  
                "pesan":"Semangat kuliahnya bang, semoga lulus tepat waktu!!"
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakanya asik betull!!",  
                "pesan":"Semoga sehat selalu kakk!!"
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "abangnya keren bangett, pengetahuannya luas!!",  
                "pesan":"Semangat abang pj tugas gauss"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()


elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16ROnYVGzSCKSY_Tx3ZxlJncImc5z8dAt",#1
            "https://drive.google.com/uc?export=view&id=16TtwzWUkja-Zf_GGm67UMdykUu96IgGi",#2
            "https://drive.google.com/uc?export=view&id=1bf6Am_9CcMMXDG4sDcpGAk4bO6YR4fdR",#3
            "https://drive.google.com/uc?export=view&id=1-ZJVjphZ9l4BKPiH6FjIiTA50hbYnFo2",#4
            "https://drive.google.com/uc?export=view&id=18E0P_5VxPpWNHdm7fHc0MXaEABKA8YG8",#5
            "https://drive.google.com/uc?export=view&id=18Sgb7NWcedL-AsIzV93HlE9uu4s_P_uF",#6
            "https://drive.google.com/uc?export=view&id=1-x4erNp5BYEMqk9q8anKHgX9Qw5nAvz9",#7
            "https://drive.google.com/uc?export=view&id=16Rxd3Q1NT54XVWcwOAp8HugRU382VSNl",#8
            "https://drive.google.com/uc?export=view&id=1-ZXGUe8eDqigtdhfx7vg2oT-CaLM6fL0",#9
            "https://drive.google.com/uc?export=view&id=1-vsYjWEZRdgkADck0oOd6KR6Sa2XykY4",#10
            "https://drive.google.com/uc?export=view&id=1-_7xSR-TMb-VJ6FVmLezXa_-qIvXit2H",#11
            "https://drive.google.com/uc?export=view&id=1-iqnB89A5vgHsSSl0K48CMHz1HCVtaVT",#12
            "https://drive.google.com/uc?export=view&id=1-mGafe8i8JKHwHlJrvu1id9ZxayeAlch",#13
            "https://drive.google.com/uc?export=view&id=108IjN_xAbWuudO63BBDwCCxg2Sz8fs-s",#14
            "https://drive.google.com/uc?export=view&id=18LiTfqtpmZ6TyeAb4q3DAdNbzXpHYCpa",#15
            "https://drive.google.com/uc?export=view&id=1bZarEhBNmS1nJTHu9bdOXTKOLFsrF8DB",#16
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama", #1
                "nim": "121450041",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@Yogyyyyyyyyy_",
                "kesan": "Abangnya ramah banget!!",  
                "pesan":"Semangat Kuliahnya bang!!"
            },
            {
                "nama": "Ramadhita Atifa Hendri", #2
                "nim": "121400131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya baik bangett,seriuss!!",  
                "pesan":"Semangat kak kuliahnya, semoga segalanya diperlancar!"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya baik dan ramah!!",  
                "pesan":"semangat kuliahnya kak, semoga sehat selalu!!"
            },
            {
                "nama": "Dea Mustia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kakak lucuuu!!",  
                "pesan":"semoga sehat selalu kak, lancar kuliahnya!1"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakanya baik banget asli!!",  
                "pesan":"sehat selalu kak, semangat menjalani semester 5 nya!!!"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya seruu!!",  
                "pesan":"semangat belajarnya bang, semoga kuliahnya lancar"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya ramah bangett",  
                "pesan":"semoga kuliahnya lancar bang!!"
            },
            {
                "nama": "Rizki Adrian Bennofry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "abangnya kecee",  
                "pesan":"semangat kuliahnya bang, semoga cepat lulus!!"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@rafiramadhanmaulan",
                "kesan": "abangnya asik bangett",  
                "pesan":"semangat kuliahnya bang, semoga sehat selalu"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfawwwww",
                "kesan": "Kakaknya seru bangett, gokil!!",  
                "pesan":"semangat menjalani semester 5 nya kak!!"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "abangnya baikk",  
                "pesan":"semoga sehat selalu bang, lancar kuliahnya!!"
            },
            {
                "nama": "Triayunanni",
                "nim": "122450062",
                "umur": "17",
                "asal":"Bogor",
                "alamat": "Pemda",
                "hobbi": "Bersholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya asik parahhh",  
                "pesan":"semangat kak, semoga kuliahnya lancar selalu!!"
            },
            {
                "nama": "Khalisah Zuhrah Alyaa Vannefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat kak menjalani perkuliahan ini"
            },
            {
                "nama": "Assa Doa Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Ening",
                "alamat": "Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya baik banget, kalem",  
                "pesan":"semangat kak, semoga kuliahnya lancar!!"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Planning Content",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya baik banget asli!!",  
                "pesan":"semangat semester 5 nya kakk"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Main Volly",
                "sosmed": "@@izzalutfiaa",
                "kesan": "Kakak izzah asik bangett",  
                "pesan":"semangat semester 5 nya kak, sehat selalu!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DnU6i9cW5zhyFhk03IAuFNMwrXiBjLNm",#1
            "https://drive.google.com/uc?export=view&id=1DW2_3O-cYTIHtmTVNNGaleavw9-xDbOd",#2
            "https://drive.google.com/uc?export=view&id=1DrdTUWpYst7OGVXNv_kBdhSiTyx1R7YB",#3
            "https://drive.google.com/uc?export=view&id=1DMlD_Ae55CnzHNTNgJijgaV9422ffD7r",#4
            "https://drive.google.com/uc?export=view&id=1DMz7ij4GS-jO0yMA8vfP0mp0uckAykLf",#5
            "https://drive.google.com/uc?export=view&id=1DTxa58_reMyyLfFFLNPCziAbbyfCC8gA",#6
            "https://drive.google.com/uc?export=view&id=1DWZNm-WwfxqGnqzlr_C_4IIyk6-j1PUT",#7
            "https://drive.google.com/uc?export=view&id=1DXOrglhKLVapVzvN2YqRp8gcGbNCSanD",#8
            "https://drive.google.com/uc?export=view&id=1Df6WT1KYo1kgaTWtRKV8MT4IDV3IFkJ6",#9
            "https://drive.google.com/uc?export=view&id=1Dlwt-3JB3G9pB18Ti0olnl9_kb5zfgIJ",#10
            "https://drive.google.com/uc?export=view&id=1DdHP9qED9cUGOpK7W5oe9Bol68hKr0kS",#11
            "https://drive.google.com/uc?export=view&id=1DKeDqfIXERlHbZXwMvlsCVvJH39CycH8",#12
            "https://drive.google.com/uc?export=view&id=1DcNewIsJkPLHSLO1Uvl5a42V3Gf1lDcQ",#13
        ]
        data_list = [
            {
                "nama": "Dimas Rizki Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":"Pamulang, Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "Manjat tower sutet",
                "sosmed": "@dimzrky_",
                "kesan": "pengalaman abang menginspirasi banget, dan bikin penasaran buat magang di internal!!",  
                "pesan":"semangat terus kuliahnya bang, semoga semua impian abang tercapai!!!"#1
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
                "kesan": "kakak bikin aku lebih siap dan excited buat magang!",  
                "pesan":"Semoga lancar semua urusan Kakak, selalu positif!! "# 3
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakak sangat ramah, sangat kerenn!!",  
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
                "kesan": "Kakak luar biasa, keren poll!!",  
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
                "kesan": "Abang memiliki kepribadian yang ramah dan menyenangkan!!",  
                "pesan":"semoga hari-hari abang menyenangkan !!!"# 6
            },
            {
                "nama": "Josua Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Abangnya sangat sabar dalam mengajarkan hal baru kepada kami.",  
                "pesan":"Semoga Abang selalu diberi kemudahan dalam setiap usaha!!"# 7
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar.resdika",
                "kesan": "Abang selalu berusaha menciptakan suasana yang menyenangkan.",  
                "pesan":"Semoga semua usaha Abang membuahkan hasil yang memuaskan!!"# 8
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
                "kesan": "Abang sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semoga Abang selalu berhasil dalam semua yang dilakukan!!"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abang sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semoga Abang selalu berhasil dalam semua yang dilakukan!!"# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hW1Ek0tH6k8Uat9Fqt5CpegwD1HDg28B", #1
            "https://drive.google.com/uc?export=view&id=1hVJ_ir6U_3DVRXGYAvBrFDg0t7YukRkA", #2
            "https://drive.google.com/uc?export=view&id=1gufrh0xdvKP5PC43ovQ6A5UKtdUb74Et", #3
            "https://drive.google.com/uc?export=view&id=1gpW0E6_NJ-KWCszADQJM1pZw30qJgyJK", #4
            "https://drive.google.com/uc?export=view&id=1gkKeVSn2CePv2mwwRV3mkYLhpBNTpwaH", #5
            "https://drive.google.com/uc?export=view&id=1gntzSBN4xMQLEFns2XZCqclHuAmOUZsB", #6
            "https://drive.google.com/uc?export=view&id=1h59wAlLyzU9II36SKilDA8IuaZNbhIVX", #7
            "https://drive.google.com/uc?export=view&id=1hPGRbLvGftgBiRZOydIzhjCcBlzXKi0E", #8
            "https://drive.google.com/uc?export=view&id=1h0c6_k6u1EK_oUi0QAHOiWZeIIEhplfJ", #9
            "https://drive.google.com/uc?export=view&id=1hAxfx8v7y3RlVrXIg-1uIC1Bsnq7l5hU", #10
            "https://drive.google.com/uc?export=view&id=1hNeC466q73exnzlkXY6yHqGfFLj0sSJe", #11
            "https://drive.google.com/uc?export=view&id=1hlY_y3MgNIuGGgpQhikcZIJqQbBqC6iD", #12
            "https://drive.google.com/uc?export=view&id=1ht8SRQzIOehKTUjKhCExAUAXqduo9QqK", #13
            "https://drive.google.com/uc?export=view&id=1hlTr2ySTgKAkPErpT0tF7ifJRF_KrGXy", #14
            "https://drive.google.com/uc?export=view&id=1htYtg5zR1c8OjwTaLJpTm1pjktBPXURn", #15
            "https://drive.google.com/uc?export=view&id=1hKtUWVsg7z45FVJdFS3sfk1_V6k_Ayzb", #16
            
        
        ]

        data_list = [
            {
                "nama": "Wahyudianto", #1
                "nim": "121450040",
                "umur": "22",
                "asal":"Makkasar",
                "alamat": "Sukarame",
                "hobbi": "Nonton Netflix",
                "sosmed": "wayyulaja",
                "kesan": "Abangnya baik banget, makasih!",  
                "pesan":"semoga lulus tepat waktu bangg!"
            },
            {
                "nama": "Elok Fiola", #2
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@Elokviola",
                "kesan": "kakaknya inspiratif bangett!!",  
                "pesan":"semangat kuliah nya kakk!!"
            },
            {
                "nama": "Cintya Bella", #3
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cyhntiabella18",
                "kesan": "Kakak cantik bangett, keren kakk!!",  
                "pesan":"semangat kak kuliahnya, semoga lancar!!"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri", #4
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "kak cia asik parahh",  
                "pesan":"semangat kuliahnya kakk, semangat menghadapi semester 5!!"
            },
            {
                "nama": "Rahma Neliyana", #5
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@Rahmaneliyana",
                "kesan": "kakaknya sangat amat positiff!!",  
                "pesan":"semangat kak kuliahnya!!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah", #6
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "kakaknya baikk, seru deh!",  
                "pesan":"semangat kak ngejar cita - citanya"
            },
            {
                "nama": "Muhammad Kaisar Firdaus", #7
                "nim": "122450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Maih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "abangnya supportif banget!!",  
                "pesan":"semangat bang menjalani semester 5"
            },
            {
                "nama": "Dwi Ratna Anggraeni", #8
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kakaknya super asik dan lucu",  
                "pesan":"semangat kulianya kakk, sehat sehat selalu!"
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy", #9
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@aimnn.as",
                "kesan": "abangnya baikk, gokil lahh!!",  
                "pesan":"semangat bang, semoga kuliahnya lancar"
            },
            {
                "nama": "Nasywa Nur Afifah", #10
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kreatif banget kakaknya!!!",  
                "pesan":"semangat terus kak kuliahnya!"
            },
            {
                "nama": "Priska Silvia Ferantiana", #11
                "nim": "121450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kakak seru bangett, keren deh!!",  
                "pesan":"semangat terus kak belajarnya!"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama", #12
                "nim": "121450111",
                "umur": "-",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@Arsalutama",
                "kesan": "abangnya inspiratif banget, keren deh pokoknya!!",  
                "pesan":"semangat terus bang kuliahnya!!"
            },
            {
                "nama": "Abit Ahmad Oktarian", #13
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Abangnya kuece poll!!",  
                "pesan":"semangat bang semster 5 nya!!!"
            },
            {
                "nama": "Akmal Faiz Abdillah", #14
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@akmal.faiz",
                "kesan": "pengetahuan bang akmal luas bangett, keren bang !!",  
                "pesan":"semangat terus bang, jangan lupa istirahat bang!!"
            },
            {
                "nama": "Hermawan Manurung", #15
                "nim": "121450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanmanurung",
                "kesan": "bang hermawan menginspirasi banget, kreatif, seru diajak ngobrol!!",  
                "pesan":"semangat terus bang, jaga kesehatan"
            },
            {
                "nama": "Khusnun Nisa", #16
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kakaknya seru diajak ngobrol!!",  
                "pesan":"semangat terus kak belajarnya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11YAMMaHd6EffuadYQM9dR6YN7TwwP54O", #1
            "https://drive.google.com/uc?export=view&id=11E7A9-tVtUBc5CVm82vu1mgIcP3URR84", #2
            "https://drive.google.com/uc?export=view&id=11Nd0eYNBo-TehLCTWIxiQhbEKFXdnFOw", #3
            "https://drive.google.com/uc?export=view&id=110bqS6Zmjl620d2Qh9lYZCXCnY_VE72d", #4
            "https://drive.google.com/uc?export=view&id=10wAqKszS4OfEpH8c09LwRhIXGKS_f59w", #5
            "https://drive.google.com/uc?export=view&id=10xkyAkEmKQ4tHkjrnxMZa0L3siVpKpSZ", #6
            "https://drive.google.com/uc?export=view&id=11N9RAvBCBpTMT5Ijmas0my7dTB5CCASB", #7
            "https://drive.google.com/uc?export=view&id=14saW4Uoup_rcch_I61FYVpAedTAuKr9o", #8
            "https://drive.google.com/uc?export=view&id=11c__qaM8ndTS1oGhSWoR7dxNyiaXAJFp", #9
            "https://drive.google.com/uc?export=view&id=11XisGhi4OESKSJWPVr-nadMRSAg09UY2", #10
            "https://drive.google.com/uc?export=view&id=14uADJSvHLchWfCGG70d2YFmMhStrgzML", #11
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol ", #1
                "nim": "121450090",
                "umur": "20",
                "asal":"Sidikalang",
                "alamat": "Dekat penjara",
                "hobbi": "Nyari hobi",
                "sosmed": "@Andrianelgaol",
                "kesan": "abangnya baikk, gokil!",  
                "pesan":"Semoga lulus tepat waktu bangg, semangat!!"
            },
            {
                "nama": "Adisty Syawaida Ariyanto ", #2
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@Adhistysa_",
                "kesan": "Ramah banget kakaknya!!",  
                "pesan":"Semangat kak, semoga sehat selalu!!"
            },
            {
                "nama": "Nabila azhari ", #3
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "kakak baikk, inspiratif bangett!!",  
                "pesan":"sehat selalu kak, semoga lulus tepat waktu!"
            },  
            {
                "nama": "Ahmad Rizqi ", #4
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@Ahmad.riz45",
                "kesan": "abangnya kerenn!!",  
                "pesan":"semangat kuliiah nya bang!!"
            },
            {
                "nama": "Danang Hilal Kurniawan", #5
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan":"abang asikk, enak diajak ngobrol",  
                "pesan":"semangat kuliahnya bang, semoga lancar selalu"
            },
            {
                "nama": "Farrel Julio Akbar", #6
                "nim": "122450110",
                "umur": "20",
                "asal":"Salatiga",
                "alamat": "Bogor",
                "hobbi": "Jl.lapas",
                "sosmed": "@farrel__julio",
                "kesan":"abangnya asik, gokil parah!!",  
                "pesan":"semangat kuliahnya bang!!"
            },
            {
                "nama": "Tessa Kania Sagala", #7
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@Tesakaniaa",
                "kesan":" kakaknya baik bangett, keren pokoknya",  
                "pesan":"sehat selalu kak, semangat menghadapi semester 5!!"
            },
            {
                "nama": "Nabilah Andika Fitriati", #8
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanfir",
                "kesan":"kakaknya humblee, keren kakk!!",  
                "pesan":"sehat-sehat kakak, semangat kuliahnya kak"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng", #9
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alfiagntng",
                "kesan":"kakaknya menginspirasi banget!",  
                "pesan":"sehat selalu kakk, semoga bahagia!!"
            },
            {
                "nama": "Dhafin Rezaqa Luthhfi", #10
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnyaa baik, keren bang!!",  
                "pesan":"semangat kuliahnya bang, sukses selalu"
            },
            {
                "nama": "Elia Meylani Simanjuntak ", #11
                "nim": "12145002",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "kakaknya enak diajak ngobrol, kreatif juga, gokil parahh",  
                "pesan":"semangat kuliahnya kak, semoga lulus diwaktu yang diinginkan!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()