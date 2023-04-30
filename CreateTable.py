# import mysql classes
import mysql.connector
from mysql.connector import Error, errorcode

# import custom connection function
from MySqlConnetor import connect_to_mysql

# set db name
db_name = 'heroes'

# define a dictionary for tables
tables = {}

# define superhero table
tables['superhero'] = (
    "CREATE TABLE `superhero` ("
    "  `hero_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `hero_name` varchar(40) NOT NULL,"
    "  `real_name` varchar(40) NOT NULL,"
    "  `birth_date` date NOT NULL,"
    "  `city` varchar(20) NOT NULL,"
    "  PRIMARY KEY (`hero_id`)"
    ") ENGINE=InnoDB")

# define movie table
tables['movie'] = (
    "CREATE TABLE `movie` ("
    "  `movie_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `movie_name` varchar(1000) NOT NULL,"
    "  `release_year` int(4) NOT NULL,"
    "  PRIMARY KEY (`movie_id`)"
    ") ENGINE=InnoDB")

# define heromovie table
tables['heromovie'] = (
    "CREATE TABLE `heromovie` ("
    "  `hero_id` int(11) NOT NULL,"
    "  `movie_id` int(11) NOT NULL,"
    "  `release_year` int(4) NOT NULL,"
    "  PRIMARY KEY (`hero_id`,`movie_id`),"
    "  CONSTRAINT `hero_id_fk` FOREIGN KEY (`hero_id`) "
    "     REFERENCES `superhero` (`hero_id`) ON DELETE CASCADE,"
    "  CONSTRAINT `movie_id_fk` FOREIGN KEY (`movie_id`) "
    "     REFERENCES `movie` (`movie_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


# connect and start creating tables
def start_tables_creation():
    try:
        # connect to the server
        connection = connect_to_mysql()
        print(f'Connection - CreateTable: {connection}')
        if connection is not None:
            # set the cursor
            cursor = connection.cursor()
            # set use db for cursor
            cursor.execute(f"USE {db_name}")
            # create tables
            create_tables_in_db(connection, cursor)
    except Error as e:
        print(f'An erroroccured in table creation:\n{e}')


# define the create_tables_in_db() function
def create_tables_in_db(connection, cursor):
    # create tables one by one
    for table in tables:
        table_creation_code = tables[table]
        try:
            print(f'Creation started for {table}')
            cursor.execute(table_creation_code)
        except Error as e:
            if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f'Table {table} already exists.')
            else:
                print(e.msg)
        else:
            print(f'Table {table} created successfully.')
    # close active connection
    cursor.close()
    connection.close()


# call the function to start creating the tables
# start_tables_creation()

# Check tables in database
def print_tables():
    try:
        # set connection to MySql DB Server
        connection = connect_to_mysql()
        if connection is not None:
            # set the cursor
            cursor = connection.cursor()
            # set use db for cursor
            cursor.execute(f'USE heroes')

            # execute queries to show dbs
            cursor.execute('SHOW TABLES')

            # print tables
            for table in cursor:
                print(table)
    except mysql.connector.Error as e:
        print(f'An error occures in displaying the tables:\n"{e}"')

    else:
        if connection is not None:
            # close the cursor and connection
            cursor.close()
            connection.close()

# call the function to see the tables
print_tables()


