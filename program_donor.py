from datetime import datetime, timedelta
import random
import os
import time

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
            return

        # Gather data in a list
        data_list = []
        while current_node:
            data_list.append(current_node)
            current_node = current_node.next

        # Sort the list by blood type
        blood_order = {'A': 1, 'B': 2, 'AB': 3, 'O': 4}
        data_list.sort(key=lambda node: blood_order[node.gol_darah])

        # Display sorted data
        print("-------------------------")
        print("Data saat ini :\n")
        for node in data_list:
            print("No ID\t\t\t:", node.ID)
            print("Nama\t\t\t:", node.nama)
            print("Jenis kelamin\t\t:", node.gender)
            print("Umur\t\t\t:", node.umur)
            print("Alamat\t\t\t:", node.alamat)
            print("Golongan darah\t\t:", node.gol_darah)
            print("Terakhir donor darah\t:", node.waktu)
            print("-------------------------")

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

linked_list = LinkedList()

class fitur:
    def tambah_data():
        nama = input("Masukkan nama: ")
        while True:
            pilih_gender = int(input("Masukkan jenis kelamin ((1) Laki-laki // (2) Perempuan): "))
            if pilih_gender == 1:
                gender = "Laki-laki"
                break
            elif pilih_gender == 2:
                gender = "Perempuan"
                break
            else:
                print("Pilihan Anda tidak valid, coba lagi")
        umur = int(input("Masukkan umur: "))
        alamat= input("Masukkan alamat: ")
        while True:
            goldar = input("Masukkan golongan darah (A/AB/B/O) : ")
            pilih_goldar = goldar.lower()
            if pilih_goldar == 'a':
                gol_darah = 'A'
                break
            elif pilih_goldar == 'ab' :
                gol_darah = 'AB'
                break
            elif pilih_goldar == 'b':
                gol_darah = 'B'
                break
            elif pilih_goldar == 'o':
                gol_darah = 'O'
                break
            else:
                print("Golongan darah yang Anda masukkan tidak ada.")
        linked_list.tambah_data(nama, umur, gol_darah, gender, alamat)
        print("Data berhasil ditambahkan.")

    def cari_data():
        node_data = linked_list.head
        if node_data is not None:
            nama = input("Masukkan nama yang ingin dicari: ")
            linked_list.cari_data(nama)

    def hapus_data():
        node_data = linked_list.head
        if node_data is not None:
            ID = input("Masukkan ID yang ingin dihapus: ")
            linked_list.hapus_data(ID)

    def ubah_data():
        ID = input("Masukkan ID yang ingin diubah: ")
        if linked_list.cari_data_by_id(ID):
            print("Biarkan kosong jika tidak ingin mengubah.")
            nama_baru = input("Masukkan nama baru: ")
            gender_baru = input("Masukkan jenis kelamin: ")
            umur_baru = input("Masukkan umur baru: ")
            alamat_baru = input("Masukkan alamat baru: ")
            gol_darah_baru = input("Masukkan golongan darah baru: ")
            if umur_baru:
                umur_baru = int(umur_baru)
            linked_list.ubah_data(ID, nama_baru, umur_baru, gol_darah_baru, gender_baru, alamat_baru)
        else:
            print("Data tidak ditemukan.")

    def tampilkan_menu():
        print("\nPilih operasi yang ingin dilakukan:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Cari Data")
        print("5. Tampilkan Riwayat Terbaru")
        print("6. Ingatkan Donor Dua Bulan Kedepan")
        print("7. Ubah Data Pendonor")
        print("8. Update Tanggal Terakhir Donor")
        print("9. Keluar")

    def update_tanggal_donor():
        linked_list.tampilkan_data()
        ID = input("Masukkan ID pendonor yang ingin diperbarui tanggal terakhir donor darahnya: ")
        tanggal_baru = datetime.now().strftime("%Y-%m-%d %X")
        linked_list.update_tanggal_donor(ID, tanggal_baru)

def cari_data_by_id(self, ID):
    current_node = self.head
    while current_node:
        if current_node.ID == ID:
            return True
        current_node = current_node.next
    return False

LinkedList.cari_data_by_id = cari_data_by_id

def main():
    os.system('cls')
    while True:
        fitur.tampilkan_menu()
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7/8/9): ")
        if pilihan == "1":
            os.system('cls')
            fitur.tambah_data()
            time.sleep(2)
            os.system('cls')
        elif pilihan == "2":
            os.system('cls')
            linked_list.tampilkan_data()
            a = input("Tekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
            os.system('cls')
        elif pilihan == "3":
            os.system('cls')
            linked_list.tampilkan_data()
            fitur.hapus_data() 
            a = input("Tekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break                  
            os.system('cls')
        elif pilihan == "4":
            os.system('cls')
            linked_list.tampilkan_data()
            fitur.cari_data()
            a = input("Tekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
            os.system('cls')
        elif pilihan == "5":
            os.system('cls')
            linked_list.tampilkan_riwayat_terbaru()
            a = input("Tekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
            os.system('cls')
        elif pilihan == "6":
            os.system('cls')
            linked_list.ingatkan_donor()
            a = input("Tekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
            os.system('cls')
        elif pilihan == "7":
            fitur.ubah_data()
        elif pilihan == "8":
            fitur.update_tanggal_donor()
            time.sleep(2)
        elif pilihan == "9":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
