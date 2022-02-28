# class Kucing:
# 	warna=None
# 	usia=None

# kucing1=Kucing()
# kucing1.warna="hitam"
# kucing1.usia="3 bulan"

# kucing2=Kucing()
# kucing2.warna="putih"
# kucing2.usia="2 bulan"

# kucing3=Kucing()
# kucing3.warna="kuning"
# kucing3.usia="3.5 bulan"

# print(kucing1.warna)
# print(kucing1.usia)

# class Mahasiswa:
# 	nama=None
# 	asal=None

# 	def perkenalan(self):
# 		print(f"Perkenalan saya {self.nama} dari {self.asal}")

# rama=Mahasiswa()
# rama.nama="Rama Fajar Fadhillah"
# rama.asal="Jakarta"

# rama.perkenalan()

# class Mahasiswa:
# 	"""
# 	Kelas ini digunakan untuk mendefenisikan objek Mahasiswa
# 	di kehidupan nyata
# 	"""

	# def __init__(self, nama, asal):
	# 	self.nama=nama
	# 	self.asal=asal

	# def perkenalan(self):
	# 	print(f"Perkenalkan saya {self.nama} dari {self.asal}")
# rama=Mahasiswa("Rama","Jakarta")
# rama.perkenalan()
# print(Mahasiswa.__doc__)

# class Kucing:
# 	def __init__(self, warna, usia):
# 		self.warna=warna
# 		self.usia=usia

# class Mahasiswa:
# 	"""kelas mahasiswa"""
# 	def __init__(self, nama, asal, kucing):
# 		self.nama=nama
# 		self.asal=asal
# 		self.kucing=kucing

# 	def perkenalan(self):
# 		print(f'Perkenalkan saya {self.nama} dari {self.asal}')
# 		print(f'Saya memiliki kucing berwarna {self.kucing.warna} usia {self.kucing.usia}')
# rama=Mahasiswa("Rama","Jakarta", kucing=Kucing("Merah","3 bulan"))
# rama.perkenalan()

# class Orang:
# 	def __init__(self, nama, asal):
# 		self.nama=nama
# 		self.asal=asal
# 		print("fungsi Orang.__init__() dieksekusi")

# 	def perkenalan(self):
# 		print(f"Perkenalkan saya {self.nama} dari {self.asal}")

class Pelajar(Orang):
	def __init__(self, nama, asal,sekolah):
		self.nama=nama
		self.asal=asal
		super().__init__(nama,asal)
		self.sekolah=sekolah
	

# class Pekerja(Orang):
# 	def __init__(self, nama, asal, tempat_kerja):
# 		self.nama=nama
# 		self.asal=asal
# 		Orang.__init__(self, nama, asal)
# 		self.tempat_kerja=tempat_kerja

# Manisa=Pelajar("Manisa Bachtiar","Lampung","SMKN 1 Lampung")
# Manisa.perkenalan()

# Rama=Pekerja("Rama Fajar Fadhillah","Jakarta","gayeng.co")
# Rama.perkenalan()

# class Kendaraan:
# 	def berjalan(self):
# 		print("Berjalan...")

# class Mobil(Kendaraan):
# 	def berjalan(self, kecepatan, satuan="km/jam"):
# 		super().berjalan()
# 		print(f"Berjalan dengan kecepatan {kecepatan} {satuan}")

# sepeda=Kendaraan()
# mobil=Mobil()
# sepeda.berjalan()
# mobil.berjalan("100")

class Mobil:
	def __init__(self, merk):
		self._merk=merk
		self.__kecepatan=100

class MobilBalap(Mobil):
	def __init__(self, merk, total_gear):
		super().__init__(merk)
		self._total_gear=total_gear

	def pamer(self):
		print(f"Ini mobil {self._merk} dengan total total_gear {self._total_gear} dan dengan kecepatan {self.__kecepatan} km/jam")

sedan=Mobil("Toyota")


# print(f"Merk:{sedan._merk}")
# ferrari=MobilBalap("Ferrari", 8)
# ferrari.pamer()

# class Motor:
# 	def __init__(self, tahun):
# 		self.tahun=tahun

# 	@property
# 	def tahun(self):
# 		return self.__tahun

# 	@tahun.setter
# 	def tahun(self, tahun):
# 		if tahun > 2021:
# 			self.__tahun=2021
# 		elif tahun < 2021:
# 			self.__tahun=1990
# 		else:
# 			self.__tahun=tahun

# Beat=Motor(2019)
# print(f"Motor ini dibuat tahun {Beat.tahun}")


# class Angka:
# 	def __init__(self, angka):
# 		self.angka=angka

# 	def __add__(self, objek):
# 		return self.angka + objek.angka

# 	def __lt__(self, objek):
# 		return self.angka < objek.angka

# 	def __eq__(self, objek):
# 		return self.angka == objek.angka

# x1=Angka(10)
# x2=Angka(20)


# print(x1+x2)
# print(x1 < x2)
# print(x1 > x2)


# class Segitiga:
# 	def __init__(self, a, t):
# 		self.alas=a
# 		self.tinggi=t

# 	def __str__(self):
# 		luas=0.5 * self.alas * self.tinggi
# 		return f"segitiga (alas={self.alas} tinggi={self.tinggi} luas={luas})"

# a=Segitiga(10,10)
# b=Segitiga(20,10)
# print(a)

# class Contoh:
# 	def __str__(self):
# 		return "bentuk informal"

# 	def __repr__(self):
# 		return "bentuk formal"

# x=Contoh()
# print(x)
# print(str(x))
# print(repr(x))

# class Siswa:
# 	def __init__(self):
# 		self.__list_siswa=[]

# 	def tambah_siswa(self, siswa):
# 		self.__list_siswa.append(siswa)

# 	def __len__(self):
# 		return len(self.__list_siswa)

# 	def __getitem__(self, position):
# 		return self.__list_siswa[position]

# grup1=Siswa()
# grup1.tambah_siswa('Rama')
# grup1.tambah_siswa('Fajar')

# print(len(grup1))
# print(grup1[0])

#Destructor
# a=3
# print(a)
# del a
# print(a)

# class Mahasiswa:
# 	def __init__(self, nama):
# 		self.nama=nama
# 		print(f"mahasiswa {self.nama} dibuat")

# 	def __del__(self):
# 		print(f"mahasiswa {self.nama} dihapus")

# print("Halo dunia")
# rama=Mahasiswa("Rama")
# print("Halo semuanya")
# fajar=Mahasiswa("Fajar")
# print("1+1=2")
# print("3+3=6")


class Ayah:
	def __init__(self, kulit, rambut, sifat):
		self.kulit=kulit
		self.rambut=rambut
		self.sifat=sifat

class Ibu:
	def __init__(self, kulit, rambut, sifat):
		self.kulit=kulit
		self.rambut=rambut
		self.sifat=sifat

class Anak():
	def __init__(self, nama):
		self.nama=nama
		self.rambut=ibu.rambut

	def perkenalan(self):
		print(f"Nama saya adalah {self.nama} dan saya berambut {self.rambut}")

ayah=Ayah("putih","ikal","humoris")
ibu=Ibu("kuning langsat","lurus","anggun")
# print(ayah.kulit)
# rama=Anak("Rama")
# rama.perkenalan()
keysa=Anak("keysa")
keysa.perkenalan()
