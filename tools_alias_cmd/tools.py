import typer
import os
from rich.table import Table
from rich.console import Console
from model import Command
from shell import Shell
from action import Action
from validations import Validations
console=Console()
app=typer.Typer()

db=Action("localhost","root","KOPIHITAM645","db_cmd")
sh=Shell()
validation=Validations()

# print("ok")
@app.command(short_help="Untuk melihat data")
def tampil():
	lists=db.show_data()
	console.print("[bold magenta]Daftar command[/bold magenta]!","💻️")
	table=Table(show_header=True, header_style="bold blue")
	table.add_column("No", style="dim", width=6, justify="center")
	table.add_column("command", min_width=20, justify="center")
	table.add_column("isi command", min_width=12, justify="center")
	table.add_column("deskripsi", min_width=12, justify="center")
	if len(lists) > 0 :
		for i, list in enumerate(lists, start=1):
			table.add_row(str(i), list.cmd, list.isi_cmd, list.deskripsi)
	else:
		table.add_row("-","-","-","-")
	console.print(table)

@app.command(short_help="Untuk menambahkan data")
def tambah(cmd:str=None, isi_cmd:str=None, deskripsi:str=None):
	letak_baris=sh.letakBaris()
	if validation.add(cmd, isi_cmd, deskripsi) != False:
		command=Command(None, cmd, isi_cmd, deskripsi, letak_baris+1, None)
		db.add_data(command)
		sh.add(cmd, isi_cmd)
		tampil()

@app.command(short_help="Untuk menghapus data")
def hapus(nomor:int=typer.Argument(None)):
	letakBaris=db.column("letak_baris", nomor)
	cmd=db.column("cmd", nomor)
	if validation.delete(nomor, cmd) != False:
		db.delete_data(int(nomor))
		sh.delete(letakBaris)	
		tampil()

@app.command(short_help="Untuk mengubah data")
def ubah(nomor:int, cmd:str=None, isi_cmd:str=None, deskripsi:str=None):
	command=db.column("cmd", int(nomor))
	db.update_data(nomor, cmd, isi_cmd, deskripsi)
	sh.update(nomor, cmd, isi_cmd)
	console.print(f"Mengubah data command ${command}.", style="bold green")

if __name__=="__main__":
	app()
