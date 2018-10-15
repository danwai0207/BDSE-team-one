import pymysql.cursors


def get_connection(
        db,
        host="127.0.0.1",
        port=3306,
        user="guest",
        password="password",
        charset="utf8mb4"):

    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor
    )

    return connection
