#!/usr/bin/python3
"""  script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa """

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
        cur.execute("SELECT cities.name FROM cities JOIN states ON \
        cities.state_id = states.id WHERE states.name LIKE %s \
        ORDER BY cities.id", (argv[4],))
        rows = cur.fetchall()
        lista = []
        for r in rows:
            lista.append(r[0])
        print(", ".join(lista))
        cur.close()
        db.close()
    except Exception as e:
        print("ERROR: {}".format(e))
