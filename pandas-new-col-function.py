# modules 
import mysql.connector
import pandas as pd
import os 

conn = mysql.connector.connect(read_default_file = '/Users/lotannadijemeni/.my.cnf')

query = '''
SELECT year, title, genre, avg_vote, duration, 
CASE
    WHEN avg_vote < 3 THEN 'bad'
    WHEN avg_vote < 6 THEN 'okay'
    WHEN avg_vote >=6 THEN 'good'
END as movie_rating
FROM `oscarval_sql_course`.`imdb_movies`
where year between 2005 and 2006
'''

df = pd.read_sql(query, conn)

# Create duration label function
def movie_duration(d):
    if d < 60:
        return 'short movie'
    elif d < 90:
        return 'avg length movie'
    elif d < 5000:
        return 'really long movie'
    else:
        return 'no data'

df['watchability'] = df['duration'].apply(movie_duration)

print(df.head())
# print(df[df['year'] != 2005].head())

df.to_csv('movie_watchability.csv', index=False)

conn.close()
