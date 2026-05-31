import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = "🔥"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.image("ChatGPT Image May 31, 2026, 01_33_08 PM.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan bangun datar", ["Persegi",  "Persegi panjang", "Segitiga", "Lingkaran", "Trapesium"])
    st.caption("Dibuat dengan 💖 oleh **Hendrawan Tetes Winetyo**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")
        sisi = st.number_input("Masukkan panjanga sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi* sisi
            keliling = 4 * sisi
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
    case "Persegi panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukkan panjang")
        lebar = st.number_input("Masukkan lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` dan `keliling` segitiga")
        alas = st.number_input("Masukkan alas")
        tinggi = st.number_input("Masukkan tinggi")
        sisi1 = st.number_input("Masukkan panjang sisi 1")
        sisi2 = st.number_input("Masukkan panjang sisi 2")
        sisi3 = st.number_input("Masukkan panjang sisi 3")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")
        jari_jari = st.number_input("Masukkan jari-jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jari_jari ** 2
            keliling = 2 * 3.14 * jari_jari
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
    case "Trapesium":
        st.title("Trapesium")
        st.markdown("Menghitung `luas` dan `keliling` trapesium")
        alas1 = st.number_input("Masukkan panjang alas 1")
        alas2 = st.number_input("Masukkan panjang alas 2")
        tinggi = st.number_input("Masukkan tinggi")
        sisi1 = st.number_input("Masukkan panjang sisi 1")
        sisi2 = st.number_input("Masukkan panjang sisi 2")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * (alas1 + alas2) * tinggi
            keliling = alas1 + alas2 + sisi1 + sisi2
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
    case _ :
        st.error("Terjadi kesalahan")
