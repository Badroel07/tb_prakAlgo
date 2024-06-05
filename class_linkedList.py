#Bismillah beres Ya Allah :)
#Class_LinkedList

from datetime import datetime, timedelta
import random,os,time

class Node:
    def __init__(self, nama, umur, gol_darah, waktu, ID, gender, alamat):
        self.ID = ID
        self.nama = nama
        self.umur = umur
        self.gol_darah = gol_darah
        self.waktu = waktu
        self.gender = gender
        self.alamat = alamat
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

    def tambah_data(self, nama, umur, gol_darah, gender, alamat):
        ID_pendonor = ID_generator(id_length=5)
        ID = ID_pendonor.generate_id()
        waktu = datetime.now().strftime("%Y-%m-%d %X")
        new_node = Node(nama, umur, gol_darah, waktu, ID, gender, alamat)
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
        baru = Node(new_node.nama, new_node.umur, new_node.gol_darah, new_node.waktu, new_node.ID, new_node.gender, new_node.alamat)
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
            print("Jenis kelamin\t\t:", current_node.gender)
            print("Umur\t\t\t:", current_node.umur)
            print("Alamat\t\t\t:", current_node.alamat)
            print("Golongan darah\t\t:", current_node.gol_darah)
            print("Terakhir donor darah\t:", current_node.waktu)
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
            print("Jenis kelamin\t\t:", current_node.gender)
            print("Umur\t\t\t:", current_node.umur)
            print("Alamat\t\t\t:", current_node.alamat)
            print("Golongan darah\t\t:", current_node.gol_darah)
            print("Terakhir donor darah\t:", current_node.waktu)
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
                print("Jenis kelamin:", current_node.gender)
                print("Umur:", current_node.umur)
                print("Alamat:", current_node.alamat)
                print("Golongan Darah:", current_node.gol_darah)
                print("Terakhir donor darah:", current_node.waktu)
            current_node = current_node.next
        if not found:
            print("Data tidak ditemukan.")

    def ingatkan_donor(self):
        reminder_date = datetime.now() + timedelta(days=60)
        current_node = self.head
        found = False

        print("-------------------------")
        print("Pengingat Donor Dua Bulan Kedepan :\n")

        while current_node:
            last_donor_date = datetime.strptime(current_node.waktu, "%Y-%m-%d %X")
            next_donor_date = last_donor_date + timedelta(days=60)
            if last_donor_date <= reminder_date:
                found = True
                print("No ID\t\t\t:", current_node.ID)
                print("Nama\t\t\t:", current_node.nama)
                print("Umur\t\t\t:", current_node.umur)
                print("Golongan darah\t\t:", current_node.gol_darah)
                print("Waktu terakhir donor\t:", current_node.waktu)
                print("Tanggal donor berikutnya\t:", next_donor_date.strftime("%Y-%m-%d"))
                print("-------------------------")
            current_node = current_node.next

        if not found:
            print("Tidak ada pendonor yang perlu diingatkan untuk donor dalam dua bulan ke depan.")

    def ubah_data(self, ID, nama_baru=None, umur_baru=None, gol_darah_baru=None, gender_baru=None, alamat_baru=None):
        current_node = self.head
        while current_node:
            if current_node.ID == ID:
                if nama_baru:
                    current_node.nama = nama_baru
                if gender_baru:
                    current_node.gender = gender_baru
                if umur_baru:
                    current_node.umur = umur_baru
                if alamat_baru:
                    current_node.alamat = alamat_baru
                if gol_darah_baru:
                    current_node.gol_darah = gol_darah_baru
                print("Data berhasil diubah.")
                return
            current_node = current_node.next
        print("Data tidak ditemukan.")

    def update_tanggal_donor(self, ID, tanggal_baru):
        current_node = self.head
        while current_node:
            if current_node.ID == ID:
                current_node.waktu = tanggal_baru
                print("Tanggal terakhir donor darah berhasil diperbarui.")
                # Panggil riwayat_terbaru dengan node yang diperbarui
                self.riwayat_terbaru(current_node)
                return
            current_node = current_node.next
        print("Data tidak ditemukan.")
