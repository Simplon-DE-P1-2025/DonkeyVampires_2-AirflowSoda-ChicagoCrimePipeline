from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='pipeline_chicago_crimes',
    default_args=default_args,
    description='Pipeline DataOps Chicago Crime Data · Ingestion → Validation → Transformation → Chargement',
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['chicago', 'crimes', 'dataops', 'soda'],
) as dag:
    pass  # Les tasks seront ajoutées phase par phase
