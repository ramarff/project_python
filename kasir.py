# menu={
# 	"Fried Chicken":15000,
# 	"Burger Queen":25000,
# 	"French Fries":10000,
# 	"Jasmine Tea":5000,
# 	"Ice Coca-cola":12000
# }
# print("=============================Daftar Menu==============================")
# for i in menu:
# 	print("Daftar Menu:", i, "\t Harga:", menu[i])
# print("Pembelian di atas Rp.100.000, mendapatkan diskon 15%")
# print("=======================================================================")
# beli=input("Pilih Menu:")
# jumlah=int(input("Jumlah Pesanan:"))
# bayar=jumlah * menu[beli]

# if bayar > 100000:
# 	diskon=bayar*15/100
# 	total=bayar-diskon
# else:
# 	total=bayar

# print("==========================Detail Pembayaran==============================")
# print("Menu yang dipesan        :", beli)
# print("Jumlah yang dipesan      :", jumlah)
# print("Total Biaya              :", bayar)
# print("Total yang harus dibayar :", total)

import os
# import subprocess
# result=subprocess.run(["wc -l .zshrc"], text=True, capture_output=True)
# print(result.stdout)
class Command:
	def __init__(self, cmd):
		self.cmd=cmd

	def __str__(self):
		command=os.popen(self.cmd)
		read=command.read()

		# if read == "/usr/bin/zsh":
		return f"Shell ini menggunakan termninal {read}"
		# return f"{read}"

cmd=Command("echo $SHELL")
 
print(type(cmd)) 
if cmd == "/usr/bin/zsh":
	print("ZSH")