class PenjelajahAngkasa:
    def __init__(self, nama, usia, energi):
        self.nama = nama
        self.usia = usia
        self.energi = energi
        self.berjelajah = False

    def jelajah(self):
        if not self.berjelajah:
            print(f"{self.nama} sedang menjelajah angkasa.")
            self.energi -= 10
            self.berjelajah = True
        else:
            print(f"{self.nama} sedang dalam perjalanan dan tidak dapat menjelajah lagi.")

    def kembali_dari_jelajah(self):
        if self.berjelajah:
            print(f"{self.nama} kembali dari perjalanan. Tingkat energi sekarang adalah {self.energi}.")
            self.berjelajah = False
        else:
            print(f"{self.nama} tidak sedang berjelajah, tidak dapat kembali.")

    def isi_ulang_energi(self) -> None:
        self.energi = 100

    def dapatkan_tingkat_energi(self) -> int:
        return self.energi

    def tampilkan_info(self) -> str:
        status = "Sedang berjelajah" if self.berjelajah else "Aktif"
        return f"Info {self.__class__.__name__}: Nama: {self.nama}, Usia: {self.usia}, Status: {status}, Tingkat Energi: {self.energi}"

    def edit_info(self, nama: str, usia: int) -> None:
        self.nama = nama
        self.usia = usia


class PesawatUlangAlik(PenjelajahAngkasa):
    def __init__(self, nama: str, usia: int, tingkat_bahan_bakar: int, detail_tambahan: str):
        super().__init__(nama, usia, energi=100)
        self.tingkat_bahan_bakar = tingkat_bahan_bakar
        self.detail_tambahan = detail_tambahan

    def lepas_landas(self) -> str:
        if self.energi >= 50 and self.tingkat_bahan_bakar >= 30:
            self.energi -= 50
            self.tingkat_bahan_bakar -= 30
            return f"{self.nama} lepas landas dengan pesawat ulang alik."
        else:
            return "Energi atau bahan bakar tidak mencukupi untuk lepas landas."

    def isi_ulang_bahan_bakar(self, jumlah: int) -> None:
        self.tingkat_bahan_bakar += jumlah

    def tampilkan_info(self) -> str:
        info_parent = super().tampilkan_info()
        return f"{info_parent}, Tingkat Bahan Bakar: {self.tingkat_bahan_bakar}, Detail Tambahan: {self.detail_tambahan}"

    def edit_info(self, nama: str, usia: int, tingkat_bahan_bakar: int, detail_tambahan: str) -> None:
        super().edit_info(nama, usia)
        self.tingkat_bahan_bakar = tingkat_bahan_bakar
        self.detail_tambahan = detail_tambahan


class AsistenRobot(PenjelajahAngkasa):
    def __init__(self, nama: str, usia: int, kecepatan_proses: int, detail_tambahan: str):
        super().__init__(nama, usia, energi=100)
        self.kecepatan_proses = kecepatan_proses
        self.detail_tambahan = detail_tambahan

    def bantu(self) -> str:
        if self.energi >= 20:
            self.energi -= 20
            return f"Asisten robot milik {self.nama} sedang memberikan bantuan."
        else:
            return "Energi tidak mencukupi untuk memberikan bantuan."

    def tampilkan_info(self) -> str:
        info_parent = super().tampilkan_info()
        return f"{info_parent}, Kecepatan Proses: {self.kecepatan_proses}, Detail Tambahan: {self.detail_tambahan}"

    def edit_info(self, nama: str, usia: int, kecepatan_proses: int, detail_tambahan: str) -> None:
        super().edit_info(nama, usia)
        self.kecepatan_proses = kecepatan_proses
        self.detail_tambahan = detail_tambahan

def menu_penjelajah_angkasa(objek_angkasa):
    while True:
        print("\nMenu Penjelajah Angkasa:")
        print("1. Tambah Penjelajah Angkasa")
        print("2. Edit Penjelajah Angkasa")
        print("3. Hapus Penjelajah Angkasa")
        print("4. Tampilkan Penjelajah Angkasa")
        print("5. Jelajah")
        print("6. Kembali dari Jelajah")
        print("7. Isi Ulang Energi")
        print("0. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan (0-7): ")

        if pilihan == '1':
            tambah_objek(objek_angkasa, 'Penjelajah Angkasa')
        elif pilihan == '2':
            edit_objek(objek_angkasa, 'Penjelajah Angkasa')
        elif pilihan == '3':
            hapus_objek(objek_angkasa, 'Penjelajah Angkasa')
        elif pilihan == '4':
            tampilkan_objek(objek_angkasa, 'Penjelajah Angkasa')
        elif pilihan == '5':
            menu_fungsi_objek(objek_angkasa, 'Penjelajah Angkasa', 'jelajah_menu')
        elif pilihan == '6':
            menu_fungsi_objek(objek_angkasa, 'Penjelajah Angkasa', 'kembali_dari_jelajah_menu')
        elif pilihan == '7':
            menu_fungsi_objek(objek_angkasa, 'Penjelajah Angkasa', 'isi_ulang_energi_menu')
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")



