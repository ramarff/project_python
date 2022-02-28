import os
import subprocess
from action import Action

action=Action("localhost", "root","KOPIHITAM645","db_cmd")

class Shell:
	def shellName(self):
		result=subprocess.Popen("echo $SHELL", shell=True, stdout=subprocess.PIPE)
		with result as r:
			return str(r.stdout.read()).split("/")[3].replace("\\n'","")

	def fileConfig(self):
		shell=self.shellName()
		if shell == "zsh":
			return "~/.zshrc"
		elif shell == "bash":
			return ".bashrc"
		elif shell == "fish":
			return ".fzf.bash"
	
	def add(self, cmd, isi_cmd):
		file=self.fileConfig()
		shell=self.shellName()
		if shell == "zsh":
			os.system(f"printf 'alias {cmd}=\"{isi_cmd}\"\n' >> {file}")
		elif shell == "bash":
			os.system(f"printf 'alias {cmd}=\"{isi_cmd}\"\n' >> {file}")
		elif shell == "fish":
			os.system(f"printf 'alias {cmd}=\"{isi_cmd}\"\n' >> {file}")

	def letakBaris(self):
		file=self.fileConfig()
		shell=self.shellName()
		if shell == "zsh":
			result=subprocess.Popen(f"wc -l {file}", shell=True, stdout=subprocess.PIPE)
			with result as r:
				result=r.stdout.read()
				hasil=str(result)
				letakBaris=hasil.split("/")[0].replace("b'","")
			return int(letakBaris)
		elif shell == "fish":
			result=subprocess.Popen(f"wc -l {file}", shell=True, stdout=subprocess.PIPE)
			with result as r:
				result=r.stdout.read()
				hasil=str(result)
				letakBaris=hasil.split("/")[0].replace("b'","")
			return int(letakBaris)
		elif shell == "bash":
			result=subprocess.Popen(f"wc -l {file}", shell=True, stdout=subprocess.PIPE)
			with result as r:
				result=r.stdout.read()
				hasil=str(result)
				letakBaris=hasil.split("/")[0].replace("b'","")
			return int(letakBaris)

	def delete(self, letakBaris): 
		file=self.fileConfig()
		shell=self.shellName()
		if shell == "zsh":
			os.system(f"sed -i {letakBaris}d {file}")

	def update(self, position, cmd, isi_cmd):
		file=self.fileConfig()
		shell=self.shellName()
		cmdLama=action.column("cmd", position)
		print(cmdLama)
		isiCmdLama=action.column("isi_cmd", position)
		commandSatu=f"sed -i 's|alias {cmdLama}|alias {cmd}|' {file} && sed -i 's|{isiCmdLama}|{isi_cmd}|' {file}"
		commandDua=f"sed -i 's|alias {cmdLama}|alias {cmd}|' {file}"
		print(commandDua)
		commandTiga=f"sed -i 's|{isiCmdLama}|{isi_cmd}|' {file}"
		if cmd is not None and isi_cmd is not None:
				os.system(command)
		elif cmd is not None:
				os.system(commandDua)
		elif isi_cmd is not None:
				os.system(commandTiga)


shell=Shell()
# shell.delete(116)