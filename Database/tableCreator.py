# Written By Jake Hansen, Jan 2020
# This script defines the tables and creates them in the Database

#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

   # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

       # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')






def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE Wristband (
            Wristband_id SERIAL PRIMARY KEY,
            Age INTEGER NOT NULL,
            Latitude FLOAT8,
            Longitude FLOAT8,
            NearestBeacon VARCHAR(255)
        )
        """,
        """ CREATE TABLE Vacationer (
                Vacationer_ID SERIAL PRIMARY KEY,
                Name VARCHAR(255),
                Age INT,
                Height VARCHAR(255),
                Family VARCHAR(255),
                Role VARCHAR(255)
                )
        """,


        """
        CREATE TABLE Beacon(
                Beacon_id INTEGER PRIMARY KEY,
                Latitude VARCHAR(255),
                Longitude VARCHAR(255),
                Height VARCHAR(255),
                Boat BOOL,
                Island BOOL,
                Section VARCHAR(255),
                Number INT,
                Name VARCHAR(255)

        )
        """,
        """
        CREATE TABLE Movement(
                Movement_ID SERIAL PRIMARY KEY ,
                PreviousBeacon VARCHAR(255),
                CurrentBeacon VARCHAR(255),
                Wristband VARCHAR(255),
                Time VARCHAR(255)
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print("Here")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (vendor_name,))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id



def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,vendor_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # connect()
    # create_tables()
    # insert one vendor
    # insert_vendor("3M Co.")
    # # insert multiple vendors
    # insert_vendor_list([
    #     ('AKM Semiconductor Inc.',),
    #     ('Asahi Glass Co Ltd.',),
    #     ('Daikin Industries Ltd.',),
    #     ('Dynacast International Inc.',),
    #     ('Foster Electric Co. Ltd.',),
    #     ('Murata Manufacturing Co. Ltd.',)
    # ])
    get_vendors()










#
# import psycopg2
# from config import config
# try:
#     connection = psycopg2.connect(user = "postgres",
#                                   password = "Wxhuyufs1!",
#                                   host = "127.0.0.1",
#                                   port = "5432",
#                                   database = "postgres")
#
#     cursor = connection.cursor()
#     # Print PostgreSQL Connection properties
#     print ( connection.get_dsn_parameters(),"\n")
#
#     # Print PostgreSQL version
#     cursor.execute("SELECT version();")
#     record = cursor.fetchone()
#     print("You are connected to - ", record,"\n")
#
# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)
# finally:
#     #closing database connection.
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")
