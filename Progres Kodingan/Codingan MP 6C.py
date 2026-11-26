judul1 = "Analisis Nutrisi dan Rekomendasi "
judul2 = "Menu Makanan Starbucks Berdasarkan Kalori"
kelompok = "Kelompok 6C"
asisten = "Intan Permata Mustika"
dosen = "Dr. Asmuliardi Muluk, S.T., M.T."
tahun = "2026"

LEBAR = 90  # lebar kertas 

def baris(teks=""):
    # mencetak 1 baris di tengah, dengan garis | di kiri dan kanan
    print("|" + teks.center(LEBAR) + "|")

print("+" + "-" * LEBAR + "+")   # garis atas

baris()
baris()
baris()
baris("MINI PROJECT")
baris()
baris("PEMROGRAMAN KOMPUTER")
baris()
baris("(" + judul1)
baris(judul2 + ")")
baris()
baris()

baris("Oleh :")
baris()
baris(kelompok)
baris()
baris()

baris("Anggota :")
baris()
baris("Rakha Zikra SYafdan      2610931019")
baris("Wan Aulia Ramadhani      2610933008")
baris("Rayyan Jeva              2610933020")
baris("Queena Shareefa Yandri   2610937002")
baris()
baris()
baris()

baris("Asisten Pembimbing :")
baris()
baris(asisten)
baris()
baris()
baris()

baris("Dosen Pengampu :")
baris()
baris(dosen)
baris()
baris()
baris()
baris()

baris("LABORATORIUM SISTEM INFORMASI DAN KEPUTUSAN")
baris()
baris("DEPARTEMEN TEKNIK INDUSTRI")
baris()
baris("FAKULTAS TEKNIK")
baris()
baris("UNIVERSITAS ANDALAS")
baris()
baris(tahun)
baris()
baris()
baris()

print("+" + "-" * LEBAR + "+")   # garis bawah
import csv
import statistics

FILE = "starbucks.csv"
KOLOM = ["item", "calories", "fat", "carb", "fiber", "protein", "type"]
ANGKA = ["calories", "fat", "carb", "fiber", "protein"]
TOPPING = {"mentega": 102, "selai": 56, "cream cheese": 51}

def validasi_data(baris):
    for k in KOLOM:
        if k not in baris:
            return False
    if baris["item"] is None or baris["item"].strip() == "":
        return False
    try:
        for k in ANGKA:
            if float(baris[k]) < 0:
                return False
    except (ValueError, TypeError):
        return False
    return True

def baca_csv():
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
        print("Error: File CSV tidak ditemukan.")
        return menu
    if len(menu) > 0:
        print("Data dimuat:", len(menu), "menu,", ditolak, "ditolak.")
    return menu

def tampilkan_menu(menu):
    print("\n=== DAFTAR MENU STARBUCKS ===")
    for nomor, m in enumerate(menu, start=1):
        print(f"{nomor}. {m['item']}")

def pilih_menu(menu):
    try:
        nomor = int(input("Masukkan nomor menu: "))
        if 1 <= nomor <= len(menu):
            return menu[nomor - 1]
        else:
            print("Nomor menu tidak valid.")
            return None
    except ValueError:
        print("Input harus berupa angka.")
        return None

def kategori(kalori):
    if kalori < 220:
        return "Rendah"
    elif kalori < 360:
        return "Sedang"
    else:
        return "Tinggi"

def cari_menu(menu, kata):
    hasil = []
    for m in menu:
        if kata.lower() in m["item"].lower():
            hasil.append(m)
    return hasil

def input_topping():
    print("Topping tersedia:")

    for nama in TOPPING:
        print(f"- {nama} (+{TOPPING[nama]} kkal)")
    while True:
        isi = input("Topping (pisahkan koma, kosongkan jika tanpa topping): ").lower().split(",")
        tambahan = 0
        benar = True
        for t in isi:
            t = t.strip()
            if t == "":
                continue
            if t in TOPPING:
                tambahan += TOPPING[t]
            else:
                print("Topping salah:", t)
                benar = False
        if benar:
            break
    return tambahan

