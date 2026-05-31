# ==========================================
# PROGRAM CEK INTEGRITAS FILE
# Menggunakan MD5 dan SHA-256
# ==========================================

import hashlib

# Fungsi menghitung hash MD5
def hitung_md5(nama_file):
    md5 = hashlib.md5()

    with open(nama_file, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            md5.update(data)

    return md5.hexdigest()


# Fungsi menghitung hash SHA-256
def hitung_sha256(nama_file):
    sha256 = hashlib.sha256()

    with open(nama_file, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


# Fungsi membandingkan dua file
def bandingkan_file(file1, file2):

    md5_file1 = hitung_md5(file1)
    md5_file2 = hitung_md5(file2)

    sha_file1 = hitung_sha256(file1)
    sha_file2 = hitung_sha256(file2)

    print("\n===================================")
    print("HASIL HASH FILE")
    print("===================================")

    print(f"\nFile 1 : {file1}")
    print("MD5     :", md5_file1)
    print("SHA-256 :", sha_file1)

    print(f"\nFile 2 : {file2}")
    print("MD5     :", md5_file2)
    print("SHA-256 :", sha_file2)

    print("\n===================================")
    print("HASIL PERBANDINGAN")
    print("===================================")

    if md5_file1 == md5_file2:
        print("MD5     : Sama")
    else:
        print("MD5     : Berbeda")

    if sha_file1 == sha_file2:
        print("SHA-256 : Sama")
    else:
        print("SHA-256 : Berbeda")

    if md5_file1 == md5_file2 and sha_file1 == sha_file2:
        print("\nKESIMPULAN:")
        print("File tidak berubah")
        print("Integritas file TERJAGA")
    else:
        print("\nKESIMPULAN:")
        print("File telah berubah")
        print("Integritas file TIDAK TERJAGA")


# Program utama
print("===================================")
print("PROGRAM CEK INTEGRITAS FILE")
print("MD5 DAN SHA-256")
print("===================================")

file_asli = input("\nMasukkan nama file asli : ")
file_modifikasi = input("Masukkan nama file modifikasi : ")

bandingkan_file(file_asli, file_modifikasi)