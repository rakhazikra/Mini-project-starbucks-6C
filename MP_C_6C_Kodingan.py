judul1 = "Analisis Nutrisi dan Rekomendasi "
judul2 = "Menu Makanan Starbucks Berdasarkan Kalori"
kelompok = "Kelompok 6C"
asisten = "Intan Permata Mustika"
dosen = "Dr. Asmuliardi Muluk, S.T., M.T."
tahun = "2026"

LEBAR = 90  

def baris(teks=""):
    print("|" + teks.center(LEBAR) + "|")

print("-" * (LEBAR + 2))   
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
baris("Rakha Zikra Syafdan      2610931019")
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
print("-" * (LEBAR + 2))   

import csv
import statistics

FILE = "starbucks.csv"
KOLOM = ["item", "calories", "fat", "carb", "fiber", "protein", "type"]
ANGKA = ["calories", "fat", "carb", "fiber", "protein"]
TOPPING = {"mentega": 102, "selai": 56, "cream cheese": 51}


class MenuStarbucks:
    def __init__(self, data):
        self.item = data["item"].strip()
        self.jenis = data["type"].strip()
        self.nutrisi = {}

        for kolom in ANGKA:
            self.nutrisi[kolom] = float(data[kolom])

    def kalori(self):
        return self.nutrisi["calories"]

    def kategori_kalori(self, total=None):
        if total is None:
            total = self.kalori()

        if total < 100:
            return "Rendah"
        elif total <= 399:
            return "Sedang"
        return "Tinggi"

    def baris_tabel_nutrisi(self):
        n = self.nutrisi
        nama = self.item[:43]
        return (f" {nama:<42}| {n['calories']:>7g} | {n['fat']:>6g} | "
                f"{n['carb']:>6g} | {n['fiber']:>6g} | {n['protein']:>7g} ")


