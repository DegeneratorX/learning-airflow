from airflow import DAG;
from airflow.operators.bash import BashOperator
from datetime import datetime

# Cria uma DAG com id "primeira_dag", descrição, data de início (passado, presente ou futuro) e catchup (no caso de
# a DAG startar no passado, catchup True faz ela processar aquilo que não foi processado de lá pra cá.
dag = DAG('primeira_dag', description="Nossa primeira DAG", schedule_interval=None, start_date=datetime(2024,10,24), catchup=False)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 5",dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 2",dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 3",dag=dag)

task1 >> task2 >> task3