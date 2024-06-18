#Program_Utama

from class_linkedList import *
from class_Fitur import *
import os,time

def main():
    os.system('cls')
    while True:
        os.system('cls')
        fitur.tampilkan_menu()
        pilihan = input("\nMasukkan pilihan (1-9): ")
        if pilihan == "1":
            os.system('cls')
            fitur.tambah_data()
            time.sleep(2)
        elif pilihan == "2":
            os.system('cls')
            linked_list.tampilkan_data()
            a = input("Tekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
        elif pilihan == "3":
            os.system('cls')
            linked_list.tampilkan_data()
            fitur.hapus_data() 
            a = input("--------------------------------------------\nTekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break                  
        elif pilihan == "4":
            os.system('cls')
            linked_list.tampilkan_data()
            fitur.cari_data()
            a = input("--------------------------------------------\nTekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
        elif pilihan == "5":
            os.system('cls')
            linked_list.tampilkan_riwayat_terbaru()
            a = input("Tekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
        elif pilihan == "6":
            os.system('cls')
            linked_list.ingatkan_donor()
            a = input("--------------------------------------------\nTekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
        elif pilihan == "7":
            os.system('cls')
            linked_list.tampilkan_data()
            fitur.ubah_data()
            a = input("--------------------------------------------\nTekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
        elif pilihan == "8":
            os.system('cls')
            linked_list.tampilkan_data()
            fitur.update_tanggal_donor()
            a = input("--------------------------------------------\nTekan enter untuk kembali ke menu utama. . .")
            if a == '\n':
                break
        elif pilihan == "9":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
