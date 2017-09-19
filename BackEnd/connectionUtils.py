import pymysql.cursors


# Function return a connection.
def getConnection():
    #define connection, I can add you as a user or just change this
    connection = pymysql.connect(host = 'cs-lab.letu.edu:3306',
                                 user = 'annjones',
                                 password = 'password',
                                 db = 'WOLetu',
                                 charset = 'utf8mb4',
                                 cursorclass = pymysql.cursors.DictCursor
                                 )
    return connection