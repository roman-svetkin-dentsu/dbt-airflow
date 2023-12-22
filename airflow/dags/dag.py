from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from kubernetes.client import models as k8s
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 21),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('simple_dag', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

def my_python_function():
    # Python function to run
    print("Hello from Python!")

t2 = PythonOperator(
    task_id='python_operator',
    python_callable=my_python_function,
    dag=dag,
)

t3 = KubernetesPodOperator(
    namespace='airflow',
    image='romansvetkin/airflow-dbt-test:0.0.2',
    cmds=["dbt", "run"],
    name="dbt-run-task",
    task_id="dbt-run-task",
    get_logs=True,
    dag=dag,
    secrets=[k8s.V1SecretKeySelector(name="dbt-profiles", key="profiles.yml")],
    volume_mounts=[k8s.V1VolumeMount(
        mount_path='/root/.dbt/',
        name='dbt-profiles',
        read_only=True)],
)

t4 = KubernetesPodOperator(
    namespace='airflow',
    image='romansvetkin/airflow-dbt-test:0.0.2',
    cmds=["dbt", "test"],
    name="dbt-test-task",
    task_id="dbt-test-task",
    get_logs=True,
    dag=dag,
    secrets=[k8s.V1SecretKeySelector(name="dbt-profiles", key="profiles.yml")],
    volume_mounts=[k8s.V1VolumeMount(
        mount_path='/root/.dbt/',
        name='dbt-profiles',
        read_only=True)],
)

t1 >> t2 >> t3 >> t4  # Define dependencies
