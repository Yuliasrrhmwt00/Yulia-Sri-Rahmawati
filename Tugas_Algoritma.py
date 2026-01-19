print ("Hello World")
import pandas as pd

# 1. Membaca dataset
try:
    df = pd.read_csv('data_kelompok.csv')
    print("Dataset Berhasil Dimuat!")
except:
    print("File CSV tidak ditemukan. Pastikan namanya benar.")

# 2. Menampilkan Data (Sesuai syarat minimal 50 data)
print("\n--- Tampilan 5 Data Pertama ---")
print(df.head())

# 3. Fitur Input Data (Numerik & Teks)
print("\n--- Tambah Data Baru ---")
nama_baru = input("Masukkan Nama Mahasiswa: ")
nilai_baru = int(input("Masukkan Nilai (Angka): "))

# Memasukkan ke tabel
data_baru = pd.DataFrame({'ID': [len(df)+1], 'Nama': [nama_baru], 'Nilai': [nilai_baru]})
df = pd.concat([df, data_baru], ignore_index=True)

# 4. Fitur Pengurutan (Sorting)
print("\n--- Data Diurutkan Berdasarkan Nilai Tertinggi ---")
df_sorted = df.sort_values(by='Nilai', ascending=False)
print(df_sorted)