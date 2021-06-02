#!/usr/bin/python3
import psycopg2
from config import config


def update_Database(weather_data):
    """
    Connect to the PostgreSQL database server
    Upload Weather Data
    """
    conn = None
    try:
        # read connection parameters
        params = config()
        table = params['table']
        # Using .ini file to feed the table value and deleting it since it is not accepted by the connect class
        del params['table']
        # connect to the PostgreSQL server
        print('INFO:\t\tConnecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        update = ("INSERT INTO \"{}\" ( timestamp, address, wind_dir, wind_speed, air_temp, rel_humidity, air_pressure, rain_acc) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING id;".format(
            table, weather_data['timestamp'], weather_data['address'], weather_data['wind_dir'], weather_data['wind_speed'], weather_data['air_temp'], weather_data['rel_humidity'], weather_data['air_pressure'], weather_data['rain_acc']))
        print('INFO:\t\tUpdating the database...')
        cur.execute(update)
        # display the PostgreSQL row ID
        db_response = cur.fetchone()
        # Commit changes
        print('INFO:\t\tCommitting the changes...')
        conn.commit()
        querry = 'SELECT * FROM \"{}\" WHERE id={}'.format(
            table, db_response[0])
        cur.execute(querry)
        db_response = cur.fetchall()
        print('INFO:\t\t{}'.format(db_response))
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print('ERROR:\t\t{}'.format(error))
    finally:
        if conn is not None:
            conn.close()
            print('INFO:\t\tDatabase connection closed.')
    return db_response
