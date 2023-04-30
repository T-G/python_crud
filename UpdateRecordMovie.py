# import mysql classes
from mysql.connector import Error

# import custom connection function
from MySqlConnetor import connect_to_mysql

# GET ALL MOVIES
movie_select_query = ("SELECT * FROM movie")

# connect and set cursor
def get_movies():
    try:
        # connect to server
        connection = connect_to_mysql()

        if connection is not None:
            # set the cursor
            cursor = connection.cursor()

            # execute the query
            cursor.execute(movie_select_query)

            # get the result
            result = cursor.fetchall()

            # print the results
            for (movie_id, movie_name, release_year) in result:
                print(f'{movie_id}\t{movie_name}\t{release_year}')

    except Error as e:
        print(f"An Error occured in Querying record:\n'{e}'")

    else:
        cursor.close()
        connection.close()

# UPDATE A RECORD
# WE WILL UPDATE RECORD #3 NAME FROM WONDER WOMAN TO WONDER WOMAN 1984
# and release_year 2017 to 2000

# set update query
movie_update_query = ("UPDATE movie SET movie_name=%s, release_year=2000 WHERE movie_id=%s")

# connect and update
def update_movie(id, name):
    try:
        connection = connect_to_mysql()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(movie_update_query, (name, id))

            # commit chnges
            connection.commit()
    except Error as e:
        print(f"An error occurred in updating records:\n'{e}'")

    else:
        print(f"{name} updated successfully.")
        cursor.close()
        connection.close()

# update the movie with id=3
#update_movie(3, 'Wonder Woman 1984')


# call the method to query
get_movies()