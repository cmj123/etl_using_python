# modules
from google.cloud import bigquery

client = bigquery.Client(project='cultivated-link-373708')

sql = "SELECT * FROM sample_dataset.age_income LIMIT 5"

query_job = client.query(sql)

results = query_job.result()

for r in results:
    print(r.Name, r.Marital_Status, r.Age, r.Income)
