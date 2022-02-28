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
		return request.get(url=f"{self.base_url}{query}")

class List_menu():
	def hot_song(self):
		song=Fetch()
		data_lagu=song.hot_song_url("hot")
		# print(data_lagu)
		page=10
		list_lagu={'No':[],'Nama Artist':[],'Judul Lagu':[]}
		for i in range(len(data_lagu)):
			# list_lagu.append(data_lagu['data'][i]['artist'])
			# list_lagu.append(data_lagu['data'][i]['songTitle'])
			# objek_lagu={"artist":None,"judul_lagu":None}
			# objek_lagu["artist"]=data_lagu['data'][i]['artist']
			# objek_lagu["judul_lagu"]=data_lagu['data'][i]['songTitle']
			list_lagu['No'].append(i+1)
			list_lagu['Nama Artist'].append(data_lagu['data'][i]['artist'])
			list_lagu['Judul Lagu'].append(data_lagu['data'][i]['artist'])
			# list_lagu.append(objek_lagu)
		# return print(type(list_lagu))
		return print(tabulate(list_lagu, headers="keys",  tablefmt="fancy_grid", colalign=("center","center")))

	def lyrics(self):
		print("ok")
	
	def search(self):
		print("ok")


class Main():
	# def __init__(self):

	def show_menu(self, menu):
	  for i in range(len(menu)):
	    print(f"[{i+1}] {menu[i]}")

	def input_menu(self):
	    list=List_menu()
	    menu=input("Pilih Menu:")
	    if menu == '1':
	    	list.hot_song()
	    elif menu == '2':
	    	list.lyrics()
	    elif menu == '3':
	    	list.search()
	    elif menu == '4':
	    	exit()
	    else:
	    	print("Input salah")
main=Main()
cmd="clear"
print(f"{title_art}Author:{info.get('author')} | Source Code : {info.get('github')} | API : {info.get('API')}")
main.show_menu(["Hot Song","Lyrics","Search Song","Exit"])
main.input_menu()
# if __name__== "__main__":
# 	state=True
# 	while(state):
		# main.show_menu(["Hot Song","Lyrics","Search Song","Exit"])
# 		state=False
# 		main.input_menu()
		# print(menu)
		# os.system(cmd)


# main.input_menu()





# def main():
# 	search_result=True
# 	movie_list=None
# 	print("Enter the move name\n")
# 	while search_result:
# 		movie_name=input(" ")
# 		print(f"Searching for {movie_name} \n")
# 		movie=Fetch()
# 		movie_list=movie.fetch_data(f"list_movies.json?query_term={movie_name}")
# 		print(movie_list)
# 		if movie_list["data"]["movie_count"] >= 1:
# 			search_result=False
# 		else:
# 			print("Movie not found. Please try with different movie name \n")

# main()
