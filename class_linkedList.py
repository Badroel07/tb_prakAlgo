from datetime import datetime
import random

class Node:
    def __init__(self, nama, umur, gol_darah, waktu, ID):
        self.ID = ID
        self.nama = nama
        self.umur = umur
        self.gol_darah = gol_darah
        self.waktu = waktu
        self.next = None

class ID_generator:
    def __init__(self, id_length=5):
        self.used_ids = set()
        self.id_length = id_length

    def generate_id(self):
        while True:
            new_id = ''.join(random.choices('0123456789', k=self.id_length))
            if new_id not in self.used_ids:
                self.used_ids.add(new_id)
                return new_id

class LinkedList:
    def __init__(self):
        self.head = None
        self.head2 = None

    def tambah_data(self, nama, umur, gol_darah):
        ID_pendonor = ID_generator(id_length=5)
        ID = ID_pendonor.generate_id()
        waktu = datetime.now().strftime("%Y-%m-%d")
        new_node = Node(nama, umur, gol_darah, waktu, ID)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
        # Panggil riwayat_terbaru dengan new_node sebagai parameter
        self.riwayat_terbaru(new_node)

    def riwayat_terbaru(self, new_node):
        waktu = datetime.now().strftime("%Y-%m-%d")
        baru = Node(new_node.nama, new_node.umur, new_node.gol_darah, waktu, new_node.ID)
        if not self.head2:
            self.head2 = baru
        else:
            baru.next = self.head2
            self.head2 = baru

    def tampilkan_riwayat_terbaru(self):
        current_node = self.head2
        if current_node is None:
            print("Riwayat Terbaru kosong!")
        else:
            print("-------------------------")
            print("Riwayat Terbaru :\n")

        while current_node:
            print("No ID\t\t\t:", current_node.ID)
            print("Nama\t\t\t:", current_node.nama)
            print("Umur\t\t\t:", current_node.umur)
            print("Golongan darah\t\t:", current_node.gol_darah)
            print("Waktu terakhir donor\t:", current_node.waktu)
            print("-------------------------")
            current_node = current_node.next

    def tampilkan_data(self):
        current_node = self.head
        if current_node is None:
            print("Data kosong!")
        else:
            print("-------------------------")
            print("Data saat ini :\n")

        while current_node:
            print("No ID\t\t\t:", current_node.ID)
            print("Nama\t\t\t:", current_node.nama)
            print("Umur\t\t\t:", current_node.umur)
            print("Golongan darah\t\t:", current_node.gol_darah)
            print("Waktu terakhir donor\t:", current_node.waktu)
            print("-------------------------")
            current_node = current_node.next

    def hapus_data(self, ID):
        current_node = self.head
        if current_node and current_node.ID == ID:
            self.head = current_node.next
            current_node = None
            print("Data berhasil dihapus.")
            return
        prev = None
        while current_node and current_node.ID != ID:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            print("Data tidak ditemukan.")
            return
        prev.next = current_node.next
        current_node = None

    def cari_data(self, nama):
        found = False
        current_node = self.head
        while current_node:
            if nama.lower() in current_node.nama.lower():
                found = True
                print("Data ditemukan:")
                print("Nama:", current_node.nama)
                print("Umur:", current_node.umur)
                print("Golongan Darah:", current_node.gol_darah)
                print("Waktu Input:", current_node)
            current_node = current_node.next
        if not found:
            print("Data tidak ditemukan.")

# Membuat linked list
linked_list = LinkedList()
class fitur:
# Meminta input dari pengguna untuk menambah data
    def tambah_data():
        nama = input("Masukkan nama: ")
        umur = int(input("Masukkan umur: "))
        gol_darah = input("Masukkan golongan darah: ")
        linked_list.tambah_data(nama, umur, gol_darah)
        print("Data berhasil ditambahkan.")

# Meminta input dari pengguna untuk mencari data
    def cari_data():
        nama = input("Masukkan nama yang ingin dicari: ")
        linked_list.cari_data(nama)

# Meminta input dari pengguna untuk menghapus data
    def hapus_data():
        ID = input("Masukkan ID yang ingin dihapus: ")
        linked_list.hapus_data(ID)

# Menampilkan menu
    def tampilkan_menu():
        print("\nPilih operasi yang ingin dilakukan:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Cari Data")
        print("5. Tampilkan Riwayat Terbaru")
        print("6. Keluar")

# Program Utama
while True:
    fitur.tampilkan_menu()
    pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

    if pilihan == "1":
        fitur.tambah_data()
    elif pilihan == "2":
        linked_list.tampilkan_data()
    elif pilihan == "3":
        fitur.hapus_data()
    elif pilihan == "4":
        fitur.cari_data()
    elif pilihan == "5":
        linked_list.tampilkan_riwayat_terbaru()
    elif pilihan == "6":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
