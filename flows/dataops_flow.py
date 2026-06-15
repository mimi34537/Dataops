from prefect import flow, task
import subprocess

PROJECT_DIR = "/Users/mihasoarajoelisolo/Downloads/Dataops"
DBT_ENV = f"{PROJECT_DIR}/dbt-env/bin"


def run_command(name, command):
    print(f"\n========== {name} ==========")
    result = subprocess.run(command, cwd=PROJECT_DIR)

    if result.returncode != 0:
        print(f"⚠️ {name} terminé avec erreur ou anomalie")
        if name != "Soda scan":
            raise subprocess.CalledProcessError(result.returncode, command)
    else:
        print(f"✅ {name} terminé")


@task
def seed_postgres():
    run_command(
        "Seed PostgreSQL",
        [f"{DBT_ENV}/python", "seed_environment.py"]
    )


@task
def postgres_to_minio():
    run_command(
        "Ingestion PostgreSQL vers MinIO",
        [f"{DBT_ENV}/python", "flows/postgres_to_minio.py"]
    )


@task
def dbt_run():
    run_command(
        "dbt run",
        [
            f"{DBT_ENV}/dbt",
            "run",
            "--project-dir", ".",
            "--profiles-dir", "/Users/mihasoarajoelisolo/.dbt"
        ]
    )


@task
def dbt_test():
    run_command(
        "dbt test",
        [
            f"{DBT_ENV}/dbt",
            "test",
            "--project-dir", ".",
            "--profiles-dir", "/Users/mihasoarajoelisolo/.dbt"
        ]
    )


@task
def soda_scan():
    run_command(
        "Soda scan",
        [
            f"{DBT_ENV}/soda",
            "scan",
            "-d", "dataops_postgres",
            "-c", "soda/configuration.yml",
            "soda/checks.yml"
        ]
    )


@task
def run_streamlit():
    run_command(
        "Streamlit",
        [
            f"{DBT_ENV}/python",
            "-m",
            "streamlit",
            "run",
            "streamlit_app.py"
        ]
    )


@flow(name="dataops-full-pipeline")
def dataops_pipeline():
    seed_postgres()
    postgres_to_minio()
    dbt_run()
    dbt_test()
    soda_scan()
    run_streamlit()


if __name__ == "__main__":
    dataops_pipeline()