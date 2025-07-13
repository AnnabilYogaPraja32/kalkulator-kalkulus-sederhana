import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Setup halaman Streamlit
st.set_page_config(page_title="Kalkulator Integral & Turunan", layout="centered")
st.title("🧮 Kalkulator Integral & Turunan")

# Input fungsi dari pengguna
fungsi_input = st.text_input("Masukkan fungsi aljabar (misal: x**2 + 3*x - 5):", value="x**2")

# Pilihan operasi
operasi = st.radio("Pilih operasi:", ("Turunan", "Integral"))

# Inisialisasi simbol x
x = sp.Symbol('x')

try:
    # Konversi string ke ekspresi simbolik
    fungsi = sp.sympify(fungsi_input)

    if operasi == "Turunan":
        hasil = sp.diff(fungsi, x)
        st.subheader("Hasil Turunan")
    else:
        hasil = sp.integrate(fungsi, x)
        st.subheader("Hasil Integral")

    # Tampilkan hasil simbolik
    st.latex(sp.latex(hasil))

    # Hitung hasil numerik pada titik tertentu (opsional)
    titik = st.number_input("Masukkan nilai x untuk evaluasi numerik:", value=1.0)
    hasil_numerik = hasil.evalf(subs={x: titik})
    st.write(f"Hasil evaluasi pada x = {titik} adalah: {hasil_numerik}")

    # Gambar grafik
    st.subheader("Grafik")
    x_vals = np.linspace(-10, 10, 400)
    f_lambdified = sp.lambdify(x, fungsi, modules=['numpy'])
    h_lambdified = sp.lambdify(x, hasil, modules=['numpy'])

    fig, ax = plt.subplots()
    ax.plot(x_vals, f_lambdified(x_vals), label="Fungsi Awal")
    ax.plot(x_vals, h_lambdified(x_vals), label=f"Hasil {operasi}", linestyle='--')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
