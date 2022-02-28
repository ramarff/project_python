class Command:
	def __init__(self, id_cmd, cmd, isi_cmd, deskripsi, letak_baris, posisi):
		self.id_cmd=id_cmd if id_cmd is not None else None
		self.cmd=cmd
		self.isi_cmd=isi_cmd
		self.deskripsi=deskripsi
		self.letak_baris=letak_baris
		self.posisi=posisi if posisi is not None else None

	def __repr__(self) -> str:
		return f"{self.id_cmd}, {self.cmd}, {self.isi_cmd}, {self.deskripsi}, {self.letak_baris}, {self.posisi}"