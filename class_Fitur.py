#Class_Fitur

from class_linkedList import *

linked_list = LinkedList()

class fitur:
    def tambah_data():
        nama = input("Masukkan nama: ")
        gender = input("Masukkan jenis kelamin: ")
        umur = int(input("Masukkan umur: "))
        alamat= input("Masukkan alamat: ")
        gol_darah = input("Masukkan golongan darah: ")
        linked_list.tambah_data(nama, umur, gol_darah, gender, alamat)
        print("Data berhasil ditambahkan.")

    def cari_data():
        nama = input("Masukkan nama yang ingin dicari: ")
        linked_list.cari_data(nama)

    def hapus_data():
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
        tanggal_baru = input("Masukkan tanggal baru (Format: YYYY-MM-DD): ")
        linked_list.update_tanggal_donor(ID, tanggal_baru)

def cari_data_by_id(self, ID):
    current_node = self.head
    while current_node:
        if current_node.ID == ID:
            return True
        current_node = current_node.next
    return False

LinkedList.cari_data_by_id = cari_data_by_id
