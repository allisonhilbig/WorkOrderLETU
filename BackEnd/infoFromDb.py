import MySQLdb
import mysql.connector

# connect to MySQL database
con = mysql.connector.connect(user='sw2proj',password='password',host='cs-lab.letu.edu',database='sw2projdb')
cur = con.cursor()

class InfoFromDatabase:

    def __init__(self):
        # don't know if this is necessary, but it'll stay here in case it is
        pass

    def getMsg(self):
        # pull from Db
        # this is currently filler
        msg = "This prototype works."
        #cur.execute("""select * from pytable""") <--- example for syntax
        #msg = cur.fetch__ idk
        return msg

    def getFromAddr(self):
        # pull from Db
        # first time would be user, second would be RA, third would be RD

        return fromAddr

    def getToAddr(self):
        # pull from Db
        # first would be to RA, then RD, then FS

        return toAddr

    def getSubject(self):
        # pull from Db
        # hall, room number, description

        return subject