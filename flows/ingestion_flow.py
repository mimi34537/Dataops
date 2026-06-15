from prefect import flow, task
from pathlib import Path
import pandas as pd

@task
def extract_data():
    return pd.DataFrame({
        "event_id": [1, 2, 3],
        "event_name": ["login", "purchase", "logout"],
        "created_at": ["2026-06-01 10:00:00", "2026-06-01 10:05:00", "2026-06-01 10:10:00"]
    })

@task
def load_to_csv(df: pd.DataFrame):
    output_dir = Path("seed_output")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "events.csv"
    df.to_csv(output_path, index=False)
    return str(output_path)

@flow(name="local-ingestion-flow")
def ingestion_flow():
    df = extract_data()
    path = load_to_csv(df)
    print(f"Fichier généré : {path}")

if __name__ == "__main__":
    ingestion_flow()