def menu_pesawat_ulang_alik(objek_angkasa):
    while True:
        print("\nMenu Pesawat Ulang Alik:")
        print("1. Tambah Pesawat Ulang Alik")
        print("2. Edit Pesawat Ulang Alik")
        print("3. Hapus Pesawat Ulang Alik")
        print("4. Tampilkan Pesawat Ulang Alik")
        print("5. Lepas Landas")
        print("6. Isi Ulang Bahan Bakar")
        print("0. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan (0-6): ")

        if pilihan == '1':
            tambah_objek(objek_angkasa, 'Pesawat Ulang Alik')
        elif pilihan == '2':
            edit_objek(objek_angkasa, 'Pesawat Ulang Alik')
        elif pilihan == '3':
            hapus_objek(objek_angkasa, 'Pesawat Ulang Alik')
        elif pilihan == '4':
            tampilkan_objek(objek_angkasa, 'Pesawat Ulang Alik')
        elif pilihan == '5':
            menu_fungsi_objek(objek_angkasa, 'Pesawat Ulang Alik', 'lepas_landas_menu')
        elif pilihan == '6':
            menu_fungsi_objek(objek_angkasa, 'Pesawat Ulang Alik', 'isi_ulang_bahan_bakar_menu')
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def menu_asisten_robot(objek_angkasa):
    while True:
        print("\nMenu Asisten Robot:")
        print("1. Tambah Asisten Robot")
        print("2. Edit Asisten Robot")
        print("3. Hapus Asisten Robot")
        print("4. Tampilkan Asisten Robot")
        print("5. Bantu")
        print("0. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan (0-5): ")

        if pilihan == '1':
            tambah_objek(objek_angkasa, 'Asisten Robot')
        elif pilihan == '2':
            edit_objek(objek_angkasa, 'Asisten Robot')
        elif pilihan == '3':
            hapus_objek(objek_angkasa, 'Asisten Robot')
        elif pilihan == '4':
            tampilkan_objek(objek_angkasa, 'Asisten Robot')
        elif pilihan == '5':
            menu_fungsi_objek(objek_angkasa, 'Asisten Robot', 'bantu_menu')
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tambah_objek(objek_angkasa, kategori):
    nama = input(f"Masukkan nama {kategori.lower()}: ")
    usia = int(input("Masukkan usia: "))
    if kategori == 'Penjelajah Angkasa':
        objek = PenjelajahAngkasa(nama, usia, energi=100)
    elif kategori == 'Pesawat Ulang Alik':
        bahan_bakar = int(input("Masukkan tingkat bahan bakar: "))
        detail_tambahan = input("Masukkan detail tambahan: ")
        objek = PesawatUlangAlik(nama, usia, bahan_bakar, detail_tambahan)
    elif kategori == 'Asisten Robot':
        kecepatan = int(input("Masukkan kecepatan proses: "))
        detail_tambahan = input("Masukkan detail tambahan: ")
        objek = AsistenRobot(nama, usia, kecepatan, detail_tambahan)
    else:
        print("Kategori tidak valid.")
        return

    objek_angkasa[kategori].append(objek)
    print(f"{nama} telah ditambahkan sebagai {kategori.lower()}.")


def edit_objek(objek_angkasa, kategori):
    if not objek_angkasa[kategori]:
        print(f"Belum ada objek {kategori} yang dibuat.")
        return

    tampilkan_objek(objek_angkasa, kategori)
    idx = int(input(f"Masukkan indeks objek {kategori} yang ingin diedit: "))

    if 0 <= idx < len(objek_angkasa[kategori]):
        objek = objek_angkasa[kategori][idx]
        nama_baru = input("Masukkan nama baru: ")
        usia_baru = int(input("Masukkan usia baru: "))

        if kategori == 'Penjelajah Angkasa':
            objek.edit_info(nama_baru, usia_baru)
        elif kategori == 'Pesawat Ulang Alik':
            bahan_bakar_baru = int(input("Masukkan tingkat bahan bakar baru: "))
            detail_tambahan = input("Masukkan detail tambaha: n")
            objek.edit_info(nama_baru, usia_baru, bahan_bakar_baru, detail_tambahan)
        elif kategori == 'Asisten Robot':
            kecepatan_baru = int(input("Masukkan kecepatan proses baru: "))
            detail_tambahan = input("Masukkan detail tambahan: ")
            objek.edit_info(nama_baru, usia_baru, kecepatan_baru, detail_tambahan)

        print(f"Info objek {kategori} berhasil diubah.")
    else:
        print("Indeks objek tidak valid.")


