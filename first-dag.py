from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor

with DAG(dag_id="first_dag", schedule_interval="*/20 * * * *" ) as dag:
    waiting_for_file = FileSensor(
        task_id="waiting_for_file",
        fs_conn_id="fs_test",
        filepath="test.txt",
        poke_interval=5,
    )
