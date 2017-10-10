import MySQLdb
import mysql.connector

# connect to MySQL database
con = mysql.connector.connect(user='sw2proj',password='password',host='localhost',database='sw2projdb')
cur = con.cursor()

class InfoFromDatabase:

    def __init__(self):
        # don't know if this is necessary, but it'll stay here in case it is
        pass

    def getSubject(self, idPreference, idWorkOrder):
        # pull from Db
        # hall, room number, description
        subject1 = cur.execute("""SELECT resHall FROM 'Preference' WHERE idPreference = '{}'""").format(idPreference)
        subject2 = cur.execute("""SELECT roomNumber FROM 'Preference' WHERE idPreference = '{}'""").format(idPreference)
        subject3 = cur.execute("""SELECT Description FROM 'Work Order' WHERE idWorkOrder = '{}'""").format(idWorkOrder)
        subject = subject1 + subject2 + subject3
        return subject

    def getFromAddr(self, idPreference):
        # pull from Db
        # first time would be user, second would be RA, third would be RD
        fromAddr = cur.execute("""SELECT userEmail FROM 'Preference' WHERE idPreference = '{}'""").format(idPreference)
        return fromAddr

    def getToAddr(self, emailForSend, idPreference):
        # pull from Db
        # first would be to RA, then RD, then FS
        toAddr = cur.execute("""SELECT {} FROM 'Preference' WHERE idPreference = '{}'""").format(emailForSend, idPreference)
        return toAddr

    def getMsg(self, idWorkOrder):
        # pull from Db
        # random message?
        msg = "Thank you!"
        return msg