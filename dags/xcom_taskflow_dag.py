from datetime import datetime
from airflow.sdk import dag, task
@dag(dag_id="xcom_taskflow_example", start_date=datetime(2024,1,1), schedule=None, catchup=False)
def xcom_taskflow_example():
    @task()
    def extract():
        return {"a": 10, "b": 32}
    @task()
    def transform(values: dict) -> int:
        return sum(values.values())
    @task()
    def load(total: int):
        print(f"Total is {total}")
    vals = extract()
    tot = transform(vals)
    load(tot)
xcom_taskflow_example()