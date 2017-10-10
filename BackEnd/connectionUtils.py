import pymysql.cursors


# Function return a connection.
def getConnection():
    #define connection, I can add you as a user or just change this
    connection = pymysql.connect(host = 'cs-lab.letnet.net/phpmyadmin',
                                 user = 'sw2proj',
                                 password = 'password',
                                 db = 'sw2projdb',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor
                                 )
    return connection