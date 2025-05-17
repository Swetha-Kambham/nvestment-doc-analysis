import pandas as pd
import snowflake.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# === Step 1: Load KPI data from Excel ===
df = pd.read_excel("extracted_kpis.xlsx")

# === Step 2: Snowflake connection ===
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

cursor = conn.cursor()

# === Step 3: Insert data ===
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO investment_kpis (metric, value) VALUES (%s, %s)",
        (row["Metric"], str(row["Value"]))
    )

print("✅ Upload complete. Data inserted into Snowflake.")

cursor.close()
conn.close()
