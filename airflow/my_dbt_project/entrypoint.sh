#!/bin/bash

# Clone the dbt repository
git clone https://github.com/roman-svetkin-dentsu/dbt-airflow.git 

# Navigate into the project directory
cd /airflow/my_dbt_project

# Execute the command passed to the docker run command
exec "$@"
