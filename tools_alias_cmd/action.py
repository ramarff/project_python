from database2 import Database
from typing import List
from model import Command
import MySQLdb as mysql


class Action(Database):
    def __init__(self, DBrootHost, DBrootUser, DBrootPass, DBrootDatabase):
        super().__init__(DBrootHost, DBrootUser, DBrootPass, DBrootDatabase)
        self.db=super().getDB()
        self.conn=super().conn()

    def show_data(self) -> List[Command]:
        sql="SELECT * FROM table_cmd"
        lists=[]
        # print(count)
        try:
            self.db.execute(sql)
            results=self.db.fetchall()
            # print(results)
            for result in results:
                lists.append(Command(result[0],result[1], result[2], result[3], result[4], result[5]))
            return lists
        except mysql.Error as Error:
            print(f"error:{Error}")

    def add_data(self, Command):
        self.db.execute("SELECT COUNT(*) FROM table_cmd")
        count=self.db.fetchone()[0]
        # print(count)
        Command.posisi=count+1 if count else 1 
        sql="INSERT INTO table_cmd  VALUES (NULL, '%s', '%s', '%s', %d, %d)" % (Command.cmd, Command.isi_cmd, Command.deskripsi, Command.letak_baris, Command.posisi)
        try:
            self.db.execute(sql)
            self.conn.commit()
        except mysql.Error as Error:
            print(f"error:{Error}")

    def delete_data(self, position):
        self.db.execute("SELECT COUNT(*) FROM table_cmd")
        count=self.db.fetchone()[0]
        sql="DELETE FROM table_cmd WHERE posisi=%d" % (position)
        try:
            self.db.execute(sql)
            self.conn.commit()
            for pos in range(position+1, count):
                db.change_position(pos, pos-1)
        except mysql.Error as Error:
            print(f"error:{Error}")


    def update_data(self, posisi, cmd, isi_cmd, deskripsi):
        if cmd is not None:
            sql=f"UPDATE table_cmd SET cmd='{cmd}' WHERE posisi={posisi}"
            try:
                self.db.execute(sql)
                self.conn.commit()
            except mysql.Error as Error:
                print(f"error:{Error}")
        elif isi_cmd is not None:
            sql=f"UPDATE table_cmd SET isi_cmd='{isi_cmd}'WHERE posisi={posisi}"
            try:
                self.db.execute(sql)
                self.conn.commit()
            except mysql.Error as Error:
                print(f"error:{Error}")
        elif deskripsi is not None:
            sql=f"UPDATE table_cmd SET deskripsi='{deskripsi}' WHERE posisi={posisi}"
            print(sql)
            try:
                self.db.execute(sql)
                self.conn.commit()
            except mysql.Error as Error:
                print(f"error:{Error}")
        elif cmd is not None and isi_cmd is not None:
            sql=f"UPDATE table_cmd SET cmd='{cmd}', isi_cmd='{isi_cmd}' WHERE posisi={posisi}"
            try:
                self.db.execute(sql)
                self.conn.commit()
            except mysql.Error as Error:
                print(f"error:{Error}")
        elif cmd is not None and deskripsi is not None:
            sql=f"UPDATE table_cmd SET cmd='{cmd}', deskripsi='{deskripsi}' WHERE posisi={posisi}"
            try:
                self.db.execute(sql)
                self.conn.commit()
            except mysql.Error as Error:
                print(f"error:{Error}")
        elif cmd is not None and isi_cmd is not None and deskripsi is not None:
            sql=f"UPDATE table_cmd SET cmd='{cmd}', isi_cmd='{isi_cmd}', deskripsi='{deskripsi}' WHERE posisi={posisi}"
            try:
                self.db.execute(sql)
                self.conn.commit()
            except mysql.Error as Error:
                print(f"error:{Error}")


    def change_position(self, old_position, new_position):
        sql="UPDATE table_cmd SET posisi=%d WHERE posisi=%d " % (new_position, old_position)
        try:
            self.db.execute(sql)
            self.conn.commit()
        except mysql.Error as Error:
            print(f"error:{Error}")

    def column(self, column, position):
      if column == "cmd":
        sql="SELECT cmd FROM table_cmd WHERE posisi=%d" % (position)
        try:
            self.db.execute(sql)
            result=self.db.fetchone()
            return result[0] if result is not None else False
        except mysql.Error as Error:
            print(f"error:{Error}")
      elif column == "isi_cmd":
        sql="SELECT isi_cmd FROM table_cmd WHERE posisi=%d" % (position)
        try:
            self.db.execute(sql)
            result=self.db.fetchone()
            return result[0] if result is not None else False
        except mysql.Error as Error:
            print(f"error:{Error}")
      elif column == "deskripsi":
        sql="SELECT deskripsi FROM table_cmd WHERE posisi=%d" % (position)
        try:
            self.db.execute(sql)
            result=self.db.fetchone()
            return result[0] if result is not None else False
        except mysql.Error as Error:
            print(f"error:{Error}")
      elif column == "letak_baris":
        sql="SELECT letak_baris FROM table_cmd WHERE posisi=%d" % (position)
        try:
            self.db.execute(sql)
            result=self.db.fetchone()
            return result[0] if result is not None else False
        except mysql.Error as Error:
            print(f"error:{Error}")
      elif column == "posisi":
        # print(posisi)
        sql="SELECT posisi FROM table_cmd WHERE posisi=%d" % (position)
        # print(sql)
        try:
            self.db.execute(sql)
            result=self.db.fetchone()
            return result[0] if result is not None else False
        except mysql.Error as Error:
            print(f"error:{Error}")

db=Action("localhost","root","KOPIHITAM645","db_cmd")
data=Command(None,"ls","ls-la","deskripsi",120, None)
# db.add_data(data)

