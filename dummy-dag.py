from airflow import DAG

with DAG(dag_id="dummy_dag", schedule_interval="*/20 * * * *" ) as dag:
    None
