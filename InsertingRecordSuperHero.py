# read csv files
import csv

superheroes = []
movies = []

def get_data_as_dict(path):
    file = open(path)
    reader = csv.DictReader(file)
    list_of_data = []
    for row in reader:
        list_of_data.append(row)
    file.close()
    return list_of_data

# fill the lists
superheroes = get_data_as_dict('data/superhero.csv')
movies = get_data_as_dict('data/movie.csv')

for hero in superheroes:
    print(hero)

for movie in movies:
    print(movie)

# import mysql classes
from mysql.connector import Error

# import custom connection function
from MySqlConnetor import connect_to_mysql

# set db name
db_name = 'heroes'

# connect and set cursor
def start_record_insert():
    try:
        # connect to server
        connection = connect_to_mysql()

        if connection is not None:
            # set the cursor
            cursor = connection.cursor()

            # set use db for cursor
            cursor.execute(f'USE {db_name}')

            # insert superheroes
            insert_superheroes(cursor)

            # insert movies
            insert_movies(cursor)
    except Error as e:
        print(f'An error occurred in record creation.\n"{e}"')

    else:
        # commit to the database
        connection.commit()
        cursor.close()
        connection.close()

# function for inserting superheroes
def insert_superheroes(cursor):
    # convert str to date for birth_date
    str_to_date("birth_date")
    sql_superhero_command = ("INSERT INTO superhero (hero_name, real_name,birth_date,city) VALUES (%(hero_name)s, %(real_name)s, %(birth_date)s, %(city)s)")

    for superhero in superheroes:
        cursor.execute(sql_superhero_command, superhero)

    print("Superheroes inserted.")

# function to converting str to date
def str_to_date(column_name):
    from datetime import datetime
    for hero in superheroes:
        str_date = hero[column_name]
        date_format = "%d.%m.%Y"
        hero[column_name] = datetime.strptime(str_date, date_format).date()


# function for inserting movies
def insert_movies(cursor):
    sql_movie_command = ("INSERT INTO movie (movie_name, release_year) VALUES(%(movie_name)s, %(release_year)s)")
    for movie in movies:
        cursor.execute(sql_movie_command, movie)

    print("Movies inseerted.")

# call the start function
start_record_insert()