def hapus_objek(objek_angkasa, kategori):
    if not objek_angkasa[kategori]:
        print(f"Belum ada objek {kategori} yang dibuat.")
        return

    tampilkan_objek(objek_angkasa, kategori)
    idx = int(input(f"Masukkan indeks objek {kategori} yang ingin dihapus: "))

    if 0 <= idx < len(objek_angkasa[kategori]):
        objek_angkasa[kategori].pop(idx)
        print(f"Objek {kategori} berhasil dihapus.")
    else:
        print("Indeks objek tidak valid.")

def jelajah_menu(objek):
    objek.jelajah()
    return f"{objek.nama} telah menjelajah angkasa dan tingkat energi sekarang adalah {objek.energi}."
    
def kembali_dari_jelajah_menu(objek):
    objek.kembali_dari_jelajah()
    return f"{objek.nama} telah kembali dari perjalanan dan tingkat energi sekarang adalah {objek.energi}."

def tampilkan_objek(objek_angkasa, kategori):
    print(f"\nData {kategori}:")
    if not objek_angkasa[kategori]:
        print("Belum ada data.")
    else:
        for idx, objek in enumerate(objek_angkasa[kategori]):
            print(f"{idx}. {objek.tampilkan_info()}")


def menu_fungsi_objek(objek_angkasa, kategori, fungsi_menu):
    if not objek_angkasa[kategori]:
        print(f"Belum ada objek {kategori} yang dibuat.")
        return

    tampilkan_objek(objek_angkasa, kategori)
    idx = int(input(f"Masukkan indeks objek {kategori} yang akan digunakan: "))

    if 0 <= idx < len(objek_angkasa[kategori]):
        objek = objek_angkasa[kategori][idx]
        if fungsi_menu == 'jelajah_menu':
            print(objek.jelajah())
        elif fungsi_menu == 'lepas_landas_menu':
            print(objek.lepas_landas())
        elif fungsi_menu == 'kembali_dari_jelajah_menu':
            print(kembali_dari_jelajah_menu(objek))
        elif fungsi_menu == 'isi_ulang_energi_menu':
            objek.isi_ulang_energi()
            print(f"Energi {objek.nama} telah diisi ulang.")
        elif fungsi_menu == 'isi_ulang_bahan_bakar_menu':
            jumlah = int(input("Masukkan jumlah bahan bakar yang ingin diisi: "))
            objek.isi_ulang_bahan_bakar(jumlah)
            print(f"Bahan bakar pesawat {objek.nama} telah diisi ulang sebanyak {jumlah}.")
        elif fungsi_menu == 'bantu_menu':
            print(objek.bantu())
        else:
            print("Fungsi tidak valid.")
    else:
        print("Indeks objek tidak valid.")

def main_menu():
    objek_angkasa = {'Penjelajah Angkasa': [], 'Pesawat Ulang Alik': [], 'Asisten Robot': []}

    while True:
        print("\nMenu Utama:")
        print("1. Menu Penjelajah Angkasa")
        print("2. Menu Pesawat Ulang Alik")
        print("3. Menu Asisten Robot")
        print("4. Tampilkan Semua Data")
        print("0. Keluar")

        kategori_pilihan = input("Masukkan kategori (0-4): ")

        if kategori_pilihan == '1':
            menu_penjelajah_angkasa(objek_angkasa)
        elif kategori_pilihan == '2':
            menu_pesawat_ulang_alik(objek_angkasa)
        elif kategori_pilihan == '3':
            menu_asisten_robot(objek_angkasa)
        elif kategori_pilihan == '4':
            tampilkan_semua_data(objek_angkasa)
        elif kategori_pilihan == '0':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def tampilkan_semua_data(objek_angkasa):
    for kelas, objek_list in objek_angkasa.items():
        print(f"\nData {kelas}:")
        if not objek_list:
            print("Belum ada data.")
        else:
            for objek in objek_list:
                print(objek.tampilkan_info())

if __name__ == "__main__":
    main_menu()