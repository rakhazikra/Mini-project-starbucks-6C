import csv


FILE = "starbucks.csv"
KOLOM = ["item", "calories", "fat", "carb", "fiber", "protein", "type"]
ANGKA = ["calories", "fat", "carb", "fiber", "protein"]
TOPPING = {"mentega": 102, "selai": 56, "cream cheese": 51}

def validasi_data(baris):
    for k in KOLOM:
        if k not in baris:
            return False
    if baris["item"] == None or baris["item"].strip() == "":
        return False
    try:
        for k in ANGKA:
            if float(baris[k]) < 0:
                return False
    except ValueError:
        return False
    except TypeError:
        return False
    return True


def baca_file_csv():
    menu = []
    ditolak = 0
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            data = csv.DictReader(file)
            for baris in data:
                if validasi_data(baris):
                    m = {"item": baris["item"].strip(), "type": baris["type"].strip()}
                    for k in ANGKA:
                        m[k] = float(baris[k])
                    menu.append(m)
                else:
                    ditolak += 1
    except FileNotFoundError:
        pass
    if len(menu) > 0:
        print("Data dimuat:", len(menu), "menu,", ditolak, "ditolak.")
    return menu

def hilangkan_nol_desimal(angka):
    if angka == int(angka):
        return int(angka)
    return angka


def cari_menu(menu, kata):
    hasil = []
    for m in menu:
        if kata.lower() in m["item"].lower():
            hasil.append(m)
    return hasil


def tampilkan_tabel_menu(daftar):
    print(f"{'Nama Menu':<56}{'Kalori':<8}{'Lemak':<7}{'Karbo':<7}{'Serat':<7}{'Protein'}")
    for m in daftar:
        print(f"{m['item']:<56}{hilangkan_nol_desimal(m['calories']):<8}{hilangkan_nol_desimal(m['fat']):<7}"
              f"{hilangkan_nol_desimal(m['carb']):<7}{hilangkan_nol_desimal(m['fiber']):<7}{hilangkan_nol_desimal(m['protein'])}")

def cari_dan_tampilkan_menu(menu):
    kata = input("Kata kunci menu: ")
    hasil = cari_menu(menu, kata)
    if kata.strip() == "" or len(hasil) == 0:
        print("Data tidak ditemukan.")
    else:
        tampilkan_tabel_menu(hasil)


def tampilkan_menu_utama():
    print("\n=== MENU UTAMA ===")
    print("1. Cari menu")
    print("2. Statistik nutrisi (rata-rata, maks, min)")
    print("3. Bandingkan dua menu")
    print("4. Klasifikasi kalori & simpan CSV")
    print("5. Rekomendasi menu berdasarkan target kalori")
    print("6. Hitung total kalori + topping")
    print("0. Keluar")

def main():
    print("=== MINI PROJECT PEMROGRAMAN KOMPUTER - KELOMPOK 6C ===")
    menu = baca_file_csv()
    if len(menu) == 0:
        print("Error: file tidak ditemukan, kolom tidak lengkap, atau tidak ada data valid.")
    else:
        print("\nDAFTAR SELURUH MENU")
        tampilkan_tabel_menu(menu)
        while True:
            tampilkan_menu_utama()
            pilihan = input("Pilihan: ")
            if pilihan == "0":
                print("Terima kasih")
                break
            elif pilihan == "1":
                cari_dan_tampilkan_menu(menu)
            elif pilihan in ["2", "3", "4", "5", "6"]:
                print("Fitur belum tersedia.")
            else:
                print("Pilihan tidak valid.")


main()