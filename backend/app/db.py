from sqlalchemy import create_engine
import pandas as pd

DB_URL = "postgresql://user:password@postgres_server/db_name"

def get_comparison_data():
    try:
        engine = create_engine(DB_URL)
        query = "SELECT * FROM gene_variants"
        db_df = pd.read_sql(query, engine)
        return db_df
    except Exception as e:
        print(f"Error fetching database data: {e}")
        return None