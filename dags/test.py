from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os
from airflow.configuration import conf

def test_function():
    import pandas as pd

    df = pd.read_csv(os.path.join(conf.get('core', 'DAGS_FOLDER'), 'test.csv'))
    
    
    print(os.path.join(conf.get('core', 'DAGS_FOLDER'), 'test.csv'))
    print(df)
    
    # data = {
    # "calories": [420, 380, 390],
    # "duration": [50, 40, 45]
    # }

    # #load data into a DataFrame object:
    # df = pd.DataFrame(data)

    # print(df) 

my_dag = DAG(
    'simple_python_dag',
    start_date=datetime.today(),
    schedule_interval=None
)

python_task = PythonOperator(
    task_id='python_task',
    python_callable=test_function,
    dag=my_dag
)