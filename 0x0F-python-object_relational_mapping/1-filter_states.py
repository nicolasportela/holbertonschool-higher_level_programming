#!/usr/bin/python3
""" lists all states with a name starting with N from the db hbtn_0e_0_usa """

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
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()
        for r in rows:
            print(r)
        cur.close()
        db.close()
    except Exception as e:
        print("ERROR: {}".format(e))
