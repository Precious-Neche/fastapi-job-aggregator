from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:DAbshoki%40%2317@localhost:5432/job_aggregator"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("Connected successfully!")
except Exception as e:
    print("Connection failed:", e)
