import streamlit as st

# Fungsi untuk mengatasi input kosong
def handle_empty_input(input_value):
  try:
    return float(input_value) if input_value else 0
  except ValueError:
    st.error("Masukkan harus berupa angka.")
    return 0

# Fungsi Untuk Memilih Fuel_Type
def pilih_Fuel_Type(Fuel_Type):
    if Fuel_Type == "Petrol":
        Fuel_Type = 2
    elif Fuel_Type == "Diesel":
        Fuel_Type = 1
    elif Fuel_Type == "CNG":
        Fuel_Type = 0
    
    # Handle Empty Value
    Fuel_Type = handle_empty_input(Fuel_Type)

    return Fuel_Type

# Fungsi Untuk Memilih Seller_Type
def pilih_Seller_Type(Seller_Type):
    if Seller_Type == "Dealer":
        Seller_Type = 0
    elif Seller_Type == "Individual":
        Seller_Type = 1

    # Handle Empty Value
    Seller_Type = handle_empty_input(Seller_Type)
        
    return Seller_Type

# Fungsi Untuk Memilih Transmission
def pilih_Transmission(Transmission):
    if Transmission == "Manual":
        Transmission = 1
    elif Transmission == "Automatic":
        Transmission = 0

    # Handle Empty Value
    Transmission = handle_empty_input(Transmission)
        
    return Transmission

# Fungsi Untuk Memilih Mobil_Bekas
def pilih_Mobil_Bekas(Mobil_Bekas):
    if Mobil_Bekas == "No":
        Mobil_Bekas = 0
    elif Mobil_Bekas == "Yes":
        Mobil_Bekas = 1

    # Handle Empty Value
    Mobil_Bekas = handle_empty_input(Mobil_Bekas)
        
    return Mobil_Bekas
