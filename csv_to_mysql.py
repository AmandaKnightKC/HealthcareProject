import pandas as pd
from sqlalchemy import create_engine
# import getpass
from dotenv import load_dotenv
from pathlib import Path
import os
import glob

# Show exactly where it's looking
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# MySQL connection details from .env

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "cms_data")

if not all([db_user, db_password, db_name]):
    raise ValueError(
        "Missing one or more required DB credentials. Check your .env file.")

# Create connection engine
engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")


# Step 1: Load CSV
# file_path = "data/enrollment/2020 OEP County-Level Public Use File.csv"  # one file example

# Set path to folder containing CSV files
csv_folder = Path(__file__).parent / "data" / "enrollment"
csv_files = glob.glob(str(csv_folder / "*.csv"))


for file_path in csv_files:
    print(f"\n Loading: {file_path}")

    # Read CSV
    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = df.columns.str.lower().str.replace(
        " ", "_").str.replace("[^0-9a-zA-Z_]", "", regex=True)

    # Derive table name from file
    # e.g. '2020 OEP County-Level Public Use File'
    base_name = Path(file_path).stem
    table_name = base_name.lower().replace(
        " ", "_").replace(",", "").replace("-", "_")

    # Write to MySQL
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
    print(f"✅ Loaded into table: {table_name}")

print("\n🎉 All CSV files loaded successfully.")


# Step 3: Write DataFrame to MySQL
table_name = 'enrollment_2020_county'
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print(f"✅ Table '{table_name}' created in database '{db_name}'!")

# Read back the data to confirm
df_preview = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 10", con=engine)
print(df_preview)
