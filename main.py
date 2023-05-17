import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import numpy as np
with st.sidebar:
  selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Project", "Materi", "About Us"],
    icons=["house", "book", "lamp", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
      "nav-link": {
        "font-size": "15px",
        "text-align": "left",
        "margin": "0px",
        "--hover-color": "#eee",
      },
      "nav-link-selected": {
        "background-color": "blue"
      },
    },
  )



if selected == "Home":
    st.title("WELCOME TO OUR WEB-APPS :)")
    st.write("web apps ini adalah bagian dari tugas project mata kuliah LPK oleh kelompok 7")
    st.write("Happy Using!")
    
if selected == "Materi":
    st.title("MATERI TERKAIT NORMALITAS DAN KADAR")
    st.write(":green[NORMALITAS]")
    st.write("Normalitas adalah ukuran yang menunjukkan konsentrasi dengan berat setara dalam gram per liter larutan, dimana berat setara itu sendiri adalah ukuran kapasitas reaktif dari suatu molekul yang terlarut dalam larutan. Dalam reaksi, peran zat terlarut tersebut adalah akan menentukan normalitas suatu larutan. Normalitas juga dikenal dengan sebagai satuan konsentrasi larutan yang setara.")
    st.write("Normalitas dapat disingkat dengan huruf “N” yang merupakan salah satu cara efektif dan berguna dalam proses laboratorium. Secara umum, normalitas hamper sama dengan molaritas atau M. Jika molaritas merupakan satuan konsentrasi yang mewakili konsentrasi ion terlarut ataupun senyawa terlarut dalam suatu larutan, normalitas memiliki fungsi yang lebih lengkap dimana normalitas mewakili konsentrasi molar hanya dari komponen asam atau komponen basa saja. Komponen asam pada umumnya merupakan jumlah ion H+ yang berada dalam larutan asam, sedangkan komponen basa adalah ion terlarut OH– dalam larutan basa.")
    image = Image.open('rumus normalitas.PNG')

    st.image(image, caption='rumus normalitas')
    
    st.write(":green[KADAR]")
    st.write("Kadar suatu zat dapat dinyatakan dalam persen massa, persen volume, ppm, molaritas, molalitas, dan fraksi mol. Hubungan untuk mencari rumus kadar zat dalam campuran dapat dituliskan sebagai berikut")
    
    st.write("Pada rumus perhitungan kadar, ada faktor pengali dan pengencer yang bisa ikut berperan. Penggunaan faktor pengali atau pengencer ini menentukan kembali pada rumus yang kita gunakan")
    image = Image.open('rumus kadar dengan fp.PNG')

    st.image(image, caption='rumus kadar dengan FP')
    
    image = Image.open('rumus kadar tanpa fp.PNG')

    st.image(image, caption='rumus kadar tanpa FP')
             
    st.write(":green[EXTRA MATERI ASIDIMETRI DAN PENETAPAN KADAR NAOH DAN NA2CO3 DALAM CAMPURAN SECARA WARDER]")
    st.write("Asidimetri merupakan titrasi terhadap larutan basa bebas atau larutan garam terhidrolisis (yang berasal dari asam lemah) dengan larutan standar asam kuat. Konsep reaksi asam-basa yang terjadi merupakan reaksi (Arrhenius), suatu zat disebut asam bila zat itu dilarutkan dalam air menghasilkan ion H+ dan suatu zat disebut basa bila zat itu dilarutkan dalam air menghasilkan OH-. Larutan standar adalah larutan yang konsentrasinya diketahui untuk mentitrasi atau ditritrasi. Larutan standar memiliki peran penting dalam ketelitian titrasi karena konsentrasi larutan standar dilibatkan dalam perhitungan kadar atau konsentrasi zat yang sedang dianalisis. Untuk standarisasi suatu larutan diperlukan zat standar atau baku primer.")
    st.write("Karbonat dan Natrium Hidroksida dalam sampel campuran dapat ditentukan kadar masing-masing dengan titrasi asam-basa menggunakan larutan standar HCl dengan 2 indikator (PP dan SM). Pada titrasi tahap 1, digunakan indikator PP, HCl akan bereaksi terlebih dahulu dengan NaOH menurut reaksi sebagai berikut :")
    st.write("HCl + NaOH -> NaCl + H2O")
    st.write("dilanjutkan dengan reaksi ion karbonat dengan HCl pada tahap 1, ini menjadi hidrogen karbonat. Kemudian titrasi berlanjut ke tahap 2, ditambahkan indikator SM, HCl bereaksi dengan ion hidrogen karbonat dengan reaksi sebagai berikut :")
    st.write("Na2CO3 + HCl -> NaHCO3 + NaCl")
    st.write("NaHCO3 + HCl -> NaCl + H2CO3")       

    image = Image.open('rumus kadar Na2CO3.PNG')

    st.image(image, caption='rumus kadar Na2CO3')  
    
    
    image = Image.open('rumus kadar NaOH.PNG')

    st.image(image, caption='rumus kadar NaOH')    
    
    
