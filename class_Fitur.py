#Class_Fitur
from class_linkedList import *
import class_linkedList as cll

linked_list = LinkedList()

class fitur:
    def tambah_data():
        print ("\n==== TAMBAH DATA BARU ====\n")
        nama = input("Masukkan nama\t\t\t\t\t\t: ")
        while True:
            try:
                pilih_gender = int(input("Masukkan jenis kelamin ((1) Laki-laki // (2) Perempuan)\t: "))
                if pilih_gender == 1:
                    gender = "Laki-laki"
                    break
                elif pilih_gender == 2:
                    gender = "Perempuan"
                    break
                else:
                    print("Pilihan Anda tidak valid, coba lagi")
            except ValueError:
                print("Pilihan Anda tidak valid, coba lagi")
        while True:    
            try:
                umur = int(input("Masukkan umur\t\t\t\t\t\t: "))
                break
            except ValueError:
                print("Umur yang Anda masukkan tidak valid.")
        alamat= input("Masukkan alamat\t\t\t\t\t\t: ")
        while True:
            goldar = input("Masukkan golongan darah (A/AB/B/O)\t\t\t: ")
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
        print("-----------------------\nData berhasil ditambahkan.")

    def cari_data():
        cll.flag = 0
        while True:
            if cll.flag == 1:
                break
            node_data = linked_list.head
            if node_data is not None:
                nama = input("Masukkan nama yang ingin dicari: ")
                linked_list.cari_data(nama)
                if cll.flag == 2:
                    while True:
                        try:
                            konfirm = int(input("1. Ganti nama yang akan dicari\n2. Kembali ke Menu Utama\nPilihan : "))
                            if konfirm == 1:
                                cll.flag = 0
                                os.system('cls')
                                linked_list.tampilkan_data()
                                break
                            elif konfirm == 2:
                                cll.flag = 1
                                break
                            else:
                                print("Pilihan Anda tidak valid")
                        except ValueError:
                            print("Pilihan Anda tidak valid")
                else:
                    cll.flag = 1
                    break
            else:
                break

    def hapus_data():
        cll.flag = 0
        while True:
            if cll.flag == 1:
                break
            node_data = linked_list.head
            if node_data is not None:
                ID = input("Masukkan ID yang ingin dihapus: ")
                linked_list.hapus_data(ID)
                if cll.flag == 2:
                    while True:
                        try:
                            konfirm = int(input("1. Ganti ID yang akan dihapus\n2. Kembali ke Menu Utama\nPilihan : "))
                            if konfirm == 1:
                                cll.flag = 0
                                os.system('cls')
                                linked_list.tampilkan_data()
                                break   
                            elif konfirm == 2:
                                cll.flag = 1
                                break
                            else:
                                print("Pilihan Anda tidak valid")    
                        except ValueError:
                            print("Pilihan Anda tidak valid")  
                else:
                    cll.flag = 1
                    break
            else:
                break                
                            

    def ubah_data():
        flag = 0
        while True:
            if flag == 1:
                break
            node_data = linked_list.head
            if node_data is not None:
                ID = input("Masukkan ID yang ingin diubah: ")  
                if linked_list.cari_data_by_id(ID):
                    nama_baru = input("Masukkan nama baru: ")
                    while True:
                        try:
                            pilih_gender = int(input("Masukkan jenis kelamin ((1) Laki-laki // (2) Perempuan): "))
                            if pilih_gender == 1:
                                gender_baru = "Laki-laki"
                                break
                            elif pilih_gender == 2:
                                gender_baru = "Perempuan"
                                break
                            else:
                                print("Pilihan Anda tidak valid, coba lagi")
                        except ValueError:
                            print("Pilihan Anda tidak valid, coba lagi")
                    umur_baru = input("Masukkan umur baru: ")
                    alamat_baru = input("Masukkan alamat baru: ")
                    while True:
                        goldar = input("Masukkan golongan darah (A/AB/B/O) : ")
                        pilih_goldar = goldar.lower()
                        if pilih_goldar == 'a':
                            gol_darah_baru = 'A'
                            break
                        elif pilih_goldar == 'ab' :
                            gol_darah_baru = 'AB'
                            break
                        elif pilih_goldar == 'b':
                            gol_darah_baru = 'B'
                            break
                        elif pilih_goldar == 'o':
                            gol_darah_baru = 'O'
                            break
                        else:
                            print("Golongan darah yang Anda masukkan tidak ada.")
                    if umur_baru:
                        umur_baru = int(umur_baru)
                    linked_list.ubah_data(ID, nama_baru, umur_baru, gol_darah_baru, gender_baru, alamat_baru)
                    print("\nData berhasil di ubah!")
                    time.sleep(2)
                    break
                else:
                    os.system('cls')
                    print("Data tidak ditemukan.")
                    while True:
                        try:
                            konfirm = int(input("1. Ganti ID yang akan diubah\n2. Kembali ke Menu Utama\nPilihan : "))
                            if konfirm == 1:
                                os.system('cls')
                                linked_list.tampilkan_data()
                                break
                            elif konfirm == 2:
                                flag = 1
                                break
                            else:
                                print("Pilihan Anda tidak valid")
                        except ValueError:
                            print("Pilihan Anda tidak valid")
            else:
                break       
                
    def tampilkan_menu():
        print("\n==== PROGRAM MANAJEMEN DATA DONOR DARAH ====")
        print("============================================\n")
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
