import csv

# ---------- Inisialisasi data ----------
FILE = "starbucks.csv"
KOLOM = ["item", "calories", "fat", "carb", "fiber", "protein", "type"]
ANGKA = ["calories", "fat", "carb", "fiber", "protein"]
TOPPING = {"mentega": 102, "selai": 56, "cream cheese": 51}



# ---------- Fungsi bantu ----------
def validasi_data(baris):
    # Sub flowchart validasi data: True jika data valid
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


# ---------- Program utama ----------
def main():
    print("=== MINI PROJECT PEMROGRAMAN KOMPUTER - KELOMPOK 6C ===")
    menu = baca_file_csv()
    if len(menu) == 0:
        print("Error: file tidak ditemukan, kolom tidak lengkap, atau tidak ada data valid.")
    else:
        print("Data siap digunakan.")


main()