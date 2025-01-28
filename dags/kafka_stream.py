from datetime import  datetime

import requests
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'airscholer',
    'start_date': datetime(2023, 8, 3, 10, 00)
}

def stream_data():
    #import json
    #import request
    res = requests.get("https://randomuser.me/api")
    res.json()

# with DAG('user_automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=stream_data
#     )

stream_data()
