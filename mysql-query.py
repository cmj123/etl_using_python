# module 
import mysql.connector 

conn = mysql.connector.connect(read_default_file = '/Users/lotannadijemeni/.my.cnf')
cursor = conn.cursor()

query = '''
SELECT *
FROM `oscarval_sql_course`.`imdb_movies`
LIMIT 5
'''

cursor.execute(query)

for x in cursor:
    print(x[3], x[1], x[5])

conn.close()
