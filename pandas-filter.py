# module 
import mysql.connector 
import pandas as pd

conn = mysql.connector.connect(read_default_file = '/Users/lotannadijemeni/.my.cnf')

query = '''
SELECT year, title, genre, avg_vote
FROM `oscarval_sql_course`.`imdb_movies`
where year between 2005 and 2006
'''

df = pd.read_sql(query, conn)

print(df[df['year'] != 2005].head())

df.to_csv('data_files.csv', index=False)

conn.close()
