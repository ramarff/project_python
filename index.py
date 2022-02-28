# from fetch import Fetch
from tabulate import tabulate
import json
import os
import math
from urllib import request
import  animation
import time

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

tags = ["Data sedang dimuat",".","..","...","....",".....","......",".......","........",".........","..........","...........","............",".............","..............","...............","................",".................",".................."]
animation = animation.Wait(tags, color="white", speed=0.1)

class List_menu():
	def __init__(self):
		self.song=Fetch()
		
	def hot_song(self, rev):
		data_lagu=self.song.hot_song_url("hot")
		dataPerhalaman=10
		# jumlahData=len(data_lagu['data'])
		# jumlahHalaman=math.ceil(jumlahData / dataPerhalaman)
		# halamanAktif=1
		# awalData=(dataPerhalaman * halamanAktif) - dataPerhalaman
		list_lagu={'No':[],'Nama Artist':[],'Judul Lagu':[]}
		for i in range(0,10):
			list_lagu['No'].append(i+1)
			list_lagu['Nama Artist'].append(data_lagu['data'][i]['artist'])
			list_lagu['Judul Lagu'].append(data_lagu['data'][i]['songTitle'])
		list_lagu['No'].sort(reverse=rev)
		list_lagu['Nama Artist'].sort(reverse=rev)
		list_lagu['Judul Lagu'].sort(reverse=rev)
		# print(len(list_lagu['No']))
		animation.start()
		time.sleep(10)
		if len(data_lagu['data']) > 0 :
			animation.stop()
		print(tabulate(list_lagu, headers="keys",  tablefmt="fancy_grid", colalign=("center","center")))
		main.show_menu('menuSatu')
		main.input_menu('inputSatu')

	def lyrics(self):
		print("ok")
	
	def search_song(self, song):
		hasil_pencarian=self.song.search_song_url(song)
		list_lagu={'No':[],'Nama Artist':[],'Judul Lagu':[]}
		for i in range(len(hasil_pencarian['data'])):
			list_lagu["No"].append(i+1)
			list_lagu["Nama Artist"].append(hasil_pencarian['data'][i]['artist'])			
			list_lagu["Judul Lagu"].append(hasil_pencarian['data'][i]['songTitle'])
		animation.start()
		time.sleep(10)
		if len(hasil_pencarian['data']) > 0 :	
			animation.stop()
			print(tabulate(list_lagu, headers="keys",  tablefmt="fancy_grid", colalign=("center","center")))
		else:
			animation.stop()
			print("[]==========DATA TIDAK ADA=============[]")
		main.show_menu("menuSearch")
		main.input_menu("inputSearch")




class Main():
	def show_menu(self, menu):
	  def daftar_menu(menu):
	  	for i in range(len(menu)):
	  		print(f"{[i+1]} {menu[i]}")
	  
	  if menu == 'menuUtama':
	  	daftar_menu(["Hot Song","Lyrics","Search Song","Exit"])
	  elif menu == 'menuSatu':
	  	daftar_menu(["Data selanjutanya","Data sebelumnya","urutan:asc/desc?","Balik ke menu sebelumnya"])
	  elif menu == 'menuSort':
	  	daftar_menu=["ASC:Dari kecil ke besar","DESC:Dari besar ke kecil","B:Batal"]
	  	for i in range(len(daftar_menu)):
	  		print(f"{daftar_menu[i]}")
	  elif menu == 'menuSearch':
	  	daftar_menu(["cari lagu","Batal"])

	def input_menu(self, input_menu):
		list=List_menu()
		if input_menu == 'input_utama':
			menu=input("Pilih menu:")
			if menu == '1':
				list.hot_song(False)
			elif menu == '2':
				print("ok")
			elif menu == '3':
				os.system("clear")
				print(f"{title_art}Author:{info.get('author')} | Source Code : {info.get('github')} | API : {info.get('API')}")
				main.show_menu("menuSearch")
				main.input_menu("inputSearch")
			elif menu == '4':
				print("Terimakasih telah menggunakan program python saya ^_^")
				print("Silahkan Follow ig saya xixi (@ramarff)")
				exit()
			else:
				print("Input salah!")
				print(f"{title_art}Author:{info.get('author')} | Source Code : {info.get('github')} | API : {info.get('API')}")
				main.show_menu('menuUtama')
				main.input_menu('input_utama')
		elif input_menu == 'inputSatu':
			menu=input("Pilih menu:")
			if menu == '1':
				list.hot_song(False)
			elif menu == '2':
				print("ok")
			elif menu == '3':
				main.show_menu("menuSort")
				main.input_menu('inputSort')
			elif menu == '4':
				os.system("clear")
				print(f"{title_art}Author:{info.get('author')} | Source Code : {info.get('github')} | API : {info.get('API')}")
				main.show_menu("menuUtama")
				main.input_menu("input_utama")
			else:
				print("Input salah!")
				main.show_menu("menuSatu")
				main.input_menu("inputSatu")
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
		elif input_menu == "inputSearch":
				menu=input("Pilih menu:")
				if menu == '1':
				  input_lagu=input("Masukkan judul lagu:")
				  judul_lagu=input_lagu.replace(" ","%20")
				  list.search_song(judul_lagu)
				elif menu == '2':
				  os.system("clear")
				  print(f"{title_art}Author:{info.get('author')} | Source Code : {info.get('github')} | API : {info.get('API')}")
				  main.show_menu("menuUtama")
				  main.input_menu("input_utama")



main=Main()
cmd="clear"
print(f"{title_art}Author:{info.get('author')} | Source Code : {info.get('github')} | API : {info.get('API')}")
main.show_menu('menuUtama')
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
