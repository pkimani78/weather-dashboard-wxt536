#!/usr/bin/python3
import psycopg2
import datetime
from config import config
import pandas as pd


def return_query_Timestamps(days):
    '''
    Returns the 'between' timestamps to conduct a querry
    '''
    last_date = str(datetime.date.today()) + ' 23:59:59'
    first_date = str(datetime.date.today() -
                     datetime.timedelta(days)) + ' 00:00:00'

    return first_date, last_date


def query_Database(first_date, last_date):
    """
    Connect to the PostgreSQL database server
    Querry Weather Data
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
        query = ("SELECT * FROM \"{}\" WHERE timestamp BETWEEN '{}' AND '{}';".format(
            table, first_date, last_date))
        #query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{}';".format(table)
        print('INFO:\t\tQuerying the database...\n', query)
        df = pd.read_sql_query(query, con=conn)
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print('ERROR:\t\t{}'.format(error))
    finally:
        if conn is not None:
            conn.close()
            print('INFO:\t\tDatabase connection closed.')
    return df


if __name__ == '__main__':
    first_day, last_day = return_query_Timestamps(7)
    df = query_Database(first_day, last_day)
    print(df)
