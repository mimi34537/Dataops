import pandas as pd
from sqlalchemy import create_engine
import boto3
from pathlib import Path

# Connexion PostgreSQL
POSTGRES_URL = "postgresql://dataops:dataops@127.0.0.1:5433/oltp"

# Connexion MinIO
MINIO_ENDPOINT = "http://127.0.0.1:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
BUCKET_NAME = "dataops"

# Tables à exporter
TABLES = [
    "customers",
    "orders",
    "products",
    "order_items"
]

OUTPUT_DIR = Path("seed_output")
OUTPUT_DIR.mkdir(exist_ok=True)

engine = create_engine(POSTGRES_URL)

s3 = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
)

# Créer le bucket s'il n'existe pas
existing_buckets = [b["Name"] for b in s3.list_buckets()["Buckets"]]

if BUCKET_NAME not in existing_buckets:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket créé : {BUCKET_NAME}")

for table in TABLES:
    print(f"Export de la table : {table}")

    df = pd.read_sql(f"SELECT * FROM public.{table}", engine)

    local_file = OUTPUT_DIR / f"{table}.parquet"
    df.to_parquet(local_file, index=False)

    s3.upload_file(
        Filename=str(local_file),
        Bucket=BUCKET_NAME,
        Key=f"bronze/{table}.parquet"
    )

    print(f"{table} envoyé dans MinIO : bronze/{table}.parquet")

print("Export PostgreSQL vers MinIO terminé.")