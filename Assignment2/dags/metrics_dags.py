from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from processor import fetch_metrics, load_metrics_to_db



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 1),

}

with DAG(

    'metrics_pipeline',
    default_args=default_args,
    description='Fetch and store metrics pipeline',
    schedule_interval=None,
    catchup=False,

    ) as dag:

    fetch_metrics_task = PythonOperator(
        task_id="fetch_metrics",
        python_callable=fetch_metrics
    )

    load_metrics_to_db_task = PythonOperator(
        task_id="load_metrics_to_db",
        python_callable=load_metrics_to_db
    )

    fetch_metrics_task >> load_metrics_to_db_task
