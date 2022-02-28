# from fetch import Fetch
from tabulate import tabulate
import json
import os
from urllib import request
title_art=r"""
##########################################################################
#                                .__                .__                  #
#    __________   ____    ____   |  | ___.__._______|__| ____   ______   #
#   /  ___/  _ \ /    \  / ___\  |  |<   |  |\_  __ \  |/ ___\ /  ___/   #
#   \___ (  <_> )   |  \/ /_/  > |  |_\___  | |  | \/  \  \___ \___ \    #
#  /____  >____/|___|  /\___  /  |____/ ____| |__|  |__|\___  >____  >   #
#       \/           \//_____/        \/                    \/     \/    #                                                         
##########################################################################                                                                    
"""
info={
	"author":"Rama Fajar Fadhillah",
	"github":"https://github.com/ramarff",
	"API":"https://api-song-lyrics.herokuapp.com/"

}
# print() 
class Fetch:
	def __init__(self):
		self.base_url="https://api-song-lyrics.herokuapp.com"
		# self.hot_url=hot_url

	def hot_song_url(self, hot_url):
		response=request.urlopen(f"{self.base_url}/{hot_url}")
		data_lagu=json.loads(response.read())
		return data_lagu
	# def lyrics():

	def search_song_url(self, query):
		response=request.urlopen(f"{self.base_url}/search?q={query}")
		data_lagu=json.loads(response.read())
		return data_lagu
		# return request.get(url=f"{self.base_url}{query}")

class List_menu():
	def __init__(self):
		self.song=Fetch()
		# self.awal=0
		# self.akhir=0
		self.pagination=[]
	def hot_song(self, rev, awal, akhir):
		data_lagu=self.song.hot_song_url("hot")
		# print(data_lagu)
		# page=20
		self.pagination.append(awal)
		self.pagination.append(akhir)
		# self.akhir=akhir
		# print(awal)
		# print(akhir)
		print(self.pagination)
		list_lagu={'No':[],'Nama Artist':[],'Judul Lagu':[]}
		for i in range(self.pagination[0], self.pagination[1]):
			list_lagu['No'].append(i+1)
			list_lagu['Nama Artist'].append(data_lagu['data'][i]['artist'])
			list_lagu['Judul Lagu'].append(data_lagu['data'][i]['songTitle'])
		list_lagu['No'].sort(reverse=rev)
		list_lagu['Nama Artist'].sort(reverse=rev)
		list_lagu['Judul Lagu'].sort(reverse=rev)

		print(tabulate(list_lagu, headers="keys",  tablefmt="fancy_grid", colalign=("center","center")))
		main.show_menu('menuSatu')
		main.input_menu('inputSatu')

	def lyrics(self):
		print("ok")
	
	def search_song(self, song):
		hasil_pencarian=self.song.search_song_url(song)


class Main():
	# def __init__(self):


	def show_menu(self, menu):
	  if menu == 'menu_utama':
	     daftar_menu=["Hot Song","Lyrics","Search Song","Exit"]
	     for i in range(len(daftar_menu)):
	     	print(f"{[i+1]} {daftar_menu[i]}")
	  elif menu == 'menuSatu':
	     daftar_menu=["Data selanjutanya","Data sebelumnya","urutan:asc/desc?","Balik ke menu sebelumnya"]
	     for i in range(len(daftar_menu)):
	     	print(f"{[i+1]} {daftar_menu[i]}")
	  elif menu == 'menuSort':
	  	daftar_menu=["ASC:Dari kecil ke besar","DESC:Dari besar ke kecil","B:Batal"]
	  	for i in range(len(daftar_menu)):
	  		print(f"{daftar_menu[i]}")
	def input_menu(self, input_menu):
		list=List_menu()
		if input_menu == 'input_utama':
			menu=input("Pilih menu:")
			if menu == '1':
				# print(list.awal)
				list.hot_song(False, 0, 10)
			elif menu == '2':
				print("ok")
			elif menu == '3':
				menu=input("Masukkan judul lagu:")
			elif menu == '4':
				print("Terimakasih telah menggunakan program python saya ^_^")
				print("Silahkan Follow ig saya xixi (@ramarff)")
				exit()
			else:
				# os.system(cmd)				
				print("Input salah!")
				print(f"{title_art}Author:{info.get('author')} | Source Code : {info.get('github')} | API : {info.get('API')}")
				main.show_menu('menu_utama')
				main.input_menu('input_utama')
		elif input_menu == 'inputSatu':
			menu=input("Pilih menu:")
			if menu == '1':
				# print("ok")
				while(True):
					list.hot_song(False, 10, 20)
				# list.pagination[0]=20
				# list_pagination[1]=30
			elif menu == '2':
				print("ok")
			elif menu == '3':
				main.show_menu("menuSort")
				main.input_menu('inputSort')
				# print("ok")
				# print(menu.lower())
			elif menu == '4':
				main.show_menu("menu_utama")
				main.input_menu("input_utama")
			else:
				print("Input salah!")
		elif input_menu == 'inputSort':
				menu=input("ASC/DESC/B?")
				if menu.lower() == 'asc':
					list.hot_song(False)
				elif menu.lower() == 'desc':
					list.hot_song(True)
				elif menu.lower() == 'b':
					main.show_menu('menuSatu')
					main.input_menu('inputSatu')
				else:
					print("Input salah !")
					main.show_menu("menuSort")
					main.input_menu("inputSort")



main=Main()
cmd="clear"
print(f"{title_art}Author:{info.get('author')} | Source Code : {info.get('github')} | API : {info.get('API')}")
main.show_menu('menu_utama')
main.input_menu('input_utama')
# if __name__== "__main__":
# 	state=True
# 	while(state):
		# main.show_menu(["Hot Song","Lyrics","Search Song","Exit"])
# 		state=False	
# 		main.input_menu()
		# print(menu)
		# os.system(cmd)


# main.input_menu()
