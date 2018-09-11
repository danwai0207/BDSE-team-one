import pymysql;


db = pymysql.connect("localhost", "testuser", "test123", "TESTDB");


def select(query="SELECT VERSION()"):
    cursor = db.cursor()
    cursor.execute(query)
    db.close();