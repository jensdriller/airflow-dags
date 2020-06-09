from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator importBashOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2020, 1, 1),
    "owner": "airflow",
}

with DAG(dag_id="operator_fun_dag", schedule_interval="*/20 * * * *", default_args=default_args) as dag:
    def print_context(ds, **kwargs):
        pprint(kwargs)
        print(ds)
        return 'Whatever you return gets printed in the logs'

    def my_sleeping_function(random_base):
        """This is a function that will run within the DAG execution"""
        time.sleep(random_base)

    print_context = PythonOperator(
        task_id='print_the_context',
        provide_context=True,
        python_callable=print_context,
        dag=dag,
    )

    # Generate 5 sleeping tasks, sleeping from 0.0 to 0.4 seconds respectively
    for i in range(5):
        task = PythonOperator(
            task_id='sleep_for_' + str(i),
            python_callable=my_sleeping_function,
            op_kwargs={'random_base': float(i) / 10},
            dag=dag,
        )

    simple_echo = BashOperator(
        task_id='simple_echo',
        bash_command='echo 1',
        dag=dag,
    )

    run_info = BashOperator(
        task_id='output_run_info',
        bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
        dag=dag,
    )

    print_context >> task >> simple_echo >> run_info
