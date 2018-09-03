import csv
import sqlite3
import time

# connect to database (create database)
conn = sqlite3.connect('skycat.db')

# a query to create table
query = '''create table if not exists user_log_batch (
               user_id int,
               item_id int,
               cat_id int,
               seller_id int,
               brand_id int,
               time_stamp int,
               action_type int);'''

# create table
conn.execute(query)

# commit
conn.commit()

# declare a list for loading data
data = []

# a statement to insert data into table
statement = 'insert into user_log_batch values(?, ?, ?, ?, ?, ?, ?);'

# read csv
s = time.time()

# beta v1.5.0
with open('user_log_format1.csv') as f:
    records = csv.reader(f)
    conn.executemany(statement, records)

# # drop table
# conn.execute('drop table user_log_batch')

# commit
conn.commit()
conn.close()

print(time.time()-s)

