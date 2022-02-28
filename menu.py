# #Variable global untuk menyimpan data Buku
# buku=[]

# #fungsi untuk menampilkan semua data
# def show_data():
#     if len(buku) <= 0:
#         print "Belum ada data"
#     else:
#         for i in range(len(buku)):
#             print "[%d] %s" % (i, buku[i])

# #fungsi untuk menambah data
# def insert_data():
#     buku_baru=raw_input("Judul Buku:")
#     buku.append(buku_baru)

# #fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks=input("Inputkan ID buku:")

#     if(indeks > len(buku)):
#         print "ID Salah"
#     else:
#         judul_baru=raw_input("Judul baru:")
#         buku[indeks]=judul_baru

# #fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks=input("Inputkan ID buku:")
#     if (indeks > len(buku)):
#         print "ID salah"
#     else:
#         buku.remove(buku[indeks])

# #fungsi untuk menampilkan menu
# def show_menu():
#     print"\n"
#     print"----------------------------MENU----------------------"
#     print"[1] Show Data"
#     print"[2] Show Data"
#     print"[3] Show Data"
#     print"[4] Show Data"
#     print"[5] Exit"

#     menu=input("Pilih Menu")

#     print "\n"

#     if menu == 1:
#         show_data()
#     elif menu == 2:
#         insert_data()
#     elif menu == 3:
#         edit_data()
#     elif menu == 4:
#         delete_data()
#     elif menu == 5:
#         exit()
#     else:
#         print "Input Salah!"


# if __name__ == "__main__":

#     while(True):
#         show_menu()

import animation
import time

tags = ["Data sedang dimuat",".","..","...","....",".....","......",".......","........",".........","..........","...........","............",".............","..............","...............","................",".................",".................."]

animation = animation.Wait(tags, color="white", speed=0.1)

def rama():
    data=[]
    if len(data) <= 0:
        animation.start()
    # else :
        # animation.stop()
rama()
time.sleep(50)
animation.stop()