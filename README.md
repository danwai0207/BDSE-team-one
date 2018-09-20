# python_mysql

## Usage

***python_mysql.get_connection(parameters)***

```
import python_mysql

conn = python_mysql.get_connection(
    host="127.0.0.1",
    port=3306,
    user="guest",
    password="password"
    db="test")
    
cursor = conn.cursor()

try:
    # declare used database
    cursor.execute("use test")
    conn.commit()
    
    # there is a table "pages" in the database "test"
    cursor.execute("select * from pages")
    print("\n".join(map(str, cursor.fetchall())))
    
finally:
    conn.close()
```

## Parameter

void

## Attributes

void


## Methods

get_connection(host, port, user, password, db, charset, cursorclass)

> parameter
>
>> host: str, default="127.0.0.1"
>>
>> port: int, default=3306
>>
>> user: str, default="guest"
>>
>> password: str, default="password"
>>
>> db: str, default="test"
>>
>> charset: str, default="utf8mb4"
>>
>> cursorclass: default=pymysql.cursors.DictCursor
>
> return
>
>> connection: function, pymysql.connect(*args)


## Requirements

PyMySQL v0.9.2
