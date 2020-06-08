from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor

from datetime import datetime

default_args = {
    "start_date" : datetime(2020, 1, 1),
    "owner": "airflow",
}

with DAG(dag_id="first_dag", schedule_interval="*/20 * * * *", default_args=default_args) as dag:
    waiting_for_file = FileSensor(
        task_id="waiting_for_file",
        fs_conn_id="fs_test",
        filepath="test.txt",
        poke_interval=5,
    )
