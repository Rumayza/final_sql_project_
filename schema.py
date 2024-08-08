import pandas as pd

from connector import set_connection
from sqlalchemy import text

schema_creation_query = """ 
    create schema energy_data;
"""
with set_connection() as ps:
    ps.execute(text(schema_creation_query))
    ps.commit()
