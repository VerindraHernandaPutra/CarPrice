import streamlit as st
import tools.Function as function
import pickle
import numpy as np
import pandas as pd

with open("carprice.pkl", "rb") as model_file:
    model = pickle.load(model_file)

def main():
    st.sidebar.title('Input')

    # Umur Mobil
    Car_Age = st.sidebar.text_input("Rasio Uranium", placeholder="Silahkan masukkan angka..")
    Car_Age = function.handle_empty_input(Car_Age)

    # Harga Original
    Harga_Original = st.sidebar.text_input("Harga Original", placeholder="Silahkan masukkan angka..")
    Harga_Original = function.handle_empty_input(Harga_Original)

    # Kms Driven
    Kms_Driven = st.sidebar.text_input("Kms Driven", placeholder="Silahkan masukkan angka..")
    Kms_Driven = function.handle_empty_input(Kms_Driven)

    # Fuel_Type
    Fuel_Type = st.sidebar.selectbox(
        "Fuel_Type",
        ("Petrol", "Diesel", "CNG"),
        index=None,
        placeholder="Silahkan pilih..",
    )
    Fuel_Type = function.pilih_Fuel_Type(Fuel_Type)

    # Seller Type
    Seller_Type = st.sidebar.radio(
        "Pilih Seller_Type",
        options=["Dealer", "Individual"],
        index=None
    )
    Seller_Type = function.pilih_Seller_Type(Seller_Type)

    # Transmission
    Transmission = st.sidebar.radio(
        "Pilih Transmission",
        options=["Manual", "Automatic"],
        index=None
    )
    Transmission = function.pilih_Transmission(Transmission)

    # Mobil Bekas
    Mobil_Bekas = st.sidebar.radio(
        "Pilih Mobil_Bekas",
        options=["No", "Yes"],
        index=None
    )
    Mobil_Bekas = function.pilih_Mobil_Bekas(Mobil_Bekas)

    # Prediksi
    input = np.array([Car_Age, Harga_Original, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Mobil_Bekas])
    input = np.expand_dims(input, axis = 0)
    predict = model.predict(input)

    # Mengembalikan ke bentuk asli
    predict = np.exp(predict)

    # Tampilkan Input
    st.write("**Input :**")
    df = pd.DataFrame(input, columns=['Car_Age', 'Harga_Original', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Mobil Bekas'])
    st.dataframe(df)

    # Tampilkan Hasil
    if predict.any():
        st.write("**Hasil Prediksi :**")
        st.success("Hasil Prediksi Harga Mobil = {} INR".format(int(predict)))

if __name__ == "__main__":
    main()
    