from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def push(**context):
    context['ti'].xcom_push(key="greeting", value="Hello from upstream!")

def pull(**context):
    msg = context['ti'].xcom_pull(task_ids="push_task", key="greeting")
    print(f"Pulled: {msg}")

with DAG(dag_id="xcom_operator_example", start_date=datetime(2024,1,1), schedule=None, catchup=False) as dag:
    push_task = PythonOperator(task_id="push_task", python_callable=push)
    pull_task = PythonOperator(task_id="pull_task", python_callable=pull)
    push_task >> pull_task