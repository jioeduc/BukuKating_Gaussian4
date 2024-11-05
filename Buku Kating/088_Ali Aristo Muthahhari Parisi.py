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
                "sosmed": "@gumilangkharisma",
                "kesan": "Bang Gumilang baik dan banyak pengalaman seru.",  
                "pesan":"Semangat terus bang, teruslah menemukan inspirasi dari musik dan semoga semua cita-citanya segera tercapai."# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Bang Pandra seru dan keren.",  
                "pesan":"Terus semangat main gitarnya bang. Semoga kuliahnya lancar dan impiannya tercapai."# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kak Meliza seru dan asik.",  
                "pesan":"Terus semangat kuliahnya kak dan semoga sukses selalu dan bisa terus menonton drakor favoritnya."# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kak Hartiti kalem dan keren.",  
                "pesan":"Semangat terus nyanyinnya kak dan Semoga sukses selalu dalam perjalanan hidup dan kuliah."# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kak Putri kece dan seru.",  
                "pesan":"Terus semangat dengerin Bang Pandra gitaran dan sukses dalam segala hal."# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Kura-kura",
                "sosmed": "@nadillaandr26",
                "kesan": "Kak Nadilla punya hobi menarik dan asik.",  
                "pesan":"Semangat ngerawat kura-kuranya dan Semoga semua yang diinginkan tercapai kak."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()




elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14O4qO1l9TYSDk6xs-ZFbiTh0blNp_co-",#1
            "https://drive.google.com/uc?ex/port=view&id=13p1uMYMMCQUERVd7NYvPYjOqS8_mO60i",#2
            "https://drive.google.com/uc?export=view&id=13k9URuNPCXTzFOVFI8IHBnNQlHLFuRQg",#3
            "https://drive.google.com/uc?export=view&id=13qRSF7z4DtkjD23H0eA8gE3kqT95pLDQ",#4
            "https://drive.google.com/uc?export=view&id=13r9FKQG_K3xfj9ItVML_g3ib9qpf9-I3",#5
            "https://drive.google.com/uc?export=view&id=14T9y86d_B5DqghQvLpQW1ysB8gyjZMUL",#6
            "https://drive.google.com/uc?export=view&id=14K_EGfL_ILNh5Rt4RGMRqFHOmPoTwTmG",#7
            "https://drive.google.com/uc?export=view&id=14IZAAHaGCkSdybsk_SSq7jpH9yFvV1Bu",#8
            "https://drive.google.com/uc?export=view&id=144xD1Kbck9T_CIe2QdSP4NYP-aD6Dwvz",#9
            "https://drive.google.com/uc?export=view&id=14LwQhnNTEj9yu-GvbVPxoBf-NiB0qffE",#10
        ]
        data_list = [
            {#1
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
            {#2
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Journal",
                "sosmed": "@dylebee",
                "kesan": "Kakaknya baik dan menyenangkan.",  
                "pesan":"Semangat terus kuliahnya kak dan semoga sukses dan bisa mencapai apa yang diimpikan."
            },
            {#3
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
            {#4
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
            {#5
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
            {#6
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
            {#7
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
            {#8
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
            {#9
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
            {#10
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
            "https://drive.google.com/uc?export=view&id=1zdIUHATFKtFqIhlQLc8Fxav5kJ4P7vnO",
            "https://drive.google.com/uc?export=view&id=1zf4sW59-RWrgr84XiRYUROa75Q-RM-ar",
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
                "kesan": "Kakaknya inspiratif",  
                "pesan":"Semanagat terus kuliahnya kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang bintang asik",  
                "pesan":"Semangat terus dan jaga kesehataanya bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xgFwwEo6MTVNsN1sRLJvzZ-LTKNY6Bka",
            "https://drive.google.com/uc?export=view&id=1wwyIzVVNc1vLTu0jpPv7Vzh5EBt4BmiB",
            "https://drive.google.com/uc?export=view&id=1xmJ-aV4Mg2HFS8kHZXNQpF6MUd1c_soU",
            "https://drive.google.com/uc?export=view&id=1xiSN5i1s4EchhSQtJWMJvpnjdGbS8lEF",
            "https://drive.google.com/uc?export=view&id=1x7p8I8KbBNksshzTGuuJWnNlE_XIOrBE",
            "https://drive.google.com/uc?export=view&id=1xmdhC27TbTF5fAT4cIeK4oRx6_3gmMbU",
            "https://drive.google.com/uc?export=view&id=1wqj2rxyF3gKFXgGZpi7TugOqD3Xcorrd",
            "https://drive.google.com/uc?export=view&id=1wzPmJ7OKFF9AVZxPjw41KlrWR-3_6K4v",
            "https://drive.google.com/uc?export=view&id=1xNy8vHL-qHE4uMMt7Js6JS7Fuicq2xPa",
            "https://drive.google.com/uc?export=view&id=1wxhxb3uLNZLLpMuP_8dzCfJJ_MHb_4Il",
            "https://drive.google.com/uc?export=view&id=1wa8-eoMn5rFN14BvBPXLJwRD5ixOCS6H",
            "https://drive.google.com/uc?export=view&id=1wf09BKCtq91Q0Ow11pJZA6VkRk7Hts6t",
            "https://drive.google.com/uc?export=view&id=1wOds3y6j_geCBon7X6dmxnc7QiT1iS0Q",
            "https://drive.google.com/uc?export=view&id=1wpRLz3iQf89MRvUp_ipUdPTUE3z_P1H8",
            "https://drive.google.com/uc?export=view&id=1weIO6HuZO0vkCSMllGi36bXXs7dSCx1v",
            "https://drive.google.com/uc?export=view&id=1xr88qbMjcnJWgQ31mkLjmoj4ZQAJMGtb",
            "https://drive.google.com/uc?export=view&id=1y4GdkGm2VbHXmRqC-5C9sLclXYVfw6b6",
            "https://drive.google.com/uc?export=view&id=1yNWfEX7j76EfA_ClEyh-KkMwJYMvDrbc",
            "https://drive.google.com/uc?export=view&id=1y9NVEyLrxZA28ngX0D8OR8aVr_lq101P",
            "https://drive.google.com/uc?export=view&id=1y9QgZtadD6iXVVvHzYWBprsNCJbtruwz",
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
                "kesan": "Bang Ericson seru punya banyak pengalaman tetang organisasi",  
                "pesan":"Semangat travellingnya bang sama rekomendasi tempat travelling dan semoga tercapai semua keinginannya."
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabethh_",
                "kesan": "Kak Elisabeth orangnya ceria dan keren",  
                "pesan":"Semangat terus menjalani segala aktivitasnya kak dan sukses selalu dalam segala hal"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Jail",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Afifah tegas orangnya.",  
                "pesan":"Semoga dipermudah segala urusan dan tercapai semua mimpinya kak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Ngukur lampu",
                "sosmed": "@allyaislami_",
                "kesan": "kak Allya serius orangnya.",  
                "pesan":"Sehat selalu buat kak Allya dan semoga dipermudah dalam mewujudkan cita-citanya."
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Lubuk Linggau",
                "alamat": "Rajabasa",
                "hobbi": "Nitip sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kak Eksanty orangnya asik dan tegas",  
                "pesan":"Sukses terus buat kak Eksanty dan semoga tercapai semua keinginannya."
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Minum Kopi",
                "sosmed": "@farahanumafifahh",
                "kesan": "kak Farahanum seru dan asik",  
                "pesan":"Semoga sehat selalu kak dan minta rekomendasiin kopi yang enak."
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Bang ferdy orangnya serius",  
                "pesan":"Semangat mewujudkan keinginan dan sehat selalu bang."
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Nyari Angin Malam",
                "sosmed": "@dransyh_",
                "kesan": "Bang Derianssyah orangnya asik dan menyenangkan",  
                "pesan":"Jangan lupa jaga keshatannya bang biar bisa terus cari angin malam dan semoga terwujud semua mimpinya"
            },
            {
                "nama": "Oktavia Nurwinda Puspitasari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Ngeliatin tingkah orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kak Oktavia orangnya asik dan menyenangkan",  
                "pesan":"Sehat selalu dan Semoga dipermudah jalan mewujudkan mimpinya kak."
            },
            { 
                "nama": "Deyvan Loxefal", 
                "nim": "121450148", 
                "umur":  "21", 
                "asal":" Duri Riau  ", 
                "alamat": "Khobam Pulau Damar", 
                "hobbi": "Belajar", 
                "sosmed": "@depanloo", 
                "kesan": "Bang Deyvan orangnya seru dan lucu",   
                "pesan":"Semangat terus belajarnya bang dan semoga apa yang diharapkan tercapai semua bang." 
            },
            { 
                "nama": "Presilia", 
                "nim": "122450081", 
                "umur": "20", 
                "asal":"Bekasi", 
                "alamat": "Kota Baru", 
                "hobbi": "Dengerin the adams", 
                "sosmed": "@presiliamg", 
                "kesan": "Kak Presilia asik dan seru.",   
                "pesan":"Sukses selalu kak dan minta rekomendasinya kak satu lagu the adams yang paling bagus." 
            },
            { 
                "nama": "Johannes Krisjon Silitonga", 
                "nim": "122450043", 
                "umur": "19", 
                "asal":"Tangerang", 
                "alamat": "Jl. Lapas", 
                "hobbi": "Ngasprak", 
                "sosmed": "@johanneskrisjnnn", 
                "kesan": "Bang Johannes seru dan serius orangnya",   
                "pesan":"Jaga kesehatannya bang biar bisa ngasprak terus dan semoga semua mimpinya terwujud." 
            },
            { 
                "nama": "Kemas Veriandra Ramadhan", 
                "nim": "122450016", 
                "umur": "19", 
                "asal":"Bekasi", 
                "alamat": "Kojo Golf UIN", 
                "hobbi": "Main ular digital", 
                "sosmed": "@kemasverii", 
                "kesan": "Bang Kemas baik dan jago ngoding",   
                "pesan":"Semangat terus kuliahnya dan semoga dipermudah jalan kesuksesannya bang" 
            },
            { 
                "nama": "Sahid Maulana", 
                "nim": "122450109", 
                "umur": "21", 
                "asal":"Depok, Jabar", 
                "alamat": "Jl. Airan Raya", 
                "hobbi": "Dengerin musik", 
                "sosmed": "@sahid_maul19", 
                "kesan": "Bang Sahid baik dan seru",   
                "pesan":"Sukses selalu bang dan minta rekomendasiin lagu yang enak didengerin pas sendirian bang." 
            },
            { 
                "nama": "Rafa Aqilla Jungjunan", 
                "nim": "122450142", 
                "umur": "20", 
                "asal":"Pekanbaru", 
                "alamat": "Belwis", 
                "hobbi": "Baca webtoon", 
                "sosmed": "@rafaaqilla", 
                "kesan": "Kak Rafa kalem dan menyenangkan orangnya",   
                "pesan":"Sukses selalu dan Semoga tergapai semua mimpinya kak. Sama minta rekomendasiin webtoon yang seru kak buat pas libur kak." 
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Bang Farhan seru dan seru orangnya.",  
                "pesan":"Jaga kesehatan dan jangan bosen dampingin peserta lomba bang. Sukses selalu bang."
            },
            {
                "nama": "Gede Moena",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "Bang Gede asik dan baik",  
                "pesan":"Sukses selalu bang dan jaga kesehatannya biar hobinya lancar terus jalannya."
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kak Jaclin seru, baik, dan Menyenangkan",  
                "pesan":"Semangat terus berenangnya dan jangan bosen ngebimbing anak gauss kak. Semoga terwujud semua cita-citanya."
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Bang Rafly Asik dan kalem orangnya",  
                "pesan":"Semoga dipermudah jalan mewujudkan mimpinya dan jangan lupa jaga kesehatannya biar lancar ngegamenya"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kak syalaisha baik dan kalem.",  
                "pesan":"Seelalu jaga kesehatannya kak biar hobi bacanya lancar jalnannya dan semangat terus mewujudkan cita-citanya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-_KXY0BR-VrHKCJl-HQuDr6JFWqy_as6",
            "https://drive.google.com/uc?export=view&id=1-GeR-OSDWcsXj5ZvhdrplM_bZ5593FtD",
            "https://drive.google.com/uc?export=view&id=100-qHwvUmkz6g5OgmaagFHSyGV3uOAmC",
            "https://drive.google.com/uc?export=view&id=1zwX0ldwIF0wKTiRut9M_bh6xOHRSXvcJ",
            "https://drive.google.com/uc?export=view&id=1-gx5rfBYc-81ReQlTtX_fgmMkJfxYADS",
            "https://drive.google.com/uc?export=view&id=1-pCZqVJsxzGx3gwhuN_T_33PWgQ3vwbi",
            "https://drive.google.com/uc?export=view&id=1-Q-lyZ1Y3xkbdgSQSVD-RXQbC0PIw8h4",
            "https://drive.google.com/uc?export=view&id=1-BtEAwfXtPzA-HYAOHbIQHxsLxQw45iS",
            "https://drive.google.com/uc?export=view&id=1-mexWdJP6-m4YJrvBgQ2eY-OGwDEn229",
            "https://drive.google.com/uc?export=view&id=100PSTT3SOdTCuNJqM8C5ZLdvLcHnzSrR",
            "https://drive.google.com/uc?export=view&id=107Rin3HxK52clM_kyQxTvxebEgqGk1Qj",
            "https://drive.google.com/uc?export=view&id=1-jiAFQVJmhJhrFri-9MskQxHnqwg3_aV",
            "https://drive.google.com/uc?export=view&id=16w9pbSXyulkLhK7xAEkc_oBfLXF8Huvx",
            "https://drive.google.com/uc?export=view&id=1014bk9EUzgRiPzrZuH_Ly8vB_Ewm-nXC",

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
                "kesan": "Bang Rafi orangnya baik dan menyenangkan",  
                "pesan":"Semangat terus bang olahraganya dan sukses selalu"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl.Pulau Sebesi, Sukarame",
                "hobbi": "baca novel",
                "sosmed": "@anovavona",
                "kesan": "Kak Annisa orangnya ramah dan baik",  
                "pesan":"Semangat terus baca novel dan sukses mewujudkan mimpinya kak."
            },

            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Bang Sahid orangnya baik dan seru",  
                "pesan":"Semangat terus olahraga dan semangat terus ngerawat anak gauss bang. Semoga terwujug semua mimpinya."
            },


            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Jl.Permadi Sukarame",
                "hobbi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "Bang Regi baik dan asik",  
                "pesan":"Semangat kuliah sama ngaspraknya dan jaga kesehatannya. Sukses selalu bang."
            },

           
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Kopri",
                "hobbi": "Scroll tiktok",
                "sosmed": "@here.am.ai",
                "kesan": "Bang Anwar orangnya baik dan kalem",  
                "pesan":"Jaga kesehatannya dan semagat kuliahnya bang. Semoga terwujud semua keinginannya."
            },

            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kak Deva ramah dan menyenangkan",  
                "pesan":"Semangat terus nonton film dan kuliahnya kak dan semoga selalu dipermudah mewujudakan mimpinya."
            },

            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kak Dinda baik dan ramah",  
                "pesan":"Semangat terus belajarnya kak dan semoga selalu dipermudah mewujudkan cita-citanya"
            },

            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Main musik ",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Marleta positive vibe dan menyenangkan",  
                "pesan":"Sukses selalu dan semangat terus main musiknya kak. Semoga dilancarkan dalam menggapai mimpinya."
            },

            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kak Puspa asik dan baik",  
                "pesan":"Semangat kuliah dan ngeresumenya kak dan jaga kesehatannya selalu.  "
            },

            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Main Game",
                "sosmed": "@rhm_adityaa",
                "kesan": "Abangnya baik, asik, dan cool",  
                "pesan":"Semangat terus kuliahnya dan jaga kesehatannya bang. Sukses selalu."
            },

            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Kopri Jaya",
                "hobbi": "Lari",
                "sosmed": "@_egistr",
                "kesan": "Bang Eggi seru dan baik",  
                "pesan":"Selalu jaga kesehatan bang biar hobinya jalan terus dan sukses selalu."
            },

            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Belwis",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kak Febiya ramah dan kalem",  
                "pesan":"Semangat terus kak nonton drakornya dan mewujudkan keinginannya."
            },

            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Ayar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Bang Syahrul keren dan seru",  
                "pesan":"Selalu jaga kesehatan dan terus semangat kuliahnya band. Semoga semua mimpinya terwujud"
            },

            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten ",
                "alamat": "Sukarame",
                "hobbi": "Berkembang dan tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Bang Randa keren, baik, dan jago ngoding",  
                "pesan":"Semangat membantu bocah-bocah Gauss dan sehat selalu serta semoga terwujud semua keinginannya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1z6sW6ysPm2DuxLh72nd5B-_92Bt-CTI0",
            "https://drive.google.com/uc?export=view&id=1zDc3eKSAgSmif7YvGXwgfwbuRJDPTaE0",  
            "https://drive.google.com/uc?export=view&id=1zQ_kw_LLlUjEATuZk6NihF3LLtrJQdhN",
            "https://drive.google.com/uc?export=view&id=1zltl-_AE83pDn87Vych7hQwZ-humAQu5",
            "https://drive.google.com/uc?export=view&id=1zLSQVVKxs2pD49TuEHZzWiS0Oz0GwE9u",
            "https://drive.google.com/uc?export=view&id=1zEZhvfoTRPweJ-AiNX2xB7saf2DM-p5f",
            "https://drive.google.com/uc?export=view&id=1znA_FJJ2D_ggXJaVGRdKaW4xT8ezMS3S",
            "https://drive.google.com/uc?export=view&id=1-1l9IV2scgopMXmTHKgBysFXJL6w3r6G",
            "https://drive.google.com/uc?export=view&id=1-01NRRvrpPmLESV_0N79w3kGh3HChQ3h",
            "https://drive.google.com/uc?export=view&id=1znQITF4c15E65zSHmr809o2fcoF69Fd-",
            "https://drive.google.com/uc?export=view&id=1Qj7AobKui6Id0VM-a7dJSHCbTZeo85bs",
            "https://drive.google.com/uc?export=view&id=1zzmwz7QDjt_yzqhqs7p63nV740ca7Ptw",
            "https://drive.google.com/uc?export=view&id=1zt6to7Q08Bq_SB0Rzk4_Bf6zkkpEfZMc",
            "https://drive.google.com/uc?export=view&id=1zly-TdtK6oivLeKsB6CX5c6g_9-bQjbb",
            "https://drive.google.com/uc?export=view&id=1zarO0GCp1mBIGtEpaVOn2E7M9QDnoS-N",
            "https://drive.google.com/uc?export=view&id=10Ex67ByYvuY2VCpMq4gfvHMB5HC30yU7",
        ]
        data_list = [
            {
                "nama": "Yogy Sa'e Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@Yogyyyyyyy",
                "kesan": "Bang Yogy banyak pengalaman seru dan asik",  
                "pesan":"Selalu jaga kesehatan dan semoga terwujud segala keinginannya bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121400131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kak Ramadhita baik dan asik",  
                "pesan":"Selalu jaga kesehatannya kak biar lancar jalan-jalannya dan sukses selalu kak."
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@yo_anamnk",
                "kesan": "Kak Yohana seru dan menyenangkan",  
                "pesan":"Semangat terus buat jurnalnya kak dan semoga tercapai semua mimpinya. Sukses selalu kak."
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Nerbitin Jurnal",
                "sosmed": "@deaa.rsn",
                "kesan": "kak Dea seru dan keren",  
                "pesan":"Jaga terus kesehatannya kak biar lancar nerbitin jurnalnya dan semoga selalu dipermudah jalan mewujudkan mimpinya."
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakaknya kece dan baik",  
                "pesan":"Terus semangat kuliahnya dan selalu jaga kesehatannya kak. Sukses selalu mewujudakn mimpinya."
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Membaca Novel",
                "sosmed": "@tobiassiagian",
                "kesan": "Bang Tobias seru, keren, dan jago main basket. ",  
                "pesan":"Semangat terus baca novel dan kuliahnya bang. semoga sehat selalu dan terwujud semua keinginannya."
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton yt, main ML",
                "sosmed": "@alfaritziirvan",
                "kesan": "Bang Irvan baik dan seru orangnya",  
                "pesan":"Sukses selalu bang dan semoga sehat selalu. Minta Rekomendasiin channel yt buat tontonan pas libur"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobbi": "Joget",
                "sosmed": "@rzkdrnnn",
                "kesan": "Bang Rizki keren dan cool",  
                "pesan":"Semoga sehat selalu dan semua keiginannya terwujud. Sukses selalu buat abangnya."
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Samping Warjo",
                "hobbi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Bang Arafi seru dan asik orangnya",  
                "pesan":"Sehat selalu bang dan semoga terwujud semua mimpinya. Minta rekomendasiin masakan yang murah meriah dan mudah dibuat bang."
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang, Sumatera Utara",
                "alamat": "Sukarame",
                "hobbi": "Berbuat baik",
                "sosmed": "@chlfaw",
                "kesan": "Kakak ini baik dan menyenangkan",  
                "pesan":"Jangan pernah bosen berbuat baik kak dan semoga dari kebaikan itu dilancarkan jalan kesuksesannya."
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Ikut Seminar",
                "sosmed": "@rayths_",
                "kesan": "Bang Raid kalem dan baik",  
                "pesan":"Selalu jaga kesehatan bang biar lancar mengikuti seminarnya dan sukses selalu bang."
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "17",
                "asal":"Bogor",
                "alamat": "Pemda",
                "hobbi": "Bersholawat",
                "sosmed": "@tria_y062",
                "kesan": "Kak Tria asik dan ramah",  
                "pesan":"Semangat terus menjalani hobinya kak dan semangat kuliahnya. Semoga terwujud semua mimpinya."
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Tillawah Alquran",
                "sosmed": "@alyaavanevi",
                "kesan": "Kak Khaalishah asik dan seru",  
                "pesan":"Jaga kesehatannya kak biar hobinya jalan terus dan semoga dari hobinya dilancarkan semua keinginannya."
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara Ening",
                "alamat": "Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kak Uyi lucu, seru, dan kalem orangnya",  
                "pesan":"Semangat cari ice breakingnya dan sukses selalu kak. "
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Planning Content",
                "sosmed": "@jasminednva",
                "kesan": "Kak Ratu asik dan keren",  
                "pesan":"Selalu jaga kesehatannya kak biar lancar planning contentnya. Sukses sealu kak."
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Main Volly",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kak Izza baik dan positive vibe",  
                "pesan":"Semangat terus main vollynya kak dan jaga kesehatannya. Semoga terwujud semua keinginannya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10qmURTiRrdF3Bk2p-jQKvpHaY_YEG8BW",#1
            "https://drive.google.com/uc?export=view&id=10njvpKmyTGHUV75OnyQfNtUZtumn0CW6",#2
            "https://drive.google.com/uc?export=view&id=10paw_UBooYkdCXQaUOM6gkNKQA1Wmk97",#3
            "https://drive.google.com/uc?export=view&id=10wxdwMNRT2sFz1yeT72ZBxsMkqlHDaiZ",#4
            "https://drive.google.com/uc?export=view&id=10OLS0FU3Z0sBHm0Qzpq56Rc4cX9ZD6Bp",#5
            "https://drive.google.com/uc?export=view&id=10kX4ge73pwWMScFV1bsfRK4zmp0EVfjE",#6
            "https://drive.google.com/uc?export=view&id=10iODSCec1PtcGEM0MNbq_qqQ7kwKLtkk",#7
            "https://drive.google.com/uc?export=view&id=11-Q0P1D-KJRqv8aQsPZ3E4OpGfJUfBLo",#8
            "https://drive.google.com/uc?export=view&id=10SmZkWDoCAIwCaL-SsmHjTPzYTmqsL8q",#9
            "https://drive.google.com/uc?export=view&id=10tIwT8gpFu0jcNafbUmKNe8A7FZ0k-Lw",#10
            "https://drive.google.com/uc?export=view&id=10tXd3nQuYdgqoiR1seo8KYlVgiOeXqBf",#11
            "https://drive.google.com/uc?export=view&id=10lLBFJRl0wvdhif0i2d8EEil-q85MoJe",#12
            "https://drive.google.com/uc?export=view&id=10Q0jfvlLKKp0rJrv3lGP77kqdQYylVq5",#13
        ]
        data_list = [
            {#1
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":"Pamulang, Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "Manjat tower sutet",
                "sosmed": "@dimzrky_",
                "kesan": "Abangnya banyak pengalaman dan menginspirasi",  
                "pesan":"Semangat terus bang dan semoga segala mimpi dan keinginan terwujud"
            },
            {#2
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "Kakaknya baik dan positive vibes",  
                "pesan":"semangat terus kuliahnya kak, semoga semua urusannya diperlancar!!"# 2
            },
            {#3
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal":"Lampung barat",
                "alamat": "Labuhan batu",
                "hobbi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "Abangnya sangat membantu dan mudah diajak bicara.",  
                "pesan":"Semoga lancar semua urusan bang, sukses terus!!"# 3
            },
            {#4
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung selatan",
                "alamat": "Natar",
                "hobbi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakaknya sangat ramah.",  
                "pesan":"Semoga Kakak sukses dalam setiap langkah ke depan!!"# 4
            },
            {#5
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Menghalu",
                "sosmed": "@meiralsty_",
                "kesan": "Kakaknya luar biasa dalam membimbing.",  
                "pesan":"Semoga kebahagiaan selalu menyertai Kakak!!"# 5
            },
            {#6
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Nyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya memiliki kepribadian yang ramah dan menyenangkan.",  
                "pesan":"semangat terus kuliahnya bang"# 6
            },
            {#7
                "nama": "Josua Alfa Viando Panggabean",
                "nim": "121450061",
                "umur": "21",
                "asal":"Pematang siantar",
                "alamat": "Gia kost Gerbang barat",
                "hobbi": "Ngawinin cupang",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Abangnya sangat sabar dalam mengajarkan hal baru kepada kami.",  
                "pesan":"Semoga abangya selalu diberi kemudahan dalam setiap usaha!!"# 7
            },
            {#8
                "nama": "M. Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan dalam",
                "hobbi": "Miara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "Abangnya selalu berusaha menciptakan suasana yang menyenangkan.",  
                "pesan":"Semoga semua usaha membuahkan hasil yang memuaskan bang"# 8
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Mancing",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya sangat bersahabat dan menyenangkan!",  
                "pesan":"Semoga Kakak selalu dikelilingi orang-orang baik!!"# 9
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan",
                "hobbi": "Lihat cogan",
                "sosmed": "@slwafhn_694",
                "kesan": "Kakaknya sangat bijaksana dan penuh pengalaman.",  
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
                "kesan": "Kakaknya sangat bijaksana dan penuh pengalaman.",  
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
                "kesan": "Abangnya sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semoga selalu berhasil dalam semua yang dilakukan bang"# 12
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Nulis Lagu",
                "sosmed": "@rendraepr",
                "kesan": "Abangya sangat bijaksana dan penuh pengalaman.",  
                "pesan":"Semoga selalu berhasil dalam semua yang dilakukan bang"# 13
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-s-ZRiwnQ-NurYrCZMHS6pkpU7IUQKCm",
            "https://drive.google.com/uc?export=view&id=1-rL5WIZh6tJbLwMb8CaxJK2kI2K6fJc3",
            "https://drive.google.com/uc?export=view&id=1-fPkZA3ZHXRKQOUe-iksgBLNUJhw1vWc",
            "https://drive.google.com/uc?export=view&id=1-w30WMQ9rO17jNPKf72onvX8hYkOF4e0",
            "https://drive.google.com/uc?export=view&id=10U7r6aAtFYT-nSiFChhWys-XOf_-BPUt",
            "https://drive.google.com/uc?export=view&id=10MoffoeUaEuxDY_-HS_rXEY4y6eC-q1i",
            "https://drive.google.com/uc?export=view&id=10757DYYk7LaK1rHitpVo7aujxNy3heIy",
            "https://drive.google.com/uc?export=view&id=10WXz6DHq-dkkKH1KM0KwbgMpUmEpzw21",
            "https://drive.google.com/uc?export=view&id=101bxlF9-q8Fq7b2m4xzl8NL6RfV0JDIL",
            "https://drive.google.com/uc?export=view&id=104T4e-I3_AGh7rP6v75uHGJ6tX5oxTBR",
            "https://drive.google.com/uc?export=view&id=10Jv5h7SR9P-95ho3uqz1QNLC2JXl1fGF",
            "https://drive.google.com/uc?export=view&id=10iG6WdkzlPSd-hAgQ4WGeNHMh4XF9Q_G",
            "https://drive.google.com/uc?export=view&id=1-bRciLnor45AeR3NCB1MfT5yAEij2gTS",
            "https://drive.google.com/uc?export=view&id=10fBKaeKr1uFi-EAMVJiHgKwaI4cq51-R",
            "https://drive.google.com/uc?export=view&id=1-e_PVpIZjZpxUCwJkrhq4aVbi83a5d3C",
            "https://drive.google.com/uc?export=view&id=1-mIIBC5FiGEk1uym9Z9SqqRat1w9NG3L",
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
                "kesan": "Bang Wahyu banyak pengalman asik dan seru",  
                "pesan":"Terus explore film-film baru di Netflix bang dan semangat terus kuliahnya."
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Kak Elok ramah dan asik",  
                "pesan":"Tetap fokus dan semangat mengejar mimpinya kak."
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal":"Teluk",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kak Cintya keren dan ramah",  
                "pesan":"Semangat terus ngegymnya kak. Keep pushing your limits!"
            },
            {
                "nama": "Patricia Leondrea Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Jatimulyo",
                "hobbi": "Cubit Orang",
                "sosmed": "@Patriciadiajeng",
                "kesan": "Kak Patricia orangnya seru dan seneng bercanda keliatan dari hobinya",  
                "pesan":"Terus jadi pribadi yang ceria, kak! Semoga sukses dengan semua cita-citanya."# 1
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Jl. Kembang 5 Sukarame",
                "hobbi": "Makan Geprek",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Rahma kalem dan ramah",  
                "pesan":"Terus jalankan hobinya kak tapi jangan lupa jaga kesehatannya juga ya kak, terus semangat dan sukses kak."
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Menonton dan Bernyanyi",
                "sosmed": "@Tryyaniciaaa",
                "kesan": "Kak Try baik dan menyenangkan",  
                "pesan":"Semangat kuliahnya dan jangan berhenti mengejar cita-citanya kak."
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobbi": "Masih Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Bang kaisar orangnya asik dan ramah",  
                "pesan":"Semangat terus mencari hobinya bang dan semoga apa yang diimpikan terwujud."
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim" : "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Perumahan Pemda",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Dwiratnn_",
                "kesan": "Kak Dwi orangnya kalem dan menyenangkan",  
                "pesan":"Terus dengarkan musik yang membawa semangat kak dan Jangan pernah lelah dalam mengejar impian, sukses selalu kak."
            },
            {
                "nama": "Gymnastiar Al-Khoarizmy",
                "nim": "122450065",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobbi": "Nyari Tuyul Baskat",
                "sosmed": "@gymnn.as",
                "kesan": "Bang Gymnastiar asik dan seru keliatan dari hobinya",  
                "pesan":"Terus semangat jalanin hobi uniknya bang dan semoga apa yang diimpikan terwujud bang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Jl. Durian 1",
                "hobbi": "Bersih - bersih",
                "sosmed": "@nsywanaf",
                "kesan": "Kak Nasywa orangnya rapi dan menyenangkan",  
                "pesan":"Terus jaga hobinya kak karena kebersihan sebagian dari iman dan sukses selalu mengejar impiannya."
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl. nangka 2",
                "hobbi": "Karaoke",
                "sosmed": "@prskslv",
                "kesan": "Kak Priska Baik dan menyenangkan",  
                "pesan":"Terus nikmati hobinya kak dan semangat terus kuiahnya dan mengejar apa yang diimpikan"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka 3",
                "hobbi": "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan": "Bang Arsal seru dan ramah",  
                "pesan":"Terus semangat koleksi parfumnya bang, siapa tau nanti bisa punya merk parfum sendiri dan sukses selalu bang."
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "20",
                "asal":"Rajabasa",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Uno",
                "sosmed": "@Abitahmad",
                "kesan": "Bang Abit Menyenangkan dan baik",  
                "pesan":"Semoga menang terus bang pas main uno. Dan jangan lupa semangat mengejar cita-citanya."
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Perum Griya Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@_akmal.faiz",
                "kesan": "Bang Akmal Menyenagkan dan baik",  
                "pesan":"Semoga hobinya bisa memberi keseimbangan antara istirahat dan aktivitas bang. Sukses selalu mengejar mimpinya."
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jalan Deket Tol",
                "hobbi": "Bengong",
                "sosmed": "@Hermanman.mnrng",
                "kesan": "Bang Hermawan orangnya semangat terus dan baik",  
                "pesan":"Bang Hermawan hobinya unik, tapi dari momen bengong bisa muncul hal-hal hebat. Semangat terus bang mengejar cita-citanya."
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Muara Piluh, Bakauheni",
                "alamat": "Jati Agung",
                "hobbi": "Ngeberantakin Kamar",
                "sosmed": "@Khusnun_nisa335",
                "kesan": "Kak Khusnun Baik dan menyenangkan",  
                "pesan":"Semangat menjalani harinya kak dan Semoga sukses selalu dalam semua usaha dan harapan."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

elif menu == "Departemen SSD":
    def SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yrnt_tgbIw4KQg2OG44thhgtOQuwCee7",
            "https://drive.google.com/uc?export=view&id=1y_g06G2kOWwvNNNxb4iOzwUF8F9xjlrd",
            "https://drive.google.com/uc?export=view&id=1yp70_uIzyh_pTYavWKXOYiNSShFcE9cb",
            "https://drive.google.com/uc?export=view&id=1yYY-25a59iU5uXuS605r0fktOSzEQpxS",
            "https://drive.google.com/uc?export=view&id=1ySzY4K5h3UyBxG-dlL2eh3DmTV4EfS3q",
            "https://drive.google.com/uc?export=view&id=1yV_RH1iJ4-SYP9WcEq_05VetczzJ1Pmt",
            "https://drive.google.com/uc?export=view&id=1yh5IIkqecj0smO8FfjJEJ8a73jAFyNfx",
            "https://drive.google.com/uc?export=view&id=1z3e2rSg1lLRPd7Z9frBG4CRmjj_sFyv2",
            "https://drive.google.com/uc?export=view&id=1z-0gSFvMR7K0qSX9B3eNHHUkKXycwQIc",
            "https://drive.google.com/uc?export=view&id=1yqLQS6CmQU3TjXfpjBVlV9wocvrQyZ8g",
            "https://drive.google.com/uc?export=view&id=1z0FKC04bZJPnbjZYHvhNgG7AsKr_sMch",
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
                "kesan": "Bang Adrian seru dan banyak pengalamannya",  
                "pesan":"Semangat terus bang mengejar mimpinya dan nyari hobinya"
            },
            {
                "nama": "Adisty Syawalda Ariyanto ",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "sukarame",
                "hobbi": "nonton film",
                "sosmed": "@Adistysa_",
                "kesan": "Kakak Adisty asik dan seru",  
                "pesan":"Selalu semangat kuliahnya dan nonton filmnya kak"
            },        
            {
                "nama": "Nabila Azhari ",
                "nim": "121450029",
                "umur": "20",
                "asal":"Simalumun",
                "alamat": "Airan",
                "hobbi": "menghitung duit",
                "sosmed": "@zajung_",
                "kesan": "Kak Nabila asik dan hobinya unik ngitungin duit",  
                "pesan":"Semangat terus kuliahnya kak dan semoga hobinya ngitung duit bisa membawa rezeki berlimpah"
            },  
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"bukit tinggi",
                "alamat": "airan",
                "hobbi": "badminton",
                "sosmed": "@ahmad.riz45",
                "kesan": "Bang Ahmad keren dan cool",  
                "pesan":"Semangat terus mengejar cita-cita dan main badminnya bang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan",
                "sosmed": "@dananghk_",
                "kesan": "Bang Danang orangnya asik dan suka banget jalan-jalan,",  
                "pesan":"Semangat menjalani harinya bnag dan jalan-jalannya bang"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Jl.lapas",
                "hobbi": "Supporteran",
                "sosmed": "@farrel__julio",
                "kesan": "Bang Farrel orangnya seru dan selalu penuh semangat",  
                "pesan":"Semangat terus bang dalam setiap kegiatan. Semoga sukses dalam mengejar mimpinya"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kak Tessa orangnya kalem",  
                "pesan":"Semangat terus kak dalam menulis dan kuliahnya"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Bandar Lampung, kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@Nabilahanftr",
                "kesan": "Kak Nabilah orangnya asik dan hobinya yang unik",  
                "pesan":"Semangat terus Kak. Semoga sukses di perkuliahan dan segala hal yang dijalani."
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobbi": "nonton",
                "sosmed": "@Alviagnting",
                "kesan": "Kak Alvia orangnya seru",  
                "pesan":"Semangat terus Kak, dalam menjalani perkuliahan dan segala aktivitas. Semoga sukses selalu dan tetap jaga semangat serta kesehatan."
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Batam",
                "alamat": "Jl.Nangka sari",
                "hobbi": "Olahraga",
                "sosmed": "@dhavinrzqa13",
                "kesan": "Bang Dhafin ramah dan kalem orangnya",  
                "pesan":"Semangat terus olahraganya bang. Semoga sukses di perkuliahan dan di setiap langkah yang diambil."
            },
            { 
                "nama": "Elia Meylani Simanjuntak ",
                "nim": "122450026",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Korpri",
                "hobbi": "Nyanyi",
                "sosmed": "@Meylaniellia",
                "kesan": "Kak Elia orangnya ceria",  
                "pesan":"Semangat terus nyanyi dan kuliahnya kak semoga sukses mengejar semua impiannya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    SSD()