'''
import raw data to sqlite name AVSC.db
'''
import pandas as pd
import sqlite3
from pandas.io import sql
import subprocess  as sp
import time
import platform


def insert_into_db(in_csv, out_sqlite, table_name, columns, chunksize):
    '''
    'in_csv'is the location of the file which be insert into db
    'out_sqlite' is the location of the db
    'table_name' is which table we wanna use
    'columns' is a list include the index of columns name
    'chunksize' is chunksize
    '''
    s = time.time()

    in_csv = '../data/transactions.csv'
    out_sqlite = '../data/AVSC.db'

    table_name = 'transactions' 
    columns = ['id', 'chain', 'dept', 'category', 'company', 'brand', 'date',
           'productsize', 'productmeasure', 'purchasequantity', 'purchaseamount']

    chunksize = 10000000 

    # to check os 
    # rows of csv file
    system_type = platform.system()
    if system_type is Windows:    # for Windows cmd  "find /V "" /C ../data/transactions.csv"
        nlines = sp.check_output(['find', '/V', '""','/C', in_csv])     # ---------- TRANSACTIONS.CSV: 349655790
        nlines = int(nlines.split()[-1])
        print('file length:', nlines)
    elif system_type is Linux:    # for Linux shell
        nlines = sp.check_output(['wc', '-l', in_csv])
        nlines = int(nlines.split()[0])
        print('file length:', nlines)
    else:
        print('your os is not Windows or Linux')

    t1 = time.time()
    print('count line cost time:',t1-s)

    cnx = sqlite3.connect(out_sqlite)

    for i in range(1, nlines, chunksize):  # csv has columns' name 0->1

        df = pd.read_csv(in_csv,
                header=None,
                nrows=chunksize,
                skiprows=i)

        df.columns = columns

        sql.to_sql(df,
                    name=table_name,
                    con=cnx,
                    index=False,
                    index_label='molecule_id',
                    if_exists='append')
    cnx.close()
    print('to db cost time:',time.time()-t1)
    print('total cost time:',time.time()-s)

if __name__ == '__main__':

    in_csv = '../data/transactions.csv'
    out_sqlite = '../data/AVSC.db'
    table_name = 'transactions'
    columns = ['id', 'chain', 'dept', 'category', 'company', 'brand', 'date',
               'productsize', 'productmeasure', 'purchasequantity', 'purchaseamount']
    chunksize = 100000

    insert_into_db(in_csv, out_sqlite, table_name, columns, chunksize)
