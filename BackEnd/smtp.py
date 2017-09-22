from socket import *
import infoFromDb

class SMTP:

    endmsg = "\r\n.\r\n"
    info = InfoFromDb()

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
        msg = "\r\n" + info.getMsg()
        return msg

    # Send HELO command and print server response.
    def sendHeloCmd(self):
        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand)
        recv1 = clientSocket.recv(1024)
        print recv1
        if recv1[:3] != '250':
            print '250 reply not received from server.'

    # Send MAIL FROM command and print server response.
    def mailFromCmd(self, fromAddr):
        mailFromCmd = 'MAIL FROM: TheBestestPerson@ever.com\r\n'
        clientSocket.send(mailFromCmd)
        recv2 = clientSocket.recv(1024)
        print recv2
        if recv2[:3] != '250':
            print '250 reply not received from server.'

    # Send RCPT TO command and print server response.
    def rcptToCmd(self, toAddr):
        rcptToCmd = 'RCPT TO: 24ponygirl@gmail.com\r\n'
        clientSocket.send(rcptToCmd)
        recv3 = clientSocket.recv(1024)
        print recv3
        if recv3[:3] != '250':
            print '250 reply not received from server.'

    # Send DATA command and print server response.
    def sendDataCmd(self):
        dataCmd = 'DATA\r\n'
        clientSocket.send(dataCmd)
        recv4 = clientSocket.recv(1024)
        print recv4
        if recv4[:3] != '250':
            print '250 reply not received from server.'

    # add subject
    def addSubjectCmd(self, subject):
        subjectCommand = "SUBJECT: hi \r\n\n"
        print subjectCommand
        clientSocket.send(subjectCommand)

    def run(self, message, fromAddr, toAddr, subject):
        self.writeMsg(message)
        self.sendHeloCmd()
        self.mailFromCmd(fromAddr)
        self.rcptToCmd(toAddr)
        self.sendDataCmd()
        self.addSubjectCmd(subject)

        # Send message data.
        clientSocket.send(msg)

        # Message ends with a single period.
        clientSocket.send(endmsg)

        # Send QUIT command and get server response.
        quitCmd = 'QUIT\r\n'
        clientSocket.send(quitCmd)
        recv5 = clientSocket.recv(1024)
        print recv5
        if recv5[:3] != '250':
            print '250 reply not received from server.'