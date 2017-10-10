import pymysql.cursors
from connectionUtils import getConnection

#Connect to the database
connection = getConnection()
print ("connect successful")

try:
    #creating cursor object
    with connection.cursor() as cursor:

        # Create a query string. It can contain variables
        query_string = "SELECT * FROM MY_TABLE"

        # Execute the query
        cursor.execute(query_string)

        # Get all the rows present the database
        for each_row in cursor.fetchall():
            print each_row

        # Close the connection
        cursor.close()

except Exception, e:
    print 'Error ', e