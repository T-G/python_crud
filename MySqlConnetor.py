# Create MySQL connection

# import MySQL Connector
import mysql.connector

# import connection credentials from Connection file
from Credentials import mysql_host, mysql_user, mysql_password


# define a connection function
def connect_to_mysql(host = mysql_host, user = mysql_user, password = mysql_password, database='heroes'):
    connection = None

    try:
        # start the connection
        connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
        print("Successfully connected to MySQL Server.")

    except mysql.connector.Error as e:
        print(f'An error occured: {e}')
    #else:
    # conn.close()
    return connection

# call the function and get connection
#connect_to_mysql()