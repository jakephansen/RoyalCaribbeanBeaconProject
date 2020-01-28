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


def insert_beacon(beacon_id,latitude,longitude,height,boat,island,section,number,name):
    """ insert a new beacon into the beacons table """
    sql = """INSERT INTO beacon
             VALUES(beacon_id,latitude,longitude,height,boat,island,section,number,name) ;"""
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
        cur.execute(sql, (beacon_id,latitude,longitude,height,boat,island,section,number,name,))
        # get the generated id back

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return 'Done'




def get_beacons():
    """ query data from the beacons table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT beacon_id,latitude,longitude,height,boat,island,section,number,name FROM beacon ORDER BY beacon_id")
        print("The number of beacons: ", cur.rowcount)
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

    # create_tables()
    beacon_id = 1
    latitude = '100.0000'
    longitude = '20.000'
    height = '4'
    boat = 'False'
    island = 'True'
    section = 'WaterPark'
    number = '8'
    name = 'TopSlide'
    insert_beacon(beacon_id,latitude,longitude,height,boat,island,section,number,name)
    beacon_id = 2
    latitude = '000.0000'
    longitude = '000.0000'
    height = '4'
    boat = 'False'
    island = 'True'
    section = 'WaterPark'
    number = '5'
    name = 'BottomSlide'
    insert_beacon(beacon_id,latitude,longitude,height,boat,island,section,number,name)
    get_beacons()
