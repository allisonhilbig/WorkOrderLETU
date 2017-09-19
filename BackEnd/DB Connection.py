import pymysql.cursors

#Connect to the database
connection = pymysql.connect(host = '127.0.0.1:3306', user = 'annjones', password = 'password',
                             db = 'WOLetu', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor
                             )
