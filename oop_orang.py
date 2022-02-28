import os
# import datetime

# class Orang:
# 	def __init__(self, nama, tanggal_lahir):
# 		date=tanggal_lahir.split("-")
# 		self.nama=nama
# 		self.tanggal_lahir=datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
# 		self.tahun_sekarang=datetime.datetime.now()

# 	def umur(self):
# 		return f"{self.tahun_sekarang.year - self.tanggal_lahir.year}"
# print(Orang("Rama Fajar","2003-06-30").umur())

# class Pegawai:
# 	honor_per_jam=30000

# 	def __init__(self, nama, jumlah_jam):
# 		self.nama=nama
# 		self.jumlah_jam=jumlah_jam

# 	def honor(self):
# 		return f"{self.honor_per_jam * self.jumlah_jam}"

# rama=Pegawai("Rama Fajar", 10)
# print(rama.honor_per_jam)
# print(Pegawai("Rama Fajar", 10).honor())

# shell=os.popen("echo $SHELL").read().split("/")[3].replace("/n","")
# print(shell)
shell=os.system("echo $SHELL")
# print(shell)