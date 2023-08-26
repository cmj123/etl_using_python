# Needed modules
import os 
import mysql.connector
import pandas as pd 
from google.cloud import bigquery

# Variables
cur_path = os.getcwd()
data_dir = os.path.join(cur_path, 'data_files')
load_file = 'mysql_export.csv'
load_file = os.path.join(data_dir, load_file)

proj = 'cultivated-link-373708'
dataset = 'sample_dataset'
table = 'annual_movie_summary'
table_id = f'{proj}.{dataset}.{table}'

# data connections
conn = mysql.connector.connect(read_default_file = 'C:/Users/conta/.my.cnf')
client = bigquery.Client(project=proj)

# Create our SQL extract query
query = """
SELECT year, 
COUNT(DISTINCT imdb_title_id) as movie_count,
AVG(avg_vote) as avg_rating
FROM `oscarval_sql_course`.`imdb_movies`
GROUP BY `year`
"""

# Extract data
df = pd.read_sql(query,conn)

# Transform data
def year_rating(x):
    if x <= 5.65:
        return 'bad movie year'
    elif x <= 5.9:
        return 'okay movie year'
    elif x <= 7:
        return 'great movie year'
    else:
        return 'not rated'
    
# Transformation by derivation
df['year_rating'] = df['avg_rating'].apply(year_rating)
df.to_csv(load_file, index=False)

# Load data
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition='WRITE_TRUNCATE'
)

# Open file for loading
with open(load_file, 'rb') as file:
    load_job = client.load_table_from_file(
        file,
        table_id,
        job_config=job_config
    )

load_job.result()

destination_table = client.get_table(table_id)
print(f"You have {destination_table.num_rows} rows in your table.")