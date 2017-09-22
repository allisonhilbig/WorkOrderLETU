from socket import *
from infoFromDb import InfoFromDatabase

class SMTP:

    endmsg = "\r\n.\r\n"
    info = InfoFromDatabase()

    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = ("smtp.letu.edu", 25)
    #  Create socket called clientSocket and establish a TCP connection with mailserver
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)

    recv = clientSocket.recv(1024)
    print recv
    if recv[:3] != '220':
        print '220 reply not received from server.'

    # Write message
    def writeMsg(self, message):
        msg = "\r\n" + SMTP.info.getMsg()
        return msg

    # Send HELO command and print server response.
    def sendHeloCmd(self):
        heloCommand = 'HELO Alice\r\n'
        SMTP.clientSocket.send(heloCommand)
        recv1 = SMTP.clientSocket.recv(1024)
        print recv1
        if recv1[:3] != '250':
            print '250 reply not received from server.'

    # Send MAIL FROM command and print server response.
    def mailFromCmd(self, fromAddr):
        mailFromCmd = 'MAIL FROM: {}\r\n'.format(SMTP.info.getFromAddr())
        SMTP.clientSocket.send(mailFromCmd)
        recv2 = SMTP.clientSocket.recv(1024)
        print recv2
        if recv2[:3] != '250':
            print '250 reply not received from server.'

    # Send RCPT TO command and print server response.
    def rcptToCmd(self, toAddr):
        rcptToCmd = 'RCPT TO: {}\r\n'.format(SMTP.info.getToAddr())
        SMTP.clientSocket.send(rcptToCmd)
        recv3 = SMTP.clientSocket.recv(1024)
        print recv3
        if recv3[:3] != '250':
            print '250 reply not received from server.'

    # Send DATA command and print server response.
    def sendDataCmd(self):
        dataCmd = 'DATA\r\n'
        SMTP.clientSocket.send(dataCmd)
        recv4 = SMTP.clientSocket.recv(1024)
        print recv4
        if recv4[:3] != '250':
            print '250 reply not received from server.'

    # add subject
    def addSubjectCmd(self, subject):
        subjectCommand = "SUBJECT: {}\r\n\n".format(SMTP.info.getSubject())
        print subjectCommand
        SMTP.clientSocket.send(subjectCommand)

    def run(self, message, fromAddr, toAddr, subject):
        # self.writeMsg(message)
        self.sendHeloCmd()
        self.mailFromCmd(fromAddr)
        self.rcptToCmd(toAddr)
        self.sendDataCmd()
        self.addSubjectCmd(subject)

        # Send message data.
        SMTP.clientSocket.send(self.writeMsg(message))

        # Message ends with a single period.
        SMTP.clientSocket.send(SMTP.endmsg)

        # Send QUIT command and get server response.
        quitCmd = 'QUIT\r\n'
        SMTP.clientSocket.send(quitCmd)
        recv5 = SMTP.clientSocket.recv(1024)
        print recv5
        if recv5[:3] != '250':
            print '250 reply not received from server.'

if __name__ == "__main__":
    SMTP.run(SMTP.info.getMsg(), SMTP.info.getFromAddr(), SMTP.info.getToAddr(), SMTP.info.getSubject())
