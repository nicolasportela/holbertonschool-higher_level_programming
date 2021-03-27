#!/usr/bin/python3
"""  script that lists all cities from the database hbtn_0e_4_usa """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    try:
        db = MySQLdb.\
            connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
        rows = cur.fetchall()
        for r in rows:
            print(r)
        cur.close()
        db.close()
    except Exception as e:
        print("ERROR: {}".format(e))
