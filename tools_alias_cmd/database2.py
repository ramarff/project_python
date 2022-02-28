import MySQLdb as mysql
import hashlib
import sys
import warnings

class Database:
    # initialization Connection Database
    # Init Start
    warnings.filterwarnings('error')

    def __init__(self, DBrootHost, DBrootUser, DBrootPass, DBrootDatabase):
        self.DBrootHost = DBrootHost
        self.DBrootUser = DBrootUser
        self.DBrootPass = DBrootPass
        self.DBrootDatabase = DBrootDatabase

        try:
            self.connection = mysql.connect(DBrootHost, DBrootUser, DBrootPass, DBrootDatabase)
            self.cursor = self.connection.cursor()
        except Warning as warn:
            print("Warning", warn)

    def CreateDB(self, DBrootDatabase):
        print("Creating database...")
        try:
            self.cursor.execute('CREATE database if NOT exists ' + DBrootDatabase)
            self.cursor.execute("SHOW DATABASES LIKE %s", (DBrootDatabase,))
            dbs = self.cursor.fetchone()
            print("Database created: ", dbs[0])
        except Warning as warn:
            print("Warning: %s \nStopping Process.\n" % warn)
            sys.exit()

    def GrantsAccess(self, DBrootDatabase):
        print("Accessing Account ...")
        try:
            self.cursor.execute("SHOW DATABASES LIKE %s", (DBrootDatabase,))
            result = self.cursor.fetchone()
            print("Access Granted for Database", result[0])
        except Warning as warn:
            print("Warningg %s" % warn)

    def getDB(self):
        return self.cursor
        
    def conn(self):
        return self.connection 

    def delCon(self):
        print("Finishing operation ...")
        self.cursor.close()
        self.con.close()
        print("Finished")