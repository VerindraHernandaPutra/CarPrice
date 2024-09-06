import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ambil Dataset hasil modifikasi
dataset_ori = pd.read_csv("Dataset/cardata.csv")
dataset_mod = pd.read_csv("Dataset_Final/cardata_modified.csv")

def distribusi_harga_sekarang():

    # Data Age
    price_ori = dataset_ori['Selling_Price']

    # Data Age
    price_mod = dataset_mod['Harga_Sekarang']

    # Buat 2 kolom
    col1, col2 = st.columns(2)

    # Histogram 1
    with col1:
        fig, ax = plt.subplots()
        ax.hist(price_ori, bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel('Harga Jual')
        ax.set_ylabel('Frekuensi')
        ax.set_title('Distribusi Harga Jual - Dataset Original')
        st.pyplot(fig)

    # Histogram 2
    with col2:
        fig, ax = plt.subplots()
        ax.hist(price_mod, bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel('Harga Jual')
        ax.set_ylabel('Frekuensi')
        ax.set_title('Distribusi Harga Jual - Dataset Modified')
        st.pyplot(fig)

def main():
    st.title("Modified Dataset")
    st.dataframe(dataset_mod)
    st.write("Disini telah dilakukan beberapa modifikasi untuk meningkatkan akurasi aplikasi, salah satunya adalah pada kolom Age. Dimana saya melakukan min-max scaling untuk memudahkan model dalam memprediksi model")

    st.title("Visualisasi")

    # Histogram distribusi Age
    st.header("Distribusi Harga Jual Mobil")
    distribusi_harga_sekarang()

    # Distribusi Harga Jual Mobil berdasarkan Jenis Fuel
    st.header("Distribusi Harga Jual Mobil berdasarkan Jenis Fuel")
    st.bar_chart(dataset_ori, x="Fuel_Type", y="Selling_Price", stack=False)

    st.write("\nTo be Continued...")

if __name__ == "__main__":
    main()
    