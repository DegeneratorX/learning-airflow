from airflow import DAG;
from airflow.operators.bash import BashOperator
from datetime import datetime

# Cria uma DAG com id "primeira_dag", descrição, data de início (passado, presente ou futuro) e catchup (no caso de
# a DAG startar no passado, catchup True faz ela processar aquilo que não foi processado de lá pra cá.
dag = DAG('primeira_dag', description="Nossa primeira DAG", schedule_interval=None, start_date=datetime(2024,10,24), catchup=False)

task1 = 