from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
'owner'                 : 'airflow',
'description'           : 'Use of the DockerOperator',
'depend_on_past'        : False,
'start_date'            : datetime(2021, 5, 1),
'email_on_failure'      : False,
'email_on_retry'        : False,
'retries'               : 1,
'retry_delay'           : timedelta(minutes=5)
}

with DAG('docker_operator_demo', default_args=default_args, schedule_interval="5 * * * *", catchup=False) as dag:
    start_dag = DummyOperator(
        task_id='start_dag'
        )

    end_dag = DummyOperator(
        task_id='end_dag'
        )        

    t1 = BashOperator(
        task_id='print_current_date',
        bash_command='date'
        )
        
    t2 = DockerOperator(
        task_id='docker_run_job_talend',
        image='raylacerda/runtalend:latest',
        container_name='task___run_job_talend',
        api_version='auto',
        auto_remove=True,
        command="/tmp/Aula1/Aula1_run.sh ",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge"
        )

    t4 = BashOperator(
        task_id='fim_job',
        bash_command='echo "Fim"'
        )

    start_dag >> t1 
    
    t1 >> t2 >> t4 >> end_dag