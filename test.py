import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
try:
    uploaded_df = pd.read_csv('test.csv')
    print("CSV Columns:", uploaded_df.columns)

    required_columns = {"gene", "type", "alteration", "alt_type"}
    if not set(required_columns).issubset(uploaded_df.columns):
        raise ValueError(f"CSV file must contain these columns: {required_columns}")
    print("CSV validated successfully!")
except Exception as e:
    print(f"Error reading file: {e}")