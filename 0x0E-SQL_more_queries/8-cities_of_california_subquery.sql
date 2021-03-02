-- lists all the cities of California that can be found in the database
SELECT id, name FROM hbtn_0d_usa.cities WHERE (name FROM hbtn_0d_usa.states WHERE name='California') ORDER BY cities.id ASC;