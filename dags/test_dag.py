"""Test DAG."""
from airflow import DAG
from airflow.decorators import task

from datetime import datetime

from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG("Test_DAG", schedule="@daily", start_date=datetime(2024, 6, 14)):
    @task
    def zxc():
        print("Start!")


    python_job = SparkSubmitOperator(
        task_id="python_job",
        conn_id="spark-conn",
        application="jobs/idk.py",
    )

    zxc_task = zxc()

    zxc_task >> python_job
