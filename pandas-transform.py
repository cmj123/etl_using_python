# modules 
import mysql.connector
import pandas as pd
import os 

conn = mysql.connector.connect(read_default_file = 'C:/Users/conta/.my.cnf')

query = '''
SELECT *
FROM `oscarval_sql_course`.`city_house_prices`
'''

df = pd.read_sql(query, conn)

# data tranformation steps
df.set_index('Date', inplace=True)
df = df.stack().reset_index()

df.columns = ['date', 'city', 'price']
df[['state','city']] = df['city'].str.split('-',expand=True)
df = df[['date','state','city','price']]

df.to_csv('data_files\city_housing.csv', index=False)

print(df.head())

conn.close()
