from rich.console import Console
from action import Action
console=Console()

action=Action("localhost", "root","KOPIHITAM645","db_cmd")
class Validations:

	def add(self, cmd, isi_cmd, deskripsi):
		if cmd is None and isi_cmd is None and deskripsi is None:
			console.print(f"Paramater cmd, isi-cmd, dan deskripsi tidak ada!.", style="bold red")
			console.print(f"Tambahkan parameter --cmd='<command>', --isi-cmd='<isi cmd>', --deskripsi='<deskripsi>'.", style="bold")
			console.print(f"Contoh python3 tools.py --cmd='py' --isi-cmd='cd ~/Documents/python' --deskripsi='untuk membuka folder project python'", style="bold")
			return False
		elif isi_cmd is None and deskripsi is None:
			console.print(f"Parameter isi-cmd dan deskripsi tidak ada!", style="bold red")
			console.print(f"Tambahkan parameter --isi-cmd='<isi cmd>' dan --deskripsi='<deskripsi>'", style="bold")
			console.print(f"Contoh --isi-cmd='ls -la' --deskripsi='untuk melihat isi dari file/folder'", style="bold")
			return False
		elif cmd is None and deskripsi is None:
			console.print(f"Parameter cmd dan deskripsi tidak ada!", style="bold red")
			console.print(f"Tambahkan parameter --cmd='<command>' dan --deskripsi='<deskripsi>'", style="bold")
			console.print(f"Contoh --cmd='ls' --deskripsi='untuk melihat isi dari file/folder'", style="bold")
			return False
		elif cmd is None and isi_cmd is None:
			console.print(f"Parameter cmd dan isi-cmd tidak ada!", style="bold red")
			console.print(f"Tambahkan parameter --cmd='<command>' dan --isi-cmd='<isi cmd>'", style="bold")
			console.print(f"Contoh --cmd='ls' --isi-cmd='ls -la'", style="bold")
			return False
		elif cmd is None:
			console.print(f"parameter cmd tidak ada!", style="bold red")
			console.print(f"Tambahkan parameter --cmd='<command>'", style="bold")
			console.print(f"Contoh --cmd='ls'", style="bold")
			return False
		elif isi_cmd is None:
			console.print(f"Parameter isi-cmd tidak ada!", style="bold red")
			console.print(f"Tambahkan parameter --isi-cmd='<isi command>'", style="bold")
			console.print(f"Contoh --isi-cmd='ls -la'", style="bold")	
			return False
		elif deskripsi is None:
			console.print(f"Parameter deskripsi tidak ada!", style="bold red")
			console.print(f"Tambahkan parameter --deskripsi='<deskripsi>'", style="bold")
			console.print(f"Contoh  --deskripsi='untuk melihat isi dari file/folder'", style="bold")	
			return False
		else:
			console.print(f"Menambahkan command ${cmd}.", style="bold green")


	def delete(self, posisi, cmd):
		posisi_db=action.column("posisi", posisi)	
		if posisi is None:
			console.print(f"Parameter nomor tidak ada!", style="bold red")
			console.print(f"Tambahkan parameter delete <nomor> yang tertera pada table")
			console.print(f"Contoh: delete 3")
			return False
		elif posisi_db is False:
			console.print(f"Tidak ada nomor {posisi} di dalam table!.", style="bold red")
			return False
		else:
			console.print(f"Menghapus command {cmd}.", style="bold green")

validations=Validations()
# validations.delete("2","ms")