if selected == 'About Us':
    st.write("Web apps ini dibuat oleh : kelompok 7")
    st.write("Aisya Ayu Dewani (2219028)")
    st.write("Ezra Artha Sasta (2219042)")
    st.write('Margaretha (2219105)')
    st.write('Naura Fildzah K A (2219128)')
    
    
    
if selected == 'Project' :
    st.title("APLIKASI PERHITUNGAN NORMALITAS dan KADAR LARUTAN")

    #NORMALITAS
    st.write(":blue[PERHITUNGAN NORMALITAS LARUTAN]")
       

    mg = st.number_input('Masukkan bobot zat terlarut (mg)')
    FP = st.number_input('Masukkan nilai FP')
    mLlarutan = st.number_input('Masukkan volume titran   (mL)')
    BE = st.number_input('masukkan nilai BE')

    tombol = st.button('Hitung nilai normalitas')

    if tombol:
        nilai_normalitas = mg/(FP*mLlarutan*BE)
        st.success(f'nilai normalitas adalah {nilai_normalitas}')

    #KADAR DENGAN FP
    st.write(":blue[PERHITUNGAN KADAR LARUTAN DENGAN FP]")

    volumetitran = st.number_input('Masukkan volume titran (mL)')
    normalitastitran = st.number_input('Masukkan normalitas titran')
    BEkadar = st.number_input('Masukkan nilai BE    ')
    volumetitrat = st.number_input('Masukkan volume titrat (mL)')
    FPkadar = st.number_input('Masukkan nilai FP   ')

    tombol = st.button('Hitung nilai kadar (%)')

    if tombol:
        nilai_kadar = (volumetitran*normalitastitran*BEkadar*FPkadar*0.1)/volumetitrat
        st.success(f'nilai kadar(%) adalah {nilai_kadar}%')
    
    #KADAR TANPA FP
    st.write(":blue[PERHITUNGAN KADAR LARUTAN TANPA FP]")

    xvolumetitran = st.number_input('Masukkan volume titran (mL) ')
    xnormalitastitran = st.number_input('Masukkan normalitas titran ')
    xBEkadar = st.number_input('Masukkan nilai BE   ')
    xvolumetitrat = st.number_input('Masukkan volume titrat (mL) ')

    tombol = st.button('Hitung nilai kadar  (%)')

    if tombol:
        nilai_kadar = (xvolumetitran*xnormalitastitran*xBEkadar*0.1)/xvolumetitrat
        st.success(f'nilai kadar(%) adalah {nilai_kadar}%')
    
    #KADAR Na2CO3
    st.write(":blue[PERHITUNGAN KADAR Na2CO3 dalam CAMPURAN SECARA ASIDIMETRI]")

    volHCLa = st.number_input('Masukkan volume HCL (a) (mL)')
    volHCLb = st.number_input('Masukkan volume HCL (b) (mL)')
    normalitasHCL = st.number_input('Masukkan normalitas HCL')
    BENa2CO3 = st.number_input('Masukkan nilai BE Na2CO3')
    volumecontoh = st.number_input('Masukkan volume contoh (mL)')

    tombol = st.button('Hitung nilai kadar Na2CO3 (%)')

    if tombol:
        nilai_kadar_Na2CO3 = (2*(volHCLb-volHCLa))*normalitasHCL*BENa2CO3*0.1/volumecontoh
        st.success(f'nilai kadar(%) adalah {nilai_kadar_Na2CO3}%')

    #KADAR NaOH
    st.write(":blue[PERHITUNGAN KADAR NaOH dalam CAMPURAN SECARA ASIDIMETRI]")

    XvolHCLa = st.number_input('Masukkan volume HCL (a)  (mL)')
    XvolHCLb = st.number_input('Masukkan volume HCL (b)  (mL)')
    XnormalitasHCL = st.number_input('Masukkan  normalitas HCL')
    BENaOH = st.number_input('Masukkan nilai BE NaOH')
    Xvolumecontoh = st.number_input('Masukkan  volume contoh (mL)')

    tombol = st.button('Hitung nilai kadar NaOH (%)')

    if tombol:
        nilai_kadar_NaOH = (2*XvolHCLa-XvolHCLb)*XnormalitasHCL*BENaOH*0.1/Xvolumecontoh
        st.success(f'nilai kadar(%) adalah {nilai_kadar_NaOH}%')