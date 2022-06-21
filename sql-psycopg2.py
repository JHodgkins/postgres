import psycopg2

# connect to chinook postgres database
connection = psycopg2.connect(database="chinook")

# Build a cursor object, anything queried from DB will be in the cursor
cursor = connection.cursor()

# Query 1: select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2: select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3: select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# can use the single method for thi one so it is not in a tuple cursor.fetchone

# Query 4: select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s, [51])

# Query 5: select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6: select all tracks where the composer is "Queen" from the "Tracks" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7: select all tracks where the composer is "AC/DC" from the "Tracks" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

# Query 8: select all tracks where the composer is "Not in DB" from the "Tracks" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test2"])

# fetch the results(multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)