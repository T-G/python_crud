# import connector
import mysql.connector

# import custom connection
from MySqlConnetor import connect_to_mysql

# function for create the db
def create_database(db_name):
    try:
        # connect to server
        connection = connect_to_mysql()
        if connection is not None:
            # set the cursor
            cursor = connection.cursor()

            # create the database
            cursor.execute(f'CREATE DATABASE {db_name}')
    except mysql.connector.Error as e:
        print(f'An Error occured in DB Creation:\n"{e}"')

    else:
        if connection is not None:
            # close the cursor and the connection
            cursor.close()
            connection.close()
            print('Database created successfully.')

# call the function and create the db
create_database("heroes")