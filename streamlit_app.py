import streamlit as st

st.title("paissbrigezmph")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/")
st.image("IMG-20250201-WA0030.jpg", width=200)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)
if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")      
else:
  st.write(f"{angka} adalah Bilangan Ganjil")                       
