# module 
import mysql.connector 
import pandas as pd

conn = mysql.connector.connect(read_default_file = 'C:/Users/conta/.my.cnf')

query = '''
SELECT year, title, genre, avg_vote,
CASE
    WHEN avg_vote < 3 THEN 'bad'
    WHEN avg_vote < 6 THEN 'okay'
    WHEN avg_vote >=6 THEN 'good'
END as movie_rating
FROM `oscarval_sql_course`.`imdb_movies`
where year between 2005 and 2006
'''

df = pd.read_sql(query, conn)

print(df.head())
# print(df[df['year'] != 2005].head())

df.to_csv('data_files\movie_rating.csv', index=False)

conn.close()
