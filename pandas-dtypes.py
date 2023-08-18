# module 
import mysql.connector 
import pandas as pd

conn = mysql.connector.connect(read_default_file = 'C:/Users/conta/.my.cnf')

query = '''
SELECT title, genre, avg_vote
FROM `oscarval_sql_course`.`imdb_movies`
LIMIT 5
'''

df = pd.read_sql(query, conn)
print(df.head())

print(df.dtypes)

conn.close()
