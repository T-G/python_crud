import mysql.connector

from MySqlConnetor import connect_to_mysql

def print_databases():
    try:
        # connect to server
        connection = connect_to_mysql()
        if connection is not None:
            # set the cursor
            cursor = connection.cursor()
            cursor.execute('SHOW DATABASES')

            # PRINT DB
            for db in cursor:
                print(db)
    except mysql.connector.Error as e:
        print(f'An Error occured:\n{e}')
    else:
        if connection is not None:
            # close the cursor and connection
            cursor.close()
            connection.close()

print_databases()