print("=== Alat hitung luas bangun datar ===")
print(" pilih 1 untuk menghitung luas persegi")
print(" pilih 2 untuk menghitung luas lingkaran")
print(" pilih 3 untuk menghitung luas segitiga")

pilihan = int(input("Masukkan pilihan 1/2/3: "))

match pilihan:
    case 1:
        s = int(input("Masukkan panjang persegi: "))
        luas = s * s
        print(f"Luas persegi adalah {luas}")
    case 2:
        r = int(input("Masukkan jari-jari lingkaran: "))
        pi = 3.14
        luas = pi * r * r
        print(f"Luas lingkaran adalah {luas}")
    case 3:
        a = int(input("Masukkan alas segitiga: "))
        t = int(input("Masukkan tinggi segitiga: "))
        luas = a * t / 2
        print(f"Luas segitiga adalah {luas}")
    case _:
        print("Masukkan pilihan dengan benar")