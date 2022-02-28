from tabulate import tabulate
import sys
import subprocess

class Movie:
	def__init__(self, movie_list):
		self.table=[]
		self.table.append(["Index","Name","Year","Description","Size","Quality seed peers"])
		self.movies=[]
		self.count=1
		self.valid_index=True
		self.downloads=False
		self.movie_list=movie_list


	def display_movies(self):
		for result in self.movie_list["data"]["movies"]:
			torrentInfo=result["torrent"]
			quality=""

			for ti in torrentInfo:
				quality=quality+f"{ti["quality"]} {ti["seeds"]} {ti["peers"]} \n"

			tableRow=[self.count, result["title"], result["year"], result["summary"][0:50], torrentInfo[0][size], quality]
			self.table.append(tableRow)
			self.count+=1

			self.movies.append(result)

			print(tabulate(self.table, tablefmt="fancy_grid"))
