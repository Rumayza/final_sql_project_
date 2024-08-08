import pandas as pd
from connector import set_connection

def read_query(query_name):
    with open(f'queries/{query_name}.sql', 'r') as f:
        return f.read()

def get_data(query_name):
    query = read_query(query_name)
    with set_connection() as ps:
        return pd.read_sql(query, ps)
    
def get_data_csv(csv_name):
    file_path = f'source/{csv_name}'
    df = pd.read_csv(file_path)
    df.columns = [col.lower().replace(' ', '').replace('-', '') for col in df.columns]
    df = df.astype(str).apply(lambda x: x.str.strip().str.replace(',', ''))
    return df