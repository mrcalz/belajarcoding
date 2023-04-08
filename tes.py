import streamlit as st

st.title('Aplikasi Perkalian')
st.subheader('Ini adalah aplikasi untuk perkalian bilangan')

number1 = st.number_input('Masukan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

number2 = st.number_input('Masukan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('Silahkan tekan tombol hitung')
    