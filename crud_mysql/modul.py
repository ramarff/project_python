"""
Sesuaikan nama-nama berikut dengan database mysql masing-masing:
localhost, root, dan passord -> jika menggunakan xampp dan tidak pernah diganti, maka biarkan saja.
dblatihan -> nama database
mahasiswa -> nama tabel
nim, nama, kode_prodi -> nama head kolom
"""
import pymysql

db = pymysql.connect(host='localhost', user='root',
                     password='KOPIHITAM645', database='db_crud')
cursor = db.cursor()


def show_data():
    dokumen = 'select * from mahasiswa'
    try:
        cursor.execute(dokumen)
        hasil = cursor.fetchall()
        for data in hasil:
            print(data)
    except:
        print('Data masih kosong!')


def tambah_data():
    nim = input('NIM\t\t: ')
    nama = input('Nama\t\t: ')
    kode_prodi = input('Kode Prodi\t: ')

    dokumen = "insert into mahasiswa(\
            nim, nama, kode_prodi)\
            values('%s', '%s', '%s')" % \
        (nim, nama, kode_prodi)

    try:
        cursor.execute(dokumen)
        db.commit()
    except:
        db.rollback()


def edit_data():
    nim = input('Masukkan NIM untuk mencari '
                'data yang akan diedit : ')
    nama = input('Nama baru: ')

    dokumen = "update mahasiswa set nama = %s"\
        " where nim = %s"
    nilai = (nama, nim)

    try:
        cursor.execute(dokumen, nilai)
        db.commit()
    except:
        db.rollback()


def hapus_data():
    nim = input('NIM\t: ')

    dokumen = 'delete from mahasiswa where nim = %s' % (nim)

    try:
        cursor.execute(dokumen)
        db.commit()
    except:
        db.rollback()


def cari_data():
    print('Cari Mahasiswa dengan NIM')
    nim = input('NIM\t: ')

    dokumen = "select * from mahasiswa\
        where nim = '%s'" % (nim)

    try:
        cursor.execute(dokumen)
        hasil = cursor.fetchall()
        for data in hasil:
            nama, kode_prodi = data[1], data[2]
            print(f'Nama\t: {nama}\nProdi\t: {kode_prodi}')
    except:
        print('Tidak ditemukan')