class AplikasiStarbucks:
    def __init__(self, nama_file):
        self.nama_file = nama_file
        self.menu = []

    def validasi_data(self, data):
        for kolom in KOLOM:
            if kolom not in data:
                return False

        if not data["item"] or data["item"].strip() == "":
            return False
        try:
            for kolom in ANGKA:
                if float(data[kolom]) < 0:
                    return False
        except (ValueError, TypeError):
            return False
        return True

    def baca_csv(self):
        ditolak = 0
        try:
            with open(self.nama_file, "r", encoding="utf-8-sig", newline="") as file:
                data = csv.DictReader(file)

                for baris in data:
                    if self.validasi_data(baris):
                        self.menu.append(MenuStarbucks(baris))
                    else:
                        ditolak += 1

        except FileNotFoundError:
            print("Error: File CSV tidak ditemukan.")
            print("Pastikan starbucks.csv berada di folder yang sama dengan program.")
            return False

        print(f"\nData dimuat: {len(self.menu)} menu, {ditolak} ditolak.")
        return len(self.menu) > 0

    def tampilkan_menu(self):
        print("\n" + "-" * (LEBAR + 2))
        baris("DAFTAR MENU STARBUCKS")
        print("-" * (LEBAR + 2))
        print(f"| {'No.':^4} | {'Nama Menu':<{LEBAR - 9}} |")
        print("-" * (LEBAR + 2))

        for nomor, menu in enumerate(self.menu, start=1):
            print(f"| {nomor:>4} | {menu.item[:LEBAR - 9]:<{LEBAR - 9}} |")

        print("-" * (LEBAR + 2))

    def pilih_menu(self):
        try:
            nomor = int(input("Masukkan nomor menu: "))
            if 1 <= nomor <= len(self.menu):
                return self.menu[nomor - 1]
            print("Nomor menu tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

        return None

    def cari_menu(self):
        menu = self.pilih_menu()
        if menu is None:
            return

        garis_tabel = "-" * (LEBAR + 2)
        print("\n" + garis_tabel)
        print(f"| {'DETAIL MENU STARBUCKS':^88} |")
        print(garis_tabel)
        print(f"| {'Nama Menu':<41} | {'Kalori':^7} | {'Lemak':^6} | {'Karbo':^6} | {'Serat':^6} | {'Protein':^7} |")
        print(garis_tabel)
        print("|" + menu.baris_tabel_nutrisi() + "|")
        print(garis_tabel)

    def statistik(self):
        garis_tabel = "-" * (LEBAR + 2)
        print("\n" + garis_tabel)
        print(f"| {f'STATISTIK NUTRISI (JUMLAH MENU: {len(self.menu)})':^88} |")
        print(garis_tabel)
        print(f"| {'Atribut':<21} | {'Rata-rata':^20} | {'Maks':^19} | {'Min':^19} |")
        print(garis_tabel)

        for kolom in ANGKA:
            nilai = [menu.nutrisi[kolom] for menu in self.menu]
            print(f"| {kolom:<21} | {statistics.mean(nilai):^20.1f} | "f"{max(nilai):^19g} | {min(nilai):^19g} |")
        print(garis_tabel)

    def bandingkan_menu(self):
        print("\n" + "=" * 42 + " MENU A " + "=" * 42)
        a = self.pilih_menu()
        if a is None:
            return

        print("\n" + "=" * 42 + " MENU B " + "=" * 42)
        b = self.pilih_menu()
        if b is None:
            return

        garis_tabel = "-" * (LEBAR + 2)
        print("\n" + garis_tabel)
        print(f"| {'HASIL PERBANDINGAN':^88} |")
        print(garis_tabel)
        print(f"| {'Atribut':<9} | {a.item[:18]:^18} | {b.item[:18]:^18} |"f" {'Selisih':^7} | {'Rekomendasi Menu':^24} |")
        print(garis_tabel)

        if a.kalori() < b.kalori():
            teks_rekomendasi = ["","Lebih baik pilih menu:",a.item[:24],"","",]
        elif b.kalori() < a.kalori():
            teks_rekomendasi = ["","Lebih baik pilih menu:",b.item[:24],"","",]
        else:
            teks_rekomendasi = ["","Kalori kedua menu sama,","keduanya dapat dipilih.","","",]

        for i, kolom in enumerate(ANGKA):
            nilai_a = a.nutrisi[kolom]
            nilai_b = b.nutrisi[kolom]
            selisih = abs(nilai_a - nilai_b)
            print(f"| {kolom:<9} | {nilai_a:>18g} | {nilai_b:>18g} |"f" {selisih:>7g} | {teks_rekomendasi[i]:^24} |")

        print(garis_tabel)

    def klasifikasi_kalori(self):
        garis_tabel = "-" * (LEBAR + 2)
        print("\n" + garis_tabel)
        print(f"| {'KLASIFIKASI KALORI MENU':^88} |")
        print(garis_tabel)
        print(f"| {'No.':^4} | {'Nama Menu':<49} | {'Kalori (kkal)':^13} | {'Kategori':^13} |")
        print(garis_tabel)

        for kategori in ["Rendah", "Sedang", "Tinggi"]:
            daftar_kat = [m for m in self.menu if m.kategori_kalori() == kategori]
            print(f"| {f'KATEGORI {kategori.upper()} ({len(daftar_kat)} menu)':<88} |")
            print(garis_tabel)

            if len(daftar_kat) == 0:
                print(f"| {'Tidak ada menu.':^88} |")
            else:
                for idx, menu in enumerate(daftar_kat, start=1):
                    print(f"| {idx:>4} | {menu.item[:49]:<49} | "f"{menu.kalori():^13g} | {kategori:^13} |")
            print(garis_tabel)

    def input_topping(self):
        garis_top = "-" * (LEBAR + 2)
        print("\n" + garis_top)
        print(f"| {'TOPPING TERSEDIA':<88} |")
        print(garis_top)
        print(f"| {'Nama Topping':<48} | {'Tambahan Kalori':^37} |")
        print(garis_top)
        for nama, kalori in TOPPING.items():
            print(f"| {nama:<48} | {'+' + str(kalori) + ' kkal':^37} |")
        print(garis_top)

        while True:
            isi = input("Topping (pisahkan koma, kosongkan jika tanpa topping): ").lower().split(",")

            tambahan = 0
            benar = True

            for topping in isi:
                topping = topping.strip()
                if topping == "":
                    continue

                if topping in TOPPING:
                    tambahan += TOPPING[topping]
                else:
                    print("Topping salah:", topping)
                    benar = False

            if benar:
                return tambahan

    def rekomendasi_menu(self):
        try:
            target = float(input("Target kalori maksimal: "))
            tambahan = self.input_topping()

            hasil = []
            for menu in self.menu:
                total = menu.kalori() + tambahan
                if total <= target:
                    hasil.append((menu, total))

            if len(hasil) == 0:
                print("Tidak ada menu yang sesuai target.")
                return

            garis_tabel = "-" * (LEBAR + 2)
            print("\n" + garis_tabel)
            print(f"| {f'REKOMENDASI MENU (MAKS {target:g} KKAL | TOPPING +{tambahan} KKAL)':^88} |")
            print(garis_tabel)
            print(f"| {'No.':^4} | {'Nama Menu':<47} | {'Total Kalori':^15} | {'Kategori':^13} |")
            print(garis_tabel)

            for idx, (menu, total) in enumerate(hasil, start=1):
                print(f"| {idx:>4} | {menu.item[:47]:<47} | "f"{f'{total:g} kkal':^15} | {menu.kategori_kalori(total):^13} |")
            print(garis_tabel)

        except ValueError:
            print("Target kalori harus berupa angka.")

    def hitung_total_kalori(self):
        print("\n" + "=" * 36 + "HITUNG TOTAL KALORI" + "=" * 37)
        menu = self.pilih_menu()
        if menu is None:
            return

        tambahan = self.input_topping()
        total = menu.kalori() + tambahan
        kategori = menu.kategori_kalori(total)

        garis_tabel = "-" * (LEBAR + 2)
        print("\n" + garis_tabel)
        print(f"| {'HASIL PERHITUNGAN TOTAL KALORI':^88} |")
        print(garis_tabel)
        print(f"| {'Nama Menu':<38} | {menu.item[:47]:<47} |")
        print(f"| {'Kalori Dasar':<38} | {f'{menu.kalori():g} kkal':<47} |")
        print(f"| {'Tambahan Topping':<38} | {f'+{tambahan} kkal':<47} |")
        print(garis_tabel)
        print(f"| {'Total Kalori':<38} | {f'{total:g} kkal':<47} |")
        print(f"| {'Kategori':<38} | {kategori:<47} |")
        print(garis_tabel)

    def tampilkan_menu_utama(self):
        print("\n" + "-" * (LEBAR + 2))
        baris("MINI PROJECT PEMROGRAMAN KOMPUTER - KELOMPOK 6C")
        print("-" * (LEBAR + 2))
        baris("MENU UTAMA")
        print("-" * (LEBAR + 2))
        print("|" + "  1. Cari menu".ljust(LEBAR) + "|")
        print("|" + "  2. Statistik nutrisi".ljust(LEBAR) + "|")
        print("|" + "  3. Bandingkan dua menu".ljust(LEBAR) + "|")
        print("|" + "  4. Klasifikasi kalori".ljust(LEBAR) + "|")
        print("|" + "  5. Rekomendasi menu berdasarkan target kalori".ljust(LEBAR) + "|")
        print("|" + "  6. Hitung total kalori + topping".ljust(LEBAR) + "|")
        print("|" + "  0. Keluar".ljust(LEBAR) + "|")
        print("-" * (LEBAR + 2))

    def jalankan(self):
        if not self.baca_csv():
            print("Error: Tidak ada data menu yang valid.")
            return

        self.tampilkan_menu()

        while True:
            self.tampilkan_menu_utama()
            pilihan = input("Pilihan: ")

            if pilihan == "0":
                print("\n" + "-" * (LEBAR + 2))
                baris("Terima kasih")
                print("-" * (LEBAR + 2))
                break
            elif pilihan == "1":
                self.cari_menu()
            elif pilihan == "2":
                self.statistik()
            elif pilihan == "3":
                self.bandingkan_menu()
            elif pilihan == "4":
                self.klasifikasi_kalori()
            elif pilihan == "5":
                self.rekomendasi_menu()
            elif pilihan == "6":
                self.hitung_total_kalori()
            else:
                print("Pilihan tidak valid.")


if __name__ == "__main__":
    aplikasi = AplikasiStarbucks(FILE)
    aplikasi.jalankan()