def cari_dan_tampilkan_menu(menu):
    kata = input("Kata kunci menu: ")
    hasil = cari_menu(menu, kata)

    if kata.strip() == "" or len(hasil) == 0:
        print("Data tidak ditemukan.")
    else:
        print(f"{'Nama Menu':<45}{'Kalori':<8}" f"{'Lemak':<7}{'Karbo':<7}{'Serat':<7}{'Protein'}")

        for m in hasil:
            print(f"{m['item']:<45}" f"{m['calories']:<8g}" f"{m['fat']:<7g}" f"{m['carb']:<7g}" f"{m['fiber']:<7g}" f"{m['protein']:g}")

def statistik(menu):
    print("Jumlah menu:", len(menu))
    print(f"{'Atribut':<10}{'Rata-rata':<12}{'Maks':<8}{'Min'}")

    for k in ANGKA:
        nilai = []
        for m in menu:
            nilai.append(m[k])
        print(f"{k:<10}" f"{statistics.mean(nilai):<12.1f}" f"{max(nilai):<8g}" f"{min(nilai):g}")

def bandingkan_menu_a_b(menu):
    print("\n=== MEMBANDINGKAN MENU ===")
    print("Menu A")
    a = pilih_menu(menu)
    if a is None:
        return
    print("\nMenu B")
    b = pilih_menu(menu)
    if b is None:
        return

    print("\n=== HASIL PERBANDINGAN ===")
    print(f"{'Atribut':<10}{a['item'][:20]:<22}{b['item'][:20]:<22}{'Selisih'}")

    for k in ANGKA:
        selisih = abs(a[k] - b[k])
        print(f"{k:<10}"
            f"{a[k]:<22g}"
            f"{b[k]:<22g}"
            f"{selisih:g}")

def klasifikasi_kalori(menu):
    for kat in ["Rendah", "Sedang", "Tinggi"]:
        print("\n=== KATEGORI", kat.upper(), "===")

        jumlah = 0
        for m in menu:
            if kategori(m["calories"]) == kat:
                print(f"- {m['item']} ({m['calories']:g} kkal)")
                jumlah += 1
        if jumlah == 0:
            print("Tidak ada menu.")

def rekomendasi_menu(menu):
    try:
        target = float(input("Target kalori maksimal: "))
        tambahan = input_topping()
        jumlah = 0
        for m in menu:
            total = m["calories"] + tambahan
            if total <= target:
                print(f"{m['item']:<45}" f"{total:g} kkal  {kategori(total)}")
                jumlah += 1
        if jumlah == 0:
            print("Tidak ada menu yang sesuai target.")
    except ValueError:
        print("Target kalori harus berupa angka.")

def hitung_total_kalori(menu):
    print("\n=== HITUNG TOTAL KALORI ===")
    m = pilih_menu(menu)
    if m is None:
        return
    tambahan = input_topping()
    total = m["calories"] + tambahan

    print(m["item"], ":", f"{m['calories']:g} + {tambahan} = {total:g} kkal")
    print("Kategori:", kategori(total))

def main():
    print("=== MINI PROJECT PEMROGRAMAN KOMPUTER - KELOMPOK 6C ===")
    menu = baca_csv()
    if len(menu) == 0:
        print("Error: Tidak ada data menu yang valid.")
    else:
        tampilkan_menu(menu)
        while True:
            print("\n=== MENU UTAMA ===")
            print("1. Cari menu")
            print("2. Statistik nutrisi (rata-rata, maks, min)")
            print("3. Bandingkan dua menu")
            print("4. Klasifikasi kalori")
            print("5. Rekomendasi menu berdasarkan target kalori")
            print("6. Hitung total kalori + topping")
            print("0. Keluar")

            pilihan = input("Pilihan: ")
            if pilihan == "0":
                print("Terima kasih")
                break
            elif pilihan == "1":
                cari_dan_tampilkan_menu(menu)
            elif pilihan == "2":
                statistik(menu)
            elif pilihan == "3":
                bandingkan_menu_a_b(menu)
            elif pilihan == "4":
                klasifikasi_kalori(menu)
            elif pilihan == "5":
                rekomendasi_menu(menu)
            elif pilihan == "6":
                hitung_total_kalori(menu)
            else:
                print("Pilihan tidak valid.")
main()