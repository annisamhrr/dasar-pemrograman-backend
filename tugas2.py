# Fungsi untuk menghitung gaji karyawan
def hitung_gaji(nama, golongan, jam_kerja):
    # Menentukan upah per jam berdasarkan golongan
    if golongan == 'A':
        upah_per_jam = 5000
    elif golongan == 'B':
        upah_per_jam = 7000
    elif golongan == 'C':
        upah_per_jam = 8000
    elif golongan == 'D':
        upah_per_jam = 10000
    else:
        print("Golongan tidak valid.")
        return
    
    # Menghitung gaji pokok
    gaji_pokok = jam_kerja * upah_per_jam
    
    # Menghitung uang lembur jika jam kerja lebih dari 48 jam
    if jam_kerja > 48:
        jam_lembur = jam_kerja - 48
        uang_lembur = jam_lembur * 4000
    else:
        uang_lembur = 0

    # Total gaji adalah gaji pokok ditambah uang lembur
    total_gaji = gaji_pokok + uang_lembur

    # Menampilkan hasil perhitungan
    print(f"Nama Karyawan: {nama}")
    print(f"Golongan: {golongan}")
    print(f"Jumlah jam kerja: {jam_kerja}")
    print(f"{nama} menerima upah Rp. {total_gaji} per minggu")

# Input data karyawan
nama = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan (A/B/C/D): ")
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

# Memanggil fungsi hitung_gaji
hitung_gaji(nama, golongan, jam_kerja)
