# import mysql classes
from mysql.connector import Error

# import custom connection function
from MySqlConnetor import connect_to_mysql

# db_name = 'heroes'
# select query to get superheroes
query = ("SELECT * FROM superhero WHERE hero_name LIKE %s")
name_starts_with = 'B%'


# connect and set cursor
def query_records():
    try:
        # connect to server
        connection = connect_to_mysql()

        if connection is not None:
            # set cursor
            cursor = connection.cursor()

            # set use db for cursor
            # cursor.execute(f"USE {db_name}")

            # execute query with parameters
            cursor.execute(query, (name_starts_with,))

            # get the result
            result = cursor.fetchall()

            # print the results
            for row in result:
                print(row)
    except Error as e:
        print(f'An error occurred in quering records:\n"{e}"')

    else:
        cursor.close()
        connection.close()

# call the query_records() method
query_records()

