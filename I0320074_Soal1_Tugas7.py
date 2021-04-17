import random
def program():
    judul = "PROGRAM PEMILIHAN KODE SOAL AEB"
    print(judul.center(70,'-'))
    list = ["Kode A MTS","KodeB MTS","Kode C MTS","Kode D MTS"]
    print("Berikut daftar kode soal tugas besar Analisis dan Estimasi Biaya:")
    print(list)
    kode = random.choice(list)
    a = input("Masukkan Nama anda:")
    nama = x.upper()
    b = input("Masukkan NIM anda:")
    nim = b.capitalize()
    print("")
    print("kode soal AEB atas nama ", nama,"dengan NIM", nim,"adalah", kode.upper())
program()
