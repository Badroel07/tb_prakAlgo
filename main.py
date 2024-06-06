#Program_Utama

from class_linkedList import *
from class_Fitur import *
import os,time

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
