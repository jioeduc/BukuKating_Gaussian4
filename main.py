import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/063_Arya Muda Siregar.py",
    title="063 - Arya Muda Siregar",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/072_Fathinah Nur Azizah.py",
    title="072 - Fathinah Nur Azizah",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/002_Afifah Fauziah.py",
    title="002 - Afifah Fauziah",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/020_Try Yani Rizki Nur Rohmah.py",
    title="117 - Anwar Muslim",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/026_Zahra Putri Salsabilla.py",
    title="026 - Zahra Putri Salsabilla",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/034_Kharisma Mustika Sari.py",
    title="034 - Kharisma Mustika Sari",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/036_Rosalia Siregar.py",
    title="036 - Rosalia Siregar",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/047_Benget Sidabutar.py",
    title="047 - Benget Sidabutar",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/065_Giofani Aristyo.py",
    title="065 - Giofani Aristyo",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/076_Iqfina Haula Halika.py",
    title="076 - Iqfina Haula Halika",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/088_Ali Aristo Muthahhari Parisi.py",
    title="088 - Ali Aristo Muthahhari Parisi",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/097_Arienta Khusnul Ananda.py",
    title="097 - Arienta Khusnul Ananda",
    icon=":material/person:",
)
Mahasiswa13 = st.Page(
    "Buku Kating/122_Melinza Nabila.py",
    title="122 - Melinza Nabila",
    icon=":material/person:",
)
#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12, Mahasiswa13],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

