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
        subjectHall = str(cur.execute("""SELECT resHall FROM 'Preference' WHERE idPreference = '{}'""").format(idPreference))
        subjectRN = str(cur.execute("""SELECT roomNumber FROM 'Preference' WHERE idPreference = '{}'""").format(idPreference))
        subjectDesc = str(cur.execute("""SELECT Description FROM 'Work Order' WHERE idWorkOrder = '{}'""").format(idWorkOrder))
        subject = subjectHall + subjectRN + subjectDesc
        return subject

    def getFromAddr(self, idPreference):
        # pull from Db
        # first time would be user, second would be RA, third would be RD
        fromAddr = str(cur.execute("""SELECT userEmail FROM 'Preference' WHERE idPreference = '{}'""").format(idPreference))
        return fromAddr

    def getToAddr(self, emailForSend, idPreference):
        # pull from Db
        # first would be to RA, then RD, then FS
        toAddr = str(cur.execute("""SELECT {} FROM 'Preference' WHERE idPreference = '{}'""").format(emailForSend, idPreference))
        return toAddr

    def getMsg(self, idWorkOrder):
        # pull from Db
        # random message?
        msg = "Thank you!"
        return msg