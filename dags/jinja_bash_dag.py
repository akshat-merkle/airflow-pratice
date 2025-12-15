from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG(dag_id="jinja_bash_example", start_date=datetime(2024,1,1), schedule="@daily", catchup=False) as dag:
    print_date = BashOperator(task_id="print_date", bash_command='echo "Run day: {{ ds }} ; Run ID: {{ run_id }}"')
    show_conn_host = BashOperator(task_id="show_conn_host", bash_command='echo "DB Host: $HOST"', env={"HOST": "{{ conn.my_db.host }}"})
    print_date >> show_conn_host