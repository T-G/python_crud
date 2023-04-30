from mysql.connector import Error

from MySqlConnetor import connect_to_mysql

movie_delete_query = ("DELETE FROM movie WHERE movie_id=%s")

def delete_movie(id):
    try:
        connection = connect_to_mysql()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(movie_delete_query, (id,))
            connection.commit()
    except Error as e:
        print(f"An error occurred when deleting the record.\n'{e}'")

    else:
        print(f'Movie with id={id} deleted successfully.')
        cursor.close()
        connection.close()

# delete the movie with id=4
delete_movie(4)
