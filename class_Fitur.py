#Class_Fitur

from class_linkedList import *

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
