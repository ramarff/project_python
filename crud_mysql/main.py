import os
import modul

run = True
while run:
    os.system('clear')
    print('=' * 10, 'TABEL MAHASISWA', '=' * 10)
    modul.show_data()
    print('=' * 37)
    print('1. Tambah Data')
    print('2. Edit Data')
    print('3. Hapus Data')
    print('4. Cari Data')
    print('0. Keluar')
    print('=' * 37)
    user_input = int(input('Pilih nomor: '))
    print('=' * 37)
    
    if user_input == 1:
        modul.tambah_data()
        wait = input('\nTekan ENTER untuk kembali!\n')
    elif user_input == 2:
        modul.edit_data()
        wait = input('\nTekan ENTER untuk kembali!\n')
    elif user_input == 3:
        print('Data dengan NIM yang Anda input akan dihapus!')
        modul.hapus_data()
        wait = input('\nTekan ENTER untuk kembali!\n')
    elif user_input == 4:
        modul.cari_data()
        wait = input('\nTekan ENTER untuk kembali!\n')
    elif user_input == 0:
        run = False
    else:
        print('Pilihan tidak tersedia!')
        wait = input('\nTekan ENTER untuk kembali!\n')