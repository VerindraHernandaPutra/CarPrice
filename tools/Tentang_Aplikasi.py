import streamlit as st
import pandas as pd

# Ambil Dataset hasil modifikasi
dataset = pd.read_csv("Dataset_Final/cardata_modified.csv")

def main():
    st.image("Asset/Car.jpg", caption="Gambar Car")

    st.title('📟 Tentang Aplikasi')
    st.write("Merupakan aplikasi sederhana yang dirancang menggunakan STREAMLIT dan dibangun secara hati-hati menggunakan keenam Indra pencipta.")
    st.write("\nAplikasi dirancang untuk bisa memprediksi seakurat mungkin harga jual dari sebuah mobil berdasarkan data-data yang diberikan pengguna.")

    st.title('📊 Tentang Dataset')
    st.write("Berisi detail mobil dan berbagai fiturnya. Saya selalu tertarik dengan mobil dan ingin mengetahui faktor-faktor yang mempengaruhi harga. Jadi memutuskan untuk mengumpulkan data yang mempengaruhi target.")
    
    # Tampilkan dataset
    st.dataframe(dataset)
    st.write("Total Kolom = ", dataset.shape[0])
    st.write("Total Baris = ", dataset.shape[1])

    # Fitur
    st.write("Fitur = ")
    st.write("- **Car_Age**: Umur mobil.")
    st.write("- **Harga_Sekarang**: Harga mboil sekarang.")
    st.write("- **Harga_Original**: Harga awal mobil.")
    st.write("- **Kms Driven**: Total KM yang ditempuh mobil.")
    st.write("- **Fuel Type**: Jenis bensin mobil.")
    st.write("- **Seller_Type**: Jenis Penjual.")
    st.write("- **Transmission**: Jenis Transmisi mobil.")
    st.write("- **Mobil Bekas*: Mobil Bekas atau bukan.")

if __name__ == "__main__":
    main